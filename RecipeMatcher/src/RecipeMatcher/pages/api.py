# src/RecipeMatcher/api.py
import httpx
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

BASE_URL = "https://www.themealdb.com/api/json/v1/1"
BACKEND_URL = "http://localhost:5000"  # Your Flask backend URL

def search_meal_by_name(meal_name):
    """Search for a meal by its name using TheMealDB API."""
    url = f"{BASE_URL}/search.php?s={meal_name}"
    response = requests.get(url)
    return response.json()

def get_random_meal():
    """Fetch a random meal using TheMealDB API."""
    url = f"{BASE_URL}/random.php"
    response = requests.get(url)
    data = response.json()

    # Check if the 'meals' key is present and contains a meal
    if data.get('meals'):
        meal = data['meals'][0]  # Assuming there is at least one meal in the response
        
        # Extracting the meal details
        meal_name = meal.get("strMeal", "Unknown")
        meal_category = meal.get("strCategory", "Unknown")
        meal_instructions = meal.get("strInstructions", "No instructions available.")
        
        # Extracting ingredients from the random meal
        ingredients = []
        for i in range(1, 21):  # The API returns up to 20 ingredients
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient:  # Only append ingredients that exist
                ingredients.append(f"{ingredient} ({measure})" if measure else ingredient)

        # Return a dictionary with the necessary details
        return {
            "meals": [{
                "name": meal_name,
                "category": meal_category,
                "instructions": meal_instructions,
                "ingredients": ingredients
            }]
        }

    return {"meals": []}  # If no meals found, return an empty list

def list_all_categories():
    """List all meal categories using TheMealDB API."""
    url = f"{BASE_URL}/categories.php"
    response = requests.get(url)
    return response.json()

def fetch_users():
    """Fetch user data from the Flask backend."""
    url = f"{BACKEND_URL}/users"
    with httpx.Client() as client:
        response = client.get(url)
    
    if response.status_code == 200:
        users = response.json()
        # Format user data as a string to display
        return "\n".join([f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}" for user in users])
    else:
        return "Failed to fetch users."

def authenticate_user(username, password):
    """Authenticate a user via the Flask backend."""
    url = f"{BACKEND_URL}/auth"
    payload = {"username": username, "password": password}
    
    with httpx.Client() as client:
        response = client.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
# <<<<<<< HEAD
         return {"error": "Authentication failed."}

def generate_grocery_list(ingredients):
    """Generate a formatted grocery list from a list of ingredients."""
    if not ingredients:
        return "No ingredients provided to generate a grocery list."
    grocery_list = "\n".join([f"- {ingredient}" for ingredient in ingredients])
    return f"Grocery List:\n{grocery_list}"
    return {"error": "Authentication failed"}

load_dotenv()

class ChatBot:
    def __init__(self):
        self.client = OpenAI(os.getenv("OPEN_AI_KEY"))
        self.conversation_history = []  # Store the conversation history
        self.persona = "You are a helpful chef that generates meal plans and recipes."

    def set_persona(self, persona):
        """
        Set a new AI persona and clear conversation history.
        """
        self.persona = persona
        self.conversation_history = [{"role": "system", "content": self.persona}]

    def generate_meal_plan(self, prompt):
        """
        Calls OpenAI API to generate a meal plan while maintaining conversation history.
        """
        try:
            if not self.conversation_history:
                self.conversation_history.append({"role": "system", "content": self.persona})

            # Append the user's input to the conversation history
            self.conversation_history.append({"role": "user", "content": prompt})

            # Call the OpenAI API
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.5,
                max_tokens=100,
            )

            # Extract the response and update the conversation history
            response = completion["choices"][0]["message"]["content"]
            self.conversation_history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return "Sorry, there was an error while generating the response."

    def clear_conversation(self):
        """
        Clears the conversation history.
        """
        self.conversation_history = [{"role": "system", "content": self.persona}]