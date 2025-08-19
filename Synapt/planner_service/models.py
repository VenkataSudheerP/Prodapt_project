from pydantic import BaseModel

class SubTask(BaseModel):
    type: str
    details: dict

class PlanSummary(BaseModel):
    itinerary: list
    total_cost: float
    notes: str
