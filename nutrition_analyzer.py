import requests

API_KEY = "O85i3Vn9TEiMogTGQ3ZKKFMXtBcLYYFNuLEBko0C"

def get_nutrition(food):

    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={food}&api_key={API_KEY}"

    response = requests.get(url)

    data = response.json()

    if len(data["foods"]) == 0:
        return {}

    nutrients = {}

    for nutrient in data["foods"][0]["foodNutrients"]:

        nutrients[
            nutrient["nutrientName"]
        ] = nutrient["value"]

    return nutrients