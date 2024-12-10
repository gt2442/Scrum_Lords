import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
from RecipeMatcher.pages.style import LABEL_STYLE, BUTTON_STYLE, CONTAINER_STYLE


def create_home_page(app, on_sign_up, on_user_profile):
    # Main container with padding, centered content, and a background color
    main_box = toga.Box( style=(CONTAINER_STYLE ))
    row1 = toga.Box(style=Pack(direction= ROW, alignment=CENTER,  padding_top=10, padding_bottom= 0))
    row2 = toga.Box(style=Pack(direction= ROW, alignment=CENTER, padding=0))
    button_size = 200

    # Decorative horizontal line for separation
    separator = toga.Box(
        style=Pack(
            height=10,
            width=800,
            background_color="#104E8B",
            padding_top=0,
            padding_bottom=0
        )
    )
    main_box.add(separator)


    # Welcome title with enhanced styling
    title = toga.Label(
        "Welcome to RecipeMatcher",
        style= Pack( font_family= "sans-serif", color="#1E90FF", font_size=40, font_weight ="bold", padding=10)
    )
    main_box.add(title)

    # Optional image for visual enhancement
    try:
        image = toga.Image("../RecipeMatcher/pages/chef_hat_logo.png")  # Replace with your image path
        image_view = toga.ImageView(image, style=Pack(width=300, height=300, padding=0))
        main_box.add(image_view)
    except Exception as e:
        print(f"Image could not be loaded: {e}")

    # Description text
    description = toga.Label(
        "Discover recipes, find meal inspirations,\n" "and interact with our AI-powered recipe assistant!",
        style=Pack(
           padding_top=0,
            padding_bottom=20,
            #width = 350,
            font_size=20,
            text_align=CENTER,
            color = "#104E8B"
        )
    )
    main_box.add(description)

    # Decorative horizontal line for separation
    separator = toga.Box(
        style=Pack(
            height=2,
            width=400,
            background_color="#A9A9A9",
            padding_top=10,
            padding_bottom=10
        )
    )
    main_box.add(separator)

    # Button for navigating to the MealDB Test page
    mealdb_button = toga.Button(
        "Explore MealDB Recipes",
        style=Pack(
            padding=5,
            width=button_size, height=100,
            background_color="#1E90FF",
            color="#104E8B"
        ),
        on_press=app.show_mealdb_test_page
    )
    row1.add(mealdb_button)
    #main_box.add(mealdb_button)
    
    #Button to go to chatbot page
    chatBot_button = toga.Button(
        "Generate Meal Ideas",
        style=Pack(
            padding=5,
            width=button_size, height=100,
            background_color="#1E90FF",
            color="white"
        ),
        on_press=app.show_chatbot_page
    )
    row1.add(chatBot_button)
    #main_box.add(chatBot_button)


    # Button for navigating to the Login page
    login_button = toga.Button(
        "Login to Your Profile",
        style=Pack(
            padding=5,
            width=button_size, height=100,
            background_color="#104E8B",
            color="white"
        ),
        on_press=app.show_login_page
    )
    row2.add(login_button)
    #main_box.add(login_button)

    # Button to go to Sign Up page with rounded borders and spacing
    sign_up_button = toga.Button(
        "Go to Sign Up",
        on_press=on_sign_up,
        style=Pack(
            padding=5,
            width=button_size, height=100,
            background_color="#104E8B",
            color="white"
        )
    )
    row2.add(sign_up_button)
    #main_box.add(sign_up_button)

    main_box.add(row1)
    main_box.add(row2)
    
    
    # Decorative horizontal line for separation
    separator = toga.Box(
        style=Pack(
            height=10,
            width=800,
            background_color="#104E8B",
            padding_top=10,
            padding_bottom=0
        )
    )
    main_box.add(separator)
    
    return main_box