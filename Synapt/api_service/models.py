from pydantic import BaseModel

class EnrichedData(BaseModel):
    flights: list
    hotels: list
    descriptions: list
