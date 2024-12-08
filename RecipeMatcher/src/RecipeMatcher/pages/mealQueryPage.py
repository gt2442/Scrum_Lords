import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
from .api import get_meals_by_category

def create_meal_query_page():
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

    # Title
    title = toga.Label(
        "Meal Query Page",
        style=Pack(font_size=24, font_weight="bold", padding_bottom=10)
    )
    main_box.add(title)

    # Result display area
    result_scroll_container = toga.ScrollContainer(style=Pack(height=200, padding_top=10))
    result_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=10))
    result_scroll_container.content = result_box
    main_box.add(result_scroll_container)

    # Function to fetch meals by category
    def fetch_meals_action(widget, category):
        result_box.children.clear()  # Clear previous results

        print(f"Fetching meals for category: {category}")  # Debug log
        result = get_meals_by_category(category)
        print(f"API response: {result}")  # Debug log

        if result and "meals" in result and result["meals"]:
            for meal in result["meals"]:
                result_box.add(toga.Label(meal["strMeal"], style=Pack(padding=5, font_size=14)))
        else:
            error_message = f"No meals found for '{category}'."
            print(error_message)  # Debug log
            result_box.add(toga.Label(error_message, style=Pack(padding=5)))

    # Add buttons
    button_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding=10))
    categories = ["Breakfast", "Starter", "Dessert", "Miscellaneous"]

    for category in categories:
        button = toga.Button(
            category,
            on_press=lambda widget, cat=category: fetch_meals_action(widget, cat),
            style=Pack(padding=5, width=150)
        )
        button_box.add(button)

    main_box.add(button_box)

    return main_box
