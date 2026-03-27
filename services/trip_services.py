from models.travel_request import TravelRequest
from agents.supervisor_agent import supervisor_agent

def plan_trip_service(request: TravelRequest):
    try:
        response = supervisor_agent(request)

        return {
            "destination": response["destination"],
            "days": response["days"],
            "itinerary": response["itinerary"],
            "restaurants": response["restaurants"],
            "stays": response["stays"],
            "transport": response["transport"],
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }