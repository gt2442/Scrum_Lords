# src/RecipeMatcher/pages/mealdbTest.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .api import search_meal_by_name, get_random_meal, list_all_categories

def create_mealdb_test_page(result_display):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    # Text input for searching meals by name
    meal_name_input = toga.TextInput(placeholder="Enter meal name", style=Pack(padding=5))

    # Button to search meal by name
    def search_meal_action(widget):
        meal_name = meal_name_input.value
        result = search_meal_by_name(meal_name)
        if result and result.get("meals"):
            meals = result["meals"]
            display_text = "\n".join(f"Meal: {meal['strMeal']}, Category: {meal['strCategory']}" for meal in meals)
        else:
            display_text = "No meal found."
        result_display.value = display_text

    search_button = toga.Button("Search Meal by Name", on_press=search_meal_action, style=Pack(padding=5))

    # Button to get a random meal
    def get_random_meal_action(widget):
        result = get_random_meal()
        if result and result.get("meals"):
            meal = result["meals"][0]
            display_text = f"Random Meal:\nName: {meal['strMeal']}\nCategory: {meal['strCategory']}\nInstructions: {meal['strInstructions']}"
        else:
            display_text = "No random meal found."
        result_display.value = display_text

    random_button = toga.Button("Get Random Meal", on_press=get_random_meal_action, style=Pack(padding=5))

    # Button to list all categories
    def list_all_categories_action(widget):
        result = list_all_categories()
        if result and result.get("categories"):
            categories = result["categories"]
            display_text = "\n".join(f"Category: {category['strCategory']}" for category in categories)
        else:
            display_text = "No categories found."
        result_display.value = display_text

    category_button = toga.Button("List All Categories", on_press=list_all_categories_action, style=Pack(padding=5))

    # Add widgets to the main box
    main_box.add(meal_name_input)
    main_box.add(search_button)
    main_box.add(random_button)
    main_box.add(category_button)

    return main_box
