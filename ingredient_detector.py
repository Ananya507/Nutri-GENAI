from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print(api_key)  # should print your key

genai.configure(
    api_key=api_key
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def detect_ingredients(image):

    prompt = """
You are an expert chef and nutritionist.

Analyze the uploaded food image carefully.

Instructions:

1. Identify the food dish shown in the image.
2. Identify all visible ingredients with confidence.
3. If some ingredients are not directly visible but are highly likely to be present in the dish, list them separately as inferred ingredients.
"""

    response = model.generate_content(
        [prompt, image]
    )

    return response.text