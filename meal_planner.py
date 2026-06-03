import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def create_plan(goal):

    prompt = f"""
    Create a 7 day meal plan.

    Goal:
    {goal}

    Include:
    Breakfast
    Lunch
    Dinner
    Snacks

    Show calories.
    """

    response = model.generate_content(
        prompt
    )

    return response.text