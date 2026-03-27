from services.llm_service import generate_itinerary

def trip_planner_agent(destination, days, interests):
    
    # Agent responsibility: planning only
    itinerary = generate_itinerary(destination, days, interests)

    return {
        "agent": "trip_planner",
        "itinerary": itinerary
    }