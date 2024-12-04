import httpx
import requests
from openai import OpenAI

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
<<<<<<< HEAD
        return {"error": "Authentication failed."}

def generate_grocery_list(ingredients):
    """Generate a formatted grocery list from a list of ingredients."""
    if not ingredients:
        return "No ingredients provided to generate a grocery list."
    grocery_list = "\n".join([f"- {ingredient}" for ingredient in ingredients])
    return f"Grocery List:\n{grocery_list}"
=======
        return {"error": "Authentication failed"}

class ChatBot:
    def __init__(self, api_key):
        # Set your OpenAI API key
        self.client = OpenAI(api_key=api_key)
        


    def generate_meal_plan(self, prompt):
        """
        Calls OpenAI API to generate a meal plan based on the user prompt.
        """
        try:
            # Use the updated API method
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  
                messages=[
                    #Gothom
                    # {"role": "system", "content": "You are a helpful chief that generates meal plans and recipes. I want you to respond in the tone of batman, randomly mention protecting gothom"},
                   #Wabbits 
                   # {"role": "system", "content": "You are a helpful chief that generates meal plans and recipes. Take the persona of Elmer Fudd randomly recommending rabbits as the side of a real meal"},
                    #QuickConversation 
                    # {"role": "system", "content": "You are a helpful chief that generates meal plans and recipes."+
                    #  "Ask the user a few questions to get to the best meal for them then use those answers to find the proper meal"
                    #  },
                    #Main Function 
                    # {"role": "system", "content": "You are a helpful chief that generates meal plans and recipes"},

                   {"role": "system", "content": "You are a helpful chief that generates meal plans and recipes. Take the persona of Elmer Fudd randomly recommending rabbits as the side of a real meal"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=100
            )
            # Extract and return the response from the API
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return "Sorry, there was an error while generating the response."
>>>>>>> edb2f631413d2204ea3c141b0d9379ddc252a42f
