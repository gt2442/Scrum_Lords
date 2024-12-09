# src/RecipeMatcher/pages/loginPage.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .api import authenticate_user, fetch_users, add_user

def create_login_page(result_display):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    # Username and password input fields
    username_input = toga.TextInput(placeholder="Enter username", style=Pack(padding=5, flex=1))
    password_input = toga.PasswordInput(placeholder="Enter password", style=Pack(padding=5, flex=1))

    result_display = toga.MultilineTextInput(
        value="",
        readonly=True,
        style=Pack(width=400, height=150, padding=(10, 0))
    )

    # Function to handle login
    def login_action(widget):
        username = username_input.value
        password = password_input.value
        #fetch_users
        result = authenticate_user(username, password)
        if "error" in result:
            result_display.value = result["error"]
        else:
            result_display.value = f"Welcome, {result['username']}!"

#add a button for fetch users
# Function to handle fetching users 
    def fetch_users_action(widget):
        users = fetch_users()  # Call the fetch_users function        
        result_display.value = users  # Display the fetched users in the result display

# Fetch users button  
    fetch_users_button = toga.Button("Fetch Users", on_press=fetch_users_action, style=Pack(padding=5))

     # Add User Form
    add_username_input = toga.TextInput(placeholder="New username", style=Pack(padding=5))
    add_email_input = toga.TextInput(placeholder="New email", style=Pack(padding=5))
    add_password_input = toga.PasswordInput(placeholder="New password", style=Pack(padding=5))

    def add_user_action(widget):    
        username = add_username_input.value
        email = add_email_input.value
        password = add_password_input.value
        if not username or not email or not password:
            result_display.value = "All fields are required to add a user!"
        else:
            result = add_user(username, email, password)
            result_display.value = result
 
    # Add User button
    add_user_button = toga.Button("Add User", on_press=add_user_action, style=Pack(padding=5))
    
    # Login button
    login_button = toga.Button("Login", on_press=login_action, style=Pack(padding=5))


    # Add components to the main box
    main_box.add(username_input)
    main_box.add(password_input)
    main_box.add(login_button)
    main_box.add(fetch_users_button)
    main_box.add(add_username_input)    
    main_box.add(add_email_input)    
    main_box.add(add_password_input)     
    main_box.add(add_user_button)
    main_box.add(result_display)

    return main_box

