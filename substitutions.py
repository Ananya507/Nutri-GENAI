import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def healthier_substitutes(recipe):

    prompt = f"""
    Suggest healthier substitutions
    for:

    {recipe}
    """

    response = model.generate_content(
        prompt
    )

    return response.text