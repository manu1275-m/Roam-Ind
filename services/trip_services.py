from models.travel_request import TravelRequest
from services.llm_service import generate_itinerary

def plan_trip_service(request: TravelRequest):

    itinerary = generate_itinerary(
        request.destination,
        request.days,
        request.interests
    )

    return {
        "destination": request.destination,
        "days": request.days,
        "budget": request.budget,
        "itinerary": itinerary,
        "status": "success"
    }