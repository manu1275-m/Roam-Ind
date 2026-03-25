from openai import OpenAI
import os

def _fallback_itinerary(destination, days, interests):
    interests = interests or ["local highlights"]
    plan = []
    for day in range(1, days + 1):
        interest = interests[(day - 1) % len(interests)]
        plan.append(f"Day {day}: Explore {interest} in {destination}")
    return "\n".join(plan)


def generate_itinerary(destination, days, interests):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return _fallback_itinerary(destination, days, interests)

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}, India.
    Interests: {', '.join(interests)}.

    Include:
    - day-wise plan
    - famous places
    - food recommendations
    - realistic travel flow
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    except Exception:
        return _fallback_itinerary(destination, days, interests)

    return response.choices[0].message.content