def restaurant_agent(destination, budget):

    return {
        "agent": "restaurant",
        "recommendations": [
            f"Famous local restaurant in {destination}",
            f"Budget-friendly food spots in {destination}",
            f"Top-rated cafes in {destination}"
        ],
        "estimated_cost": f"₹{budget//10} - ₹{budget//5}"
    }