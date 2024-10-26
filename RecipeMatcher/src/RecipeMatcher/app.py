"""
An application to create the meals of your wildest dreams.
"""
import requests
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

# Base URL for the API
BASE_URL = "https://www.themealdb.com/api/json/v1/1"

# API Function Definitions
def search_meal_by_name(meal_name):
    url = f"{BASE_URL}/search.php?s={meal_name}"
    response = requests.get(url)
    return response.json()

def list_meals_by_first_letter(letter):
    url = f"{BASE_URL}/search.php?f={letter}"
    response = requests.get(url)
    return response.json()

def lookup_meal_by_id(meal_id):
    url = f"{BASE_URL}/lookup.php?i={meal_id}"
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

def list_all(type):
    url = f"{BASE_URL}/list.php?{type}=list"
    response = requests.get(url)
    return response.json()

def filter_by_main_ingredient(ingredient):
    url = f"{BASE_URL}/filter.php?i={ingredient}"
    response = requests.get(url)
    return response.json()

def filter_by_category(category):
    url = f"{BASE_URL}/filter.php?c={category}"
    response = requests.get(url)
    return response.json()

def filter_by_area(area):
    url = f"{BASE_URL}/filter.php?a={area}"
    response = requests.get(url)
    return response.json()

# Toga Application with Integrated API Calls
class RecipeMatcher(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        # Text input for meal name search
        self.meal_name_input = toga.TextInput(placeholder="Enter meal name", style=Pack(padding=5))
        search_button = toga.Button(
            "Search Meal by Name", on_press=self.search_meal_action, style=Pack(padding=5)
        )

        # Button to get a random meal
        random_button = toga.Button(
            "Get Random Meal", on_press=self.get_random_meal_action, style=Pack(padding=5)
        )
        
        # Button to list all categories
        category_button = toga.Button(
            "List All Categories", on_press=self.list_all_categories_action, style=Pack(padding=5)
        )

        # Display area for showing API results
        self.result_display = toga.MultilineTextInput(readonly=True, style=Pack(height=200, padding=5))

        # Add widgets to the main box
        main_box.add(self.meal_name_input)
        main_box.add(search_button)
        main_box.add(random_button)
        main_box.add(category_button)
        main_box.add(self.result_display)

        # Main window setup
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # Action for search button
    def search_meal_action(self, widget):
        meal_name = self.meal_name_input.value
        result = search_meal_by_name(meal_name)
        self.result_display.value = str(result)  # Display result in the text area

    # Action for random meal button
    def get_random_meal_action(self, widget):
        result = get_random_meal()
        self.result_display.value = str(result)  # Display result in the text area

    # Action for list all categories button
    def list_all_categories_action(self, widget):
        result = list_all_categories()
        self.result_display.value = str(result)  # Display result in the text area

def main():
    return RecipeMatcher()
