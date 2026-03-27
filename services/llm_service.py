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

    # fallback if no API key
    if not api_key:
        return _fallback_itinerary(destination, days, interests)

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}, India.

    Interests: {', '.join(interests)}

    STRICT RULES:
    - Each day must be UNIQUE (no repetition)
    - Include DIFFERENT places each day
    - Do NOT repeat same words like "Explore"
    - Include REAL famous places in {destination}
    - Mix activities:
        * sightseeing
        * food experiences
        * adventure or relaxation
    - Make it realistic and practical

    FORMAT:
    Day 1:
    - Place name + short activity

    Day 2:
    - Different places + different activities

    Day 3:
    - New experiences only
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception:
        return _fallback_itinerary(destination, days, interests)