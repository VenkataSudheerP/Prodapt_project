from pydantic import BaseModel

class CrewAdvice(BaseModel):
    advice: str
    activities: list
