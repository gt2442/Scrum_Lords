import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from .api import search_meal_by_name, get_random_meal, list_all_categories, generate_grocery_list, add_to_favorites
from RecipeMatcher.pages.style import LABEL_STYLE, BUTTON_STYLE, CONTAINER_STYLE

def create_mealdb_test_page(result_display):
    # Main container with styling
    main_box = toga.Box(style=CONTAINER_STYLE)

    result_display = toga.MultilineTextInput(
        value="",
        readonly=True,
        style=Pack(flex=1, height=150, padding=(10, 0), width=400)
    )

    grocery_list_display = toga.MultilineTextInput(
        value="",
        readonly=True,
        style=Pack(flex=1, height=150, padding=(10, 0), width=400)
    )

    meal_name_input = toga.TextInput(placeholder="Enter Search", style=Pack(padding=5, width=400))

    grocery_ingredients = []
    current_meal_instructions = ""  # To store the instructions of the currently selected meal

    def search_meal_action(widget):
        nonlocal grocery_ingredients, current_meal_instructions
        meal_name = meal_name_input.value
        result = search_meal_by_name(meal_name)
        
        if result.get("meals"):
            meals = result["meals"]
            grocery_ingredients = [
                meal.get("strIngredient" + str(i), "").strip() for meal in meals for i in range(1, 21) 
                if meal.get("strIngredient" + str(i))
            ]
            current_meal_instructions = meals[0].get("strInstructions", "No instructions available.").strip()
            display_text = "\n".join(
                f"Meal: {meal.get('strMeal', 'N/A').strip()} | Category: {meal.get('strCategory', 'N/A').strip()}"
                for meal in meals
            )
        else:
            display_text = "No meal found."
            grocery_ingredients = []
            current_meal_instructions = ""
        
        result_display.value = display_text

    search_button = toga.Button("Search", on_press=search_meal_action, style=BUTTON_STYLE)

    def display_cooking_instructions_action(widget):
        if current_meal_instructions:
            result_display.value = f"Cooking Instructions:\n{current_meal_instructions}"
        else:
            result_display.value = "No instructions available. Please select a meal first."

    select_button = toga.Button("Select", on_press=display_cooking_instructions_action, style=BUTTON_STYLE)

    def get_random_meal_action(widget):
        result = get_random_meal()

        print("API Response:", result)  # Debugging line
        
        if result.get("meals"):
            meal = result["meals"][0]
            meal_name = meal.get("name", "N/A").strip()
            meal_category = meal.get("category", "N/A").strip()
            meal_instructions = meal.get("instructions", "No instructions available.").strip()
            
            display_text = f"Random Meal:\nName: {meal_name}\nCategory: {meal_category}\nInstructions: {meal_instructions}"
        else:
            display_text = "No random meal found."
        
        result_display.value = display_text

    random_button = toga.Button("Get Random Meal", on_press=get_random_meal_action, style=BUTTON_STYLE)

    def list_all_categories_action(widget):
        result = list_all_categories()
        
        if result.get("categories"):
            categories = result["categories"]
            display_text = "\n".join(f"Category: {category.get('strCategory', 'N/A')}" for category in categories)
        else:
            display_text = "No categories found."
        
        result_display.value = display_text

    category_button = toga.Button("List All Categories", on_press=list_all_categories_action, style=BUTTON_STYLE)

    def generate_grocery_list_action(widget):
        if grocery_ingredients:
            display_text = "Grocery List:\n" + "\n".join(grocery_ingredients)
        else:
            display_text = "Please search for a meal first to generate a grocery list."
        
        grocery_list_display.value = display_text

    grocery_button = toga.Button("Generate Grocery List", on_press=generate_grocery_list_action, style=BUTTON_STYLE)

    def add_to_favorites_action(widget):
        user_id = "test_user"
        meal_name = meal_name_input.value.strip()
        result = add_to_favorites(user_id, meal_name)
        if "success" in result:
            display_text = result["success"]
        else:
            display_text = result.get("error", "An error occurred.")
        result_display.value = display_text

    favorite_button = toga.Button("Add Meal To Favorites", on_press=add_to_favorites_action, style=BUTTON_STYLE)

    # Add components to the main box
    main_box.add(meal_name_input)
    main_box.add(search_button)
    main_box.add(select_button)
    main_box.add(random_button)
    main_box.add(category_button)
    main_box.add(grocery_button)
    main_box.add(favorite_button)
    main_box.add(result_display)
    main_box.add(grocery_list_display)

    return main_box
