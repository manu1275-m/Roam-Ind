from pydantic import BaseModel
from typing import List

class TravelRequest(BaseModel):
    destination: str
    days: int
    budget: int
    interests: List[str]
    travel_type: str = "solo"   # ✅ ADD THIS