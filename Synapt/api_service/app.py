from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class EnrichedData(BaseModel):
    flights: list
    hotels: list
    descriptions: list

@app.post("/api/process")
async def process_api(request: dict):
    destination = request.get("destination", "").lower()
    flights_file = f'mock_data/{destination}_flights.json'
    hotels_file = f'mock_data/{destination}_hotels.json'
    events_file = f'mock_data/{destination}_events.json'

    # Load mock data
    with open(flights_file) as f:
        flights = json.load(f)
    with open(hotels_file) as f:
        hotels = json.load(f)
    with open(events_file) as f:
        events = json.load(f)

    return EnrichedData(flights=flights, hotels=hotels, descriptions=events)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
