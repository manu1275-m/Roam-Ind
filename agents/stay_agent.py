def stay_agent(destination, budget, travel_type):

    return {
        "agent": "stay",
        "hotels": [
            f"Budget hotel in {destination}",
            f"Mid-range hotel in {destination}",
            f"Premium stay in {destination}"
        ],
        "price_range": f"₹{budget//5} - ₹{budget//2}"
    }