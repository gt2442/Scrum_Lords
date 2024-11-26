# src/RecipeMatcher/api.py
import httpx
import requests
from flask import jsonify

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
        
        # Use `idMeal` to check if the meal is already in the favorites
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
    url = f"{BACKEND_URL}/users"
    with httpx.Client() as client:
        response = client.get(url)
    
    if response.status_code == 200:
        users = response.json()
        # Format user data as a string to display
        return "\n".join([f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}" for user in users])
    else:
        return "Failed to fetch users"

#use this one
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