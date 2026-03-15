from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from planner import generate_itinerary_stream
import json
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    destination = data.get('destination')
    days = int(data.get('days'))
    vibe = data.get('vibe')
    budget = data.get('budget')
    currency = data.get('currency', 'USD')
    start_date = data.get('start_date', '')

    def stream():
        full_text = ""
        for chunk in generate_itinerary_stream(destination, days, vibe, budget, currency, start_date):
            full_text += chunk
            yield f"data: {json.dumps({'chunk': chunk})}\n\n"
        clean = re.sub(r'```json\s*', '', full_text)
        clean = re.sub(r'```\s*', '', clean).strip()
        try:
            parsed = json.loads(clean)
            yield f"data: {json.dumps({'done': True, 'result': parsed})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return Response(stream_with_context(stream()), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
