import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .api import search_meal_by_name, get_random_meal, list_all_categories, generate_grocery_list, add_to_favorites

def create_mealdb_test_page(result_display):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    # Text input for searching meals by name
    meal_name_input = toga.TextInput(placeholder="Enter meal name", style=Pack(padding=5))

    # Ingredients for the grocery list
    grocery_ingredients = []

    # Button to search meal by name
    def search_meal_action(widget):
        nonlocal grocery_ingredients
        meal_name = meal_name_input.value
        result = search_meal_by_name(meal_name)
        
        # Check if meals were returned in the result
        if result.get("meals"):
            meals = result["meals"]
            grocery_ingredients = [
                meal.get("strIngredient" + str(i), "") for meal in meals for i in range(1, 21) 
                if meal.get("strIngredient" + str(i))
            ]
            display_text = "\n".join(
                f"Meal: {meal.get('strMeal', 'N/A')}, Category: {meal.get('strCategory', 'N/A')}"
                for meal in meals
            )
        else:
            display_text = "No meal found."
            grocery_ingredients = []  # Reset grocery ingredients
        
        result_display.value = display_text

    search_button = toga.Button("Search Meal by Name", on_press=search_meal_action, style=Pack(padding=5))

    # Button to get a random meal
    def get_random_meal_action(widget):
        result = get_random_meal()

        # Debugging: Print the API response to check the structure
        print("API Response:", result)  # Debugging line
        
        # Check if "meals" exists and is not empty
        if result.get("meals"):
            meal = result["meals"][0]
            meal_name = meal.get("name", "N/A")  # Correct key for meal name
            meal_category = meal.get("category", "N/A")  # Correct key for category
            meal_instructions = meal.get("instructions", "N/A")  # Correct key for instructions
            
            display_text = f"Random Meal:\nName: {meal_name}\nCategory: {meal_category}\nInstructions: {meal_instructions}"
        else:
            display_text = "No random meal found."
        
        result_display.value = display_text

    random_button = toga.Button("Get Random Meal", on_press=get_random_meal_action, style=Pack(padding=5))

    # Button to list all categories
    def list_all_categories_action(widget):
        result = list_all_categories()
        
        # Check if categories exist in the result
        if result.get("categories"):
            categories = result["categories"]
            display_text = "\n".join(f"Category: {category.get('strCategory', 'N/A')}" for category in categories)
        else:
            display_text = "No categories found."
        
        result_display.value = display_text

    category_button = toga.Button("List All Categories", on_press=list_all_categories_action, style=Pack(padding=5))

    # Button to generate a grocery list
    def generate_grocery_list_action(widget):
        if grocery_ingredients:
            display_text = generate_grocery_list(grocery_ingredients)
        else:
            display_text = "Please search for a meal first to generate a grocery list."
        
        result_display.value = display_text

    grocery_button = toga.Button("Generate Grocery List", on_press=generate_grocery_list_action, style=Pack(padding=5))
    def add_to_favorites_action(widget):
        user_id = "test_user" #placeholder id for testing
        meal_name = meal_name_input.value
        result = add_to_favorites(user_id, meal_name)
        if "success" in result:
            display_text = result["success"]
        else:
            display_text = result.get("error", "An error occurred.")
        result_display.value = display_text

    favorite_button = toga.Button("Add Meal To Favorites", on_press=add_to_favorites_action, style=Pack(padding=5))

    # Add widgets to the main box
    main_box.add(meal_name_input)
    main_box.add(search_button)
    main_box.add(random_button)
    main_box.add(category_button)
    main_box.add(grocery_button)
    main_box.add(favorite_button)

    return main_box
