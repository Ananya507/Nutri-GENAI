# 🍽️ NutriGenAI – AI-Powered Smart Recipe Generator & Nutrition Analyzer

## 📌 Overview

NutriGenAI is a multimodal AI application that analyzes food images, identifies dishes and ingredients, generates recipes, estimates nutritional values, and recommends healthier alternatives.

The system combines Computer Vision, Large Language Models (LLMs), and Nutrition Analytics to provide personalized cooking and dietary insights.

---

## 🚀 Features

### 🖼️ Food Image Analysis

* Upload food images
* Detect dishes and visible ingredients
* Identify sauces and garnishes

### 🤖 AI Recipe Generation

* Generate complete recipes from food images
* Step-by-step cooking instructions
* Cooking and preparation time estimation

### 🥗 Nutrition Analysis

* Calorie estimation
* Protein, carbohydrate, fat, and fiber analysis
* Nutritional breakdown of ingredients

### 💪 Healthier Alternatives

* Low-calorie recipe recommendations
* High-protein modifications
* Vegan and vegetarian substitutions
* Healthy ingredient replacements

### 📅 Meal Planning

* Personalized meal plans
* Goal-based recommendations:

  * Weight Loss
  * Muscle Gain
  * Maintenance

---

## 🏗️ System Architecture

Food Image
↓
Computer Vision Analysis
↓
Dish & Ingredient Detection
↓
Recipe Generation
↓
Nutrition Analysis
↓
Health Recommendation Engine
↓
Personalized Meal Suggestions

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & Machine Learning

* Google Gemini API
* Computer Vision
* Prompt Engineering

### Data Sources

* USDA FoodData Central API

### Backend

* Python

### Libraries

* Streamlit
* Pillow
* Requests
* Python-dotenv
* Google Generative AI

---

## 📂 Project Structure

NutriGenAI/

├── app.py

├── modules/

│ ├── ingredient_detector.py

│ ├── recipe_generator.py

│ ├── nutrition_analyzer.py

│ ├── meal_planner.py

│ └── substitutions.py

├── .env

├── requirements.txt

└── README.md

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/NutriGenAI.git

cd NutriGenAI

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Example Workflow

1. Upload a food image.
2. AI identifies the dish and ingredients.
3. Recipe is automatically generated.
4. Nutritional values are estimated.
5. Healthier alternatives are suggested.


---

## 📈 Potential Applications

* Smart Cooking Assistants
* Diet Planning Platforms
* Health & Fitness Applications
* Personalized Nutrition Systems
* AI-powered Food Recommendation Systems

---

## 👩‍💻 Author

Ananya Majumdar


Interested in Artificial Intelligence, Machine Learning, Computer Vision, and Generative AI.
