# Bon Voy-AI-ge ✈️

An AI-powered travel itinerary planner built with Python and Flask.

## Features
- Generate day-by-day travel itineraries using Claude AI
- Interactive map with all stops pinned
- Google Maps & Apple Maps links for every location
- Packing list, Spotify playlist suggestion, local tips
- Budget slider with multi-currency support (USD, EUR, GBP, TRY, JPY)
- Date picker with automatic trip length calculation
- PDF export

## Tech Stack
- Python / Flask
- Anthropic Claude API (claude-haiku)
- Leaflet.js for maps
- Pinyon Script + Cormorant Garamond typography

## Setup
```bash
pip install flask anthropic python-dotenv
echo "ANTHROPIC_API_KEY=your_key" > .env
python3 app.py
```

