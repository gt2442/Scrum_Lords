import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from RecipeMatcher.pages.style import LABEL_STYLE, BUTTON_STYLE, CONTAINER_STYLE

def build_user_profile_page(return_to_home_callback):
    # Main container for the profile page
    main_box = toga.Box(style=CONTAINER_STYLE)

    # Name field
    name_label = toga.Label("Name:", style=LABEL_STYLE)
    name_input = toga.TextInput(placeholder="Enter your name", style=Pack(width=300, padding=(5, 5)))

    # Email field
    email_label = toga.Label("Email:", style=LABEL_STYLE)
    email_input = toga.TextInput(placeholder="Enter your email", style=Pack(width=300, padding=(5, 5)))

    # Password field
    password_label = toga.Label("Password:", style=LABEL_STYLE)
    password_input = toga.PasswordInput(placeholder="Enter your password", style=Pack(width=300, padding=(5, 5)))

    # Phone number field
    phone_label = toga.Label("Phone Number:", style=LABEL_STYLE)
    phone_input = toga.TextInput(placeholder="Enter your phone number", style=Pack(width=300, padding=(5, 5)))

    # Address field
    address_label = toga.Label("Address:", style=LABEL_STYLE)
    address_input = toga.TextInput(placeholder="Enter your address", style=Pack(width=300, padding=(5, 5)))

    # Submit button
    submit_button = toga.Button(
        "Submit",
        on_press=lambda x: submit_form(name_input, email_input, password_input, phone_input, address_input),
        style=Pack(
            background_color="#104E8B",  # DARK_BLUE from style.py
            color="white",
            padding=10,
            width=150
        )
    )

    # Clear button
    clear_button = toga.Button(
        "Clear",
        on_press=lambda x: clear_form(name_input, email_input, password_input, phone_input, address_input),
        style=Pack(
            background_color="#104E8B",  # DARK_BLUE from style.py
            color="white",
            padding=10,
            width=150
        )
    )

    # Organize fields into rows
    fields = [
        (name_label, name_input),
        (email_label, email_input),
        (password_label, password_input),
        (phone_label, phone_input),
        (address_label, address_input)
    ]
    
    for label, input_widget in fields:
        row = toga.Box(style=Pack(direction=ROW, padding=5, alignment=CENTER))
        row.add(label)
        row.add(input_widget)
        main_box.add(row)

    # Add buttons
    button_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding=10))
    button_box.add(submit_button)
    button_box.add(clear_button)

    main_box.add(button_box)

    # Add "Return to Home" button
    return_button = toga.Button(
        "Return to Home",
        on_press=return_to_home_callback,
        style=Pack(
            background_color="#104E8B",  # DARK_BLUE from style.py
            color="white",
            padding=10,
            width=200
        )
    )
    main_box.add(return_button)

    return main_box


# Function to handle form submission
def submit_form(name, email, password, phone, address):
    print(f"Name: {name.value}")
    print(f"Email: {email.value}")
    print(f"Password: {password.value}")
    print(f"Phone: {phone.value}")
    print(f"Address: {address.value}")
    # Here you could add functionality to process the data (like saving it)


# Function to clear all fields
def clear_form(name, email, password, phone, address):
    name.value = ""
    email.value = ""
    password.value = ""
    phone.value = ""
    address.value = ""
