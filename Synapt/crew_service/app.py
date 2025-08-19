from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CrewAdvice(BaseModel):
    advice: str
    activities: list

@app.post("/crew/process")
async def process_crew(subtask: dict):
    # Validate budget and provide advice
    budget = subtask.get("budget", 0)
    activities = ["Cultural Event 1", "Cultural Event 2"]  # Mock activities
    advice = "Budget is valid" if budget >= 80000 else "Budget is too low"
    
    return CrewAdvice(advice=advice, activities=activities)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
