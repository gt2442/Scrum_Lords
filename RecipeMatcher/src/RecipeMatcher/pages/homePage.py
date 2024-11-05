# src/RecipeMatcher/pages/homePage.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def create_home_page(app):
    # Main box for the home page layout
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

    # Welcome title
    title = toga.Label(
        "Welcome to RecipeMatcher!", 
        style=Pack(font_size=24, font_weight="bold", padding_bottom=10)
    )

    # Description text
    description = toga.Label(
        "Discover recipes, find meal inspirations, and interact with our AI-powered recipe assistant!",
        style=Pack(padding_bottom=20, font_size=14, text_align=CENTER)
    )

    # Button for navigating to the MealDB Test page
    mealdb_button = toga.Button(
        "Explore MealDB Recipes", 
        style=Pack(padding=5),
        on_press=app.show_mealdb_test_page
    )

    # Button for navigating to the Login page
    login_button = toga.Button(
        "Login to Your Profile", 
        style=Pack(padding=5),
        on_press=app.show_login_page
    )

    # Add components to the main box
    main_box.add(title)
    main_box.add(description)
    main_box.add(mealdb_button)
    main_box.add(login_button)

    return main_box
