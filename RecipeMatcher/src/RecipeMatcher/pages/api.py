# src/RecipeMatcher/api.py
import httpx
import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1"
BACKEND_URL = "http://localhost:5000"  # Your Flask backend URL

def search_meal_by_name(meal_name):
    url = f"{BASE_URL}/search.php?s={meal_name}"
    response = requests.get(url)
    return response.json()

def get_random_meal():
    url = f"{BASE_URL}/random.php"
    response = requests.get(url)
    return response.json()

def list_all_categories():
    url = f"{BASE_URL}/categories.php"
    response = requests.get(url)
    return response.json()

def fetch_users():
    url = f"{BACKEND_URL}/users"
    with httpx.Client() as client:
        response = client.get(url)
    
    if response.status_code == 200:
        users = response.json()
        # Format user data as a string to display
        return "\n".join([f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}" for user in users])
    else:
        return "Failed to fetch users"

def authenticate_user(username, password):
    """Authenticate user by sending a POST request to the Flask backend."""
    url = f"{BACKEND_URL}/auth"  # Assumes you have a /login route in your Flask app
    payload = {"username": username, "password": password}
    
    with httpx.Client() as client:
        response = client.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()  # Expected to return user info if successful
    else:
        return {"error": "Authentication failed"}
