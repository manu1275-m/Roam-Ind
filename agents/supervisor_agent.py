from agents.trip_planner_agent import trip_planner_agent
from agents.restaurant_agent import restaurant_agent
from agents.stay_agent import stay_agent
from agents.transport_agent import transport_agent

def supervisor_agent(request):

    # Call all agents
    trip = trip_planner_agent(
        request.destination,
        request.days,
        request.interests
    )

    restaurants = restaurant_agent(
        request.destination,
        request.budget
    )

    stays = stay_agent(
        request.destination,
        request.budget,
        request.travel_type
    )

    transport = transport_agent(
        request.destination
    )

    # Combine everything
    return {
        "destination": request.destination,
        "days": request.days,
        "itinerary": trip["itinerary"],
        "restaurants": restaurants,
        "stays": stays,
        "transport": transport,
        "status": "success"
    }