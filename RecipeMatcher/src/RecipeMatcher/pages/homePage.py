import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


def create_home_page(app, on_sign_up, on_user_profile):
    # Main container with padding, centered content, and a background color
    main_box = toga.Box(
        style=Pack(
            direction=COLUMN,
            padding=20,
            alignment=CENTER,
            background_color="lightblue"  # Background color for visual appeal
        )
    )

    # Welcome title with enhanced styling
    title = toga.Label(
        "Welcome to RecipeMatcher!",
        style=Pack(
            padding=10,
            font_size=24,
            font_weight="bold",
            text_align=CENTER,
            color="darkblue"  # Text color
        )
    )
    main_box.add(title)

    # Description text
    description = toga.Label(
        "Discover recipes, find meal inspirations, and interact with our AI-powered recipe assistant!",
        style=Pack(
            padding_bottom=20,
            font_size=14,
            text_align=CENTER
        )
    )
    main_box.add(description)

    # Decorative horizontal line for separation
    separator = toga.Box(
        style=Pack(
            height=2,
            width=400,
            background_color="darkblue",
            padding_top=10,
            padding_bottom=10
        )
    )
    main_box.add(separator)

    # Button for navigating to the MealDB Test page
    mealdb_button = toga.Button(
        "Explore MealDB Recipes",
        style=Pack(
            padding=10,
            width=200,
            background_color="green",
            color="white"
        ),
        on_press=app.show_mealdb_test_page
    )
    main_box.add(mealdb_button)

    # Button for navigating to the Login page
    login_button = toga.Button(
        "Login to Your Profile",
        style=Pack(
            padding=10,
            width=200,
            background_color="blue",
            color="white"
        ),
        on_press=app.show_login_page
    )
    main_box.add(login_button)

    # Button to go to Sign Up page with rounded borders and spacing
    sign_up_button = toga.Button(
        "Go to Sign Up",
        on_press=on_sign_up,
        style=Pack(
            padding=10,
            width=200,
            background_color="green",
            color="white"
        )
    )
    main_box.add(sign_up_button)

    # Button to go to User Profile page with rounded borders and spacing
    user_profile_button = toga.Button(
        "Go to User Profile",
        on_press=on_user_profile,
        style=Pack(
            padding=10,
            width=200,
            background_color="blue",
            color="white"
        )
    )
    main_box.add(user_profile_button)

    meal_query_button = toga.Button(
    "Meal Query Page", 
    style=Pack(padding=5),
    on_press=app.show_meal_query_page
    )
    main_box.add(meal_query_button)

    # Optional image for visual enhancement
    try:
        image = toga.Image("/Users/gt/Downloads/chef hat logo.png")  # Replace with your image path
        image_view = toga.ImageView(image, style=Pack(width=100, height=100, padding=10))
        main_box.add(image_view)
    except Exception as e:
        print(f"Image could not be loaded: {e}")

    return main_box
