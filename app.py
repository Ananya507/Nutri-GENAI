import streamlit as st

from PIL import Image

from modules.ingredient_detector import detect_ingredients
from modules.recipe_generator import generate_recipe
from modules.meal_planner import create_plan
from modules.substitutions import healthier_substitutes

st.set_page_config(
    page_title="NutriGenAI",
    layout="wide"
)

st.title("🥗 NutriGenAI")

goal = st.selectbox(
    "Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "Maintenance"
    ]
)

file = st.file_uploader(
    "Upload Food Image",
    type=["jpg","jpeg","png"]
)

if file:

    image = Image.open(file)

    st.image(image)

    if st.button("Analyze"):

        ingredients = detect_ingredients(
            image
        )

        st.subheader(
            "Detected Ingredients"
        )

        st.write(ingredients)

        recipe = generate_recipe(
            ingredients,
            goal
        )

        st.subheader(
            "Generated Recipe"
        )

        st.write(recipe)

        subs = healthier_substitutes(
            recipe
        )

        st.subheader(
            "Healthier Alternatives"
        )

        st.write(subs)

        meal_plan = create_plan(
            goal
        )

        st.subheader(
            "7-Day Meal Plan"
        )

        st.write(meal_plan)