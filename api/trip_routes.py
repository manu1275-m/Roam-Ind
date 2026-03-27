from fastapi import APIRouter
from models.travel_request import TravelRequest
from services.trip_services import plan_trip_service

router = APIRouter(prefix="/api", tags=["Trip"])

@router.post("/plan-trip")
def plan_trip(request: TravelRequest):
    return plan_trip_service(request)