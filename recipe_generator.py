import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_recipe(
        ingredients,
        goal):

    prompt = f"""
    Ingredients:
    {ingredients}

    Health Goal:
    {goal}

    Generate:

    1 Recipe Name
    2 Ingredients
    3 Instructions
    4 Cooking Time
    5 Estimated Calories
    """

    response = model.generate_content(
        prompt
    )

    return response.text