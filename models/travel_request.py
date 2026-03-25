from typing import List

from pydantic import BaseModel


class TravelRequest(BaseModel):
	destination: str
	days: int
	budget: int
	interests: List[str]
