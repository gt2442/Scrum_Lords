import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def build_user_profile_page(return_to_home_callback):
    # Main container for the profile page
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, alignment="center"))

    # Name field
    name_label = toga.Label("Name:", style=Pack(padding=(5, 5)))
    name_input = toga.TextInput(placeholder="Enter your name", style=Pack(flex=1))

    # Email field
    email_label = toga.Label("Email:", style=Pack(padding=(5, 5)))
    email_input = toga.TextInput(placeholder="Enter your email", style=Pack(flex=1))

    # Password field
    password_label = toga.Label("Password:", style=Pack(padding=(5, 5)))
    password_input = toga.PasswordInput(placeholder="Enter your password", style=Pack(flex=1))

    # Phone number field
    phone_label = toga.Label("Phone Number:", style=Pack(padding=(5, 5)))
    phone_input = toga.TextInput(placeholder="Enter your phone number", style=Pack(flex=1))

    # Address field
    address_label = toga.Label("Address:", style=Pack(padding=(5, 5)))
    address_input = toga.TextInput(placeholder="Enter your address", style=Pack(flex=1))

    # Submit button
    submit_button = toga.Button("Submit", on_press=lambda x: submit_form(name_input, email_input, password_input, phone_input, address_input), style=Pack(padding=10))

    # Clear button
    clear_button = toga.Button("Clear", on_press=lambda x: clear_form(name_input, email_input, password_input, phone_input, address_input), style=Pack(padding=10))

    # Organize fields into rows
    fields = [
        (name_label, name_input),
        (email_label, email_input),
        (password_label, password_input),
        (phone_label, phone_input),
        (address_label, address_input)
    ]
    
    for label, input_widget in fields:
        row = toga.Box(style=Pack(direction=ROW, padding=5))
        row.add(label)
        row.add(input_widget)
        main_box.add(row)

    # Add buttons
    button_box = toga.Box(style=Pack(direction=ROW, alignment="center", padding=10))
    button_box.add(submit_button)
    button_box.add(clear_button)

    main_box.add(button_box)

    # Add "Return to Home" button
    return_button = toga.Button(
        "Return to Home", on_press=return_to_home_callback, style=Pack(padding=10)
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
