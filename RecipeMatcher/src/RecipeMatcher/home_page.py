import toga
from toga.style import Pack

def build_app(on_sign_up, on_user_profile):
    # Main container with padding, centered content, and a background color
    main_box = toga.Box(
        style=Pack(
            direction="column",
            padding=20,
            alignment="center",
            background_color="lightblue"  # Add a background color for visual appeal
        )
    )

    # Title label with enhanced styling
    title_label = toga.Label(
        "Welcome to the Home Page",
        style=Pack(
            padding=10,
            font_size=24,
            font_weight="bold",
            text_align="center",
            color="darkblue"  # Change the text color
        )
    )
    main_box.add(title_label)

    # Decorative horizontal line for separation
    separator = toga.Box(
        style=Pack(
            height=2,
            width=400,
            background_color="darkblue",
            padding_top=10,  # Padding for separation
            padding_bottom=10
        )
    )
    main_box.add(separator)

    # Button to go to Sign Up page with rounded borders and spacing
    sign_up_button = toga.Button(
        "Go to Sign Up",
        on_press=on_sign_up,
        style=Pack(
            padding=10,
            width=200,
            background_color="green",
            color="white",
            padding_top=5,
            padding_bottom=5,
            padding_left=10,
            padding_right=10 # Note: Toga may not support this fully; rounded appearance may be limited
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
            color="white",
            padding_top=5,
            padding_bottom=5,
            padding_left=10,
            padding_right=10 # Note: Same as above, rounded support may vary
        )
    )
    main_box.add(user_profile_button)
    


# Add an image for visual enhancement (optional, if you have an image)
    # Note: Ensure 'example_image.png' exists in your resources folder
    try:
        image = toga.Image("/Users/gt/Downloads/chef hat logo.png")  # Replace with your image path
        image_view = toga.ImageView(image, style=Pack(width=100, height=100, padding=10))
        main_box.add(image_view)
    except Exception as e:
        print(f"Image could not be loaded: {e}")


    return main_box
