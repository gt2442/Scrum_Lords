import httpx
import requests

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
        return {"error": "Authentication failed."}

def generate_grocery_list(ingredients):
    """Generate a formatted grocery list from a list of ingredients."""
    if not ingredients:
        return "No ingredients provided to generate a grocery list."
    grocery_list = "\n".join([f"- {ingredient}" for ingredient in ingredients])
    return f"Grocery List:\n{grocery_list}"
