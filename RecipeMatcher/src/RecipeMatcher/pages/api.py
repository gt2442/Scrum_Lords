import httpx
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import jsonify
 
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
 
favorites = {}
 
def add_to_favorites(user_id, meal_name):
    # Check if user has a favorites list, if not, initialize it
    if user_id not in favorites:
        favorites[user_id] = []
    # Search for the meal by name
        result = search_meal_by_name(meal_name)
   
    # Search for the meal by name and print the result
    print(f"Attempting to add to favorites. Searching for meal: '{meal_name}'")
    result = search_meal_by_name(meal_name)
    print(f"Search result for '{meal_name}': {result}")  # Debugging output for search results
   
    # Check if the meal was found in the response
    if result and result.get("meals"):
        selected_meal = result["meals"][0]  # Get the first meal if multiple are returned
        print(f"Selected meal to add: {selected_meal}")  # Debugging output for selected meal
       
        # Use idMeal to check if the meal is already in the favorites
        existing_ids = {meal['idMeal'] for meal in favorites[user_id]}
        if selected_meal["idMeal"] not in existing_ids:
            favorites[user_id].append(selected_meal)
            print(f"Updated favorites for {user_id}: {favorites[user_id]}")  # Debug
            return {"success": f"{selected_meal['strMeal']} added to favorites"}
        else:
            print(f"Meal '{selected_meal['strMeal']}' is already in favorites")  # Debug
            return {"error": "Meal is already in favorites"}
    else:
        # Handle the case where no meal is found or data is invalid
        print("Meal not found or data is invalid.")  # Debugging output for not found case
        return {"error": "Meal not found"}
 
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
 
#use this one
def authenticate_user(username, password):
    """Authenticate a user via the Flask backend."""
    url = f"{BACKEND_URL}/auth"
    payload = {"username": username, "password": password}
   
    with httpx.Client() as client:
        response = client.post(url, json=payload)
   
    if response.status_code == 200:
        return response.json()
    else:
         return {"error": "Authentication failed."}
 
def generate_grocery_list(ingredients):
    """Generate a formatted grocery list from a list of ingredients."""
    if not ingredients:
        return "No ingredients provided to generate a grocery list."
    grocery_list = "\n".join([f"- {ingredient}" for ingredient in ingredients])
    return f"Grocery List:\n{grocery_list}"
    return {"error": "Authentication failed"}
 
#Zach's code
def add_user(username, email, password):
    """Add a user to the backend."""
    url = f"{BACKEND_URL}/users"
    data = {
        "username": username,
        "email": email,
        "password": password,
    }
    try:
        with httpx.Client() as client:
            response = client.post(url, json=data)
            if response.status_code == 201:
 
                return f"User {username} added successfully!"
            else:
                return f"Failed to add user: {response.json().get('error', 'Unknown error')}"
    except httpx.RequestError as e:
        return f"An error occurred: {str(e)}"
##Chat GPT code
load_dotenv()
class ChatBot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []  # For chatBotPage
        self.query_history = []  # For mealQueryPage
        self.default_persona = "You are a helpful chef that generates meal plans and recipes."
 
    def set_persona(self, persona):
        """Set a new AI persona."""
        self.default_persona = persona
        self.messages = [{"role": "system", "content": self.default_persona}]
 
    def chat_with_ai(self, user_input):
        """Handles conversational interaction for chatBotPage."""
        try:
            self.messages.append({"role": "user", "content": user_input})
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                temperature=0.7,
                max_tokens=150,
            )
            response = completion.choices[0].message.content
            self.messages.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            return f"Error: {e}"
 
    def generate_meal_suggestion(self, meal_time, flavor, nutrition_focus):
        """Generates meal suggestions for mealQueryPage."""
        try:
            prompt = (
                f"Generate a creative {meal_time} recipe that is {flavor} in flavor and "
                f"focuses on {nutrition_focus}. Provide ingredients and instructions."
            )
            self.query_history.append({"role": "user", "content": prompt})
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.query_history,
                temperature=0.7,
                max_tokens=200,
            )
            response = completion.choices[0].message.content
            self.query_history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            return f"Error: {e}"
 
    def clear_conversation(self):
        """Clear chatBotPage history."""
        self.messages = [{"role": "system", "content": self.default_persona}]
 
    def clear_meal_query(self):
        """Clear mealQueryPage history."""
        self.query_history = []
 
# Other API methods for MealDB remain unchanged