import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import webbrowser  # To open the OAuth URL in the default web browser
from .api import authenticate_user, fetch_users, add_user

def create_login_page(app):
    """Create the login page UI."""
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    # Display area for results or messages
    result_display = toga.MultilineTextInput(
        value="",
        readonly=True,
        style=Pack(width=400, height=150, padding=(10, 0))
    )

    # Login Form
    username_input = toga.TextInput(placeholder="Enter username", style=Pack(padding=5))
    password_input = toga.PasswordInput(placeholder="Enter password", style=Pack(padding=5))
    
    def login_action(widget):
        username = username_input.value
        password = password_input.value
        if not username or not password:
            result_display.value = "Please enter both username and password."
            return

        # Authenticate user using the backend API
        result = authenticate_user(username, password)
        if "error" in result:
            result_display.value = result["error"]
        else:
            result_display.value = f"Welcome, {result['username']}!"
            app.logged_in_user = result  # Store logged-in user in the app instance

    login_button = toga.Button("Login", on_press=login_action, style=Pack(padding=5))

    # Signup Form
    signup_username = toga.TextInput(placeholder="New username", style=Pack(padding=5))
    signup_email = toga.TextInput(placeholder="New email", style=Pack(padding=5))
    signup_password = toga.PasswordInput(placeholder="New password", style=Pack(padding=5))

    def signup_action(widget):
        username = signup_username.value
        email = signup_email.value
        password = signup_password.value
        if not username or not email or not password:
            result_display.value = "All fields are required for signup."
            return

        # Add user via backend API
        result = add_user(username, email, password)
        result_display.value = result

    signup_button = toga.Button("Sign Up", on_press=signup_action, style=Pack(padding=5))

    # Fetch Users (for debugging purposes)
    def fetch_users_action(widget):
        users = fetch_users()
        result_display.value = users

    fetch_users_button = toga.Button("Fetch Users", on_press=fetch_users_action, style=Pack(padding=5))

    # Google OAuth Login
    def google_login_action(widget):
        # Open the browser to initiate the Google OAuth flow
        oauth_url = "http://localhost:5000/login/google"
        webbrowser.open(oauth_url)
        result_display.value = "Opened browser for Google login. Complete the process there."

    google_login_button = toga.Button("Login with Google", on_press=google_login_action, style=Pack(padding=5))

    # Add components to the main box
    main_box.add(toga.Label("Login", style=Pack(padding=5)))
    main_box.add(username_input)
    main_box.add(password_input)
    main_box.add(login_button)
    main_box.add(google_login_button)

    main_box.add(toga.Label("Sign Up", style=Pack(padding=5)))
    main_box.add(signup_username)
    main_box.add(signup_email)
    main_box.add(signup_password)
    main_box.add(signup_button)
    
    main_box.add(fetch_users_button)
    main_box.add(result_display)

    return main_box
