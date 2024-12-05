print("API module loaded successfully.")

# src/RecipeMatcher/api.py
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
    return response.json()

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
