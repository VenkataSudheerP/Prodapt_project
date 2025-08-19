from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class TravelRequest(BaseModel):
    origin: str
    destination: str
    dates: list
    budget: float
    preferences: list
    email: str

@app.post("/planner/process")
async def process_request(request: TravelRequest):
    # Decompose request and call crew and api services
    crew_response = requests.post(f"http://localhost:8001/crew/process", json=request.dict())
    api_response = requests.post(f"http://localhost:8002/api/process", json=request.dict())
    
    # Aggregate results and return
    return {
        "crew": crew_response.json(),
        "api": api_response.json()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
