# src/RecipeMatcher/pages/recipeGeneration.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from RecipeMatcher.api import get_recipe_by_ingredient, get_meal_details, get_all_categories

def create_recipe_generation_page(result_display):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    # Ingredient input
    ingredient_input = toga.TextInput(placeholder="Enter main ingredient", style=Pack(padding=5))

    # Dropdown for categories
    category_dropdown = toga.Selection(style=Pack(padding=5))
    category_dropdown.items = ["All Categories"]

    # Recipe display area
    recipe_display = toga.MultilineTextInput(readonly=True, style=Pack(height=300, padding=5))

    # Fetch categories to populate dropdown
    def fetch_categories():
        result = get_all_categories()
        if result.get("categories"):
            categories = [cat["strCategory"] for cat in result["categories"]]
            category_dropdown.items = ["All Categories"] + categories

    fetch_categories()

    # Search recipes by ingredient
    def search_by_ingredient(widget):
        ingredient = ingredient_input.value.strip()
        if not ingredient:
            result_display.value = "Please enter an ingredient."
            return

        result = get_recipe_by_ingredient(ingredient)
        if result.get("meals"):
            recipe_display.value = "\n".join(
                f"Meal: {meal['strMeal']} (ID: {meal['idMeal']})"
                for meal in result["meals"]
            )
        else:
            recipe_display.value = "No recipes found for the given ingredient."

    # View meal details
    def view_meal_details(widget):
        selected_meal = recipe_display.value.split("(ID: ")[-1].strip(")\n")
        if not selected_meal:
            result_display.value = "Please select a meal to view details."
            return

        result = get_meal_details(selected_meal)
        if result.get("meals"):
            meal = result["meals"][0]
            recipe_display.value = (
                f"Meal: {meal['strMeal']}\n"
                f"Category: {meal['strCategory']}\n"
                f"Cuisine: {meal['strArea']}\n\n"
                f"Ingredients:\n" +
                "\n".join(
                    f"- {meal[f'strIngredient{i}']} ({meal[f'strMeasure{i}']})"
                    for i in range(1, 21)
                    if meal[f'strIngredient{i}']
                ) +
                f"\n\nInstructions:\n{meal['strInstructions']}"
            )
        else:
            recipe_display.value = "Meal details not found."

    # Buttons
    search_button = toga.Button("Search Recipes", on_press=search_by_ingredient, style=Pack(padding=5))
    view_button = toga.Button("View Details", on_press=view_meal_details, style=Pack(padding=5))

    # Add components to the main box
    main_box.add(ingredient_input)
    main_box.add(category_dropdown)
    main_box.add(search_button)
    main_box.add(view_button)
    main_box.add(recipe_display)

    return main_box
