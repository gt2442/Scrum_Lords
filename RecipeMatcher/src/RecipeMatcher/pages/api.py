# src/RecipeMatcher/api.py
import httpx
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

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

load_dotenv()

class ChatBot:
    def __init__(self, api_key):
        # Set your OpenAI API key
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []  # Store the conversation history
        self.default_persona = (
            "You are a helpful chef that generates meal plans and recipes."
        )  # Default persona

    def set_persona(self, persona):
        """Set a new AI persona."""
        self.default_persona = persona
        self.messages = [{"role": "system", "content": self.default_persona}]


    def generate_meal_plan(self, prompt):
        """
        Calls OpenAI API to generate a meal plan while maintaining conversation history.
        """
        try:
            # Append the user's input to the conversation history
            self.conversation_history.append({"role": "user", "content": prompt})

            # Call the API with the conversation history
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.5,
                max_tokens=100,
            )

            # Extract the response
            response = completion.choices[0].message.content

            # Append the AI's response to the conversation history
            self.conversation_history.append({"role": "assistant", "content": response})

            return response
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return "Sorry, there was an error while generating the response."

    def clear_conversation(self):
        """
        Clears the conversation history for a new session.
        """
        self.conversation_history = []
