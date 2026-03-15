import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def generate_itinerary_stream(destination, days, vibe, budget, currency, start_date):
    prompt = """You are a knowledgeable travel guide. Create a detailed itinerary.

Destination: """ + destination + """
Duration: """ + str(days) + """ days
Vibe: """ + vibe + """
Total budget: """ + str(budget) + " " + currency + """
Travel start date: """ + start_date + """
Currency for all prices: """ + currency + """

Important: Use the travel dates to provide realistic weather information for that specific time of year.
Use """ + currency + """ for all cost estimates.

Return ONLY valid JSON, no markdown, no extra text:
{
  "destination": "city",
  "days": 3,
  "vibe": "vibe",
  "budget_total": "1500",
  "currency": "USD",
  "center_lat": 0.0,
  "center_lng": 0.0,
  "tagline": "poetic 6-8 word tagline",
  "fun_fact": "surprising fun fact about destination",
  "spotify_search": "existing playlist name that fits the vibe",
  "packing_list": {
    "essentials": ["item1", "item2", "item3", "item4", "item5"],
    "clothes": ["item1", "item2", "item3", "item4"],
    "tech": ["item1", "item2", "item3"],
    "extras": ["item1", "item2", "item3"]
  },
  "itinerary": [
    {
      "day": 1,
      "date": "2024-06-01",
      "theme": "day theme",
      "weather": {"condition": "Sunny", "temp_c": 22},
      "morning": {
        "activity": "name",
        "description": "3-4 rich sentences about this activity, what makes it special, local tips.",
        "location": "specific place",
        "lat": 0.0,
        "lng": 0.0,
        "budget_breakdown": "what the cost covers",
        "cost": "15-25"
      },
      "afternoon": {
        "activity": "name",
        "description": "2 sentences max. What makes it special + one local tip.",
        "location": "specific place",
        "lat": 0.0,
        "lng": 0.0,
        "budget_breakdown": "what the cost covers",
        "cost": "15-25"
      },
      "evening": {
        "activity": "name",
        "description": "3-4 rich sentences about this activity, what makes it special, local tips.",
        "location": "specific place",
        "lat": 0.0,
        "lng": 0.0,
        "budget_breakdown": "what the cost covers",
        "cost": "15-25"
      }
    }
  ],
  "total_estimated_cost": "XXX-XXX",
  "tips": ["tip 1", "tip 2", "tip 3"]
}
Important: Return EXACTLY 3 tips, no more. Do not add extra tips.
Generate all """ + str(days) + """ days with real coordinates. Only valid JSON."""

    with client.messages.stream(
        model="claude-haiku-4-5-20251001",
max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            yield text