# src/RecipeMatcher/pages/loginPage.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .api import authenticate_user

def create_login_page(result_display):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    # Username and password input fields
    username_input = toga.TextInput(placeholder="Enter username", style=Pack(padding=5))
    password_input = toga.PasswordInput(placeholder="Enter password", style=Pack(padding=5))

    # Function to handle login
    def login_action(widget):
        username = username_input.value
        password = password_input.value
        result = authenticate_user(username, password)
        if "error" in result:
            result_display.value = result["error"]
        else:
            result_display.value = f"Welcome, {result['username']}!"

    # Login button
    login_button = toga.Button("Login", on_press=login_action, style=Pack(padding=5))

    # Add components to the main box
    main_box.add(username_input)
    main_box.add(password_input)
    main_box.add(login_button)

    return main_box


