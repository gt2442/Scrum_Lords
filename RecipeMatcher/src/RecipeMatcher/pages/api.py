# src/RecipeMatcher/api.py
import httpx
import requests
from openai import OpenAI

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
