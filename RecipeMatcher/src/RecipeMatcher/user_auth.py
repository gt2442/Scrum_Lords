import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def build_auth_page(return_to_home_callback):
    # Main container for the auth page
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, alignment="center"))
    
    # Title label (changes based on mode)
    title_label = toga.Label("Sign Up", style=Pack(padding=(10, 5), font_size=20))

    # Username field
    username_label = toga.Label("Username:", style=Pack(padding=(5, 5)))
    username_input = toga.TextInput(placeholder="Enter your username", style=Pack(flex=1))

    # Password field
    password_label = toga.Label("Password:", style=Pack(padding=(5, 5)))
    password_input = toga.PasswordInput(placeholder="Enter your password", style=Pack(flex=1))

    # Confirm Password field (only for Sign Up)
    confirm_password_label = toga.Label("Confirm Password:", style=Pack(padding=(5, 5)))
    confirm_password_input = toga.PasswordInput(placeholder="Confirm your password", style=Pack(flex=1))
    
    # Toggle button to switch between Sign Up and Login
    def toggle_mode(widget):
        if title_label.text == "Sign Up":
            title_label.text = "Login"
            main_box.remove(confirm_password_row)  # Hide confirm password field
            submit_button.label = "Login"
        else:
            title_label.text = "Sign Up"
            main_box.insert(4, confirm_password_row)  # Show confirm password field
            submit_button.label = "Sign Up"
    
    toggle_button = toga.Button("Switch to Login", on_press=toggle_mode, style=Pack(padding=10))

    # Submit button
    def submit_form(widget):
        if title_label.text == "Sign Up":
            # Sign Up Logic
            if password_input.value != confirm_password_input.value:
                print("Passwords do not match!")
            else:
                print(f"User '{username_input.value}' signed up successfully.")
        else:
            # Login Logic
            print(f"User '{username_input.value}' logged in.")

    submit_button = toga.Button("Sign Up", on_press=submit_form, style=Pack(padding=10))

    # Layout organization
    username_row = toga.Box(style=Pack(direction=ROW, padding=5))
    username_row.add(username_label)
    username_row.add(username_input)

    password_row = toga.Box(style=Pack(direction=ROW, padding=5))
    password_row.add(password_label)
    password_row.add(password_input)

    confirm_password_row = toga.Box(style=Pack(direction=ROW, padding=5))
    confirm_password_row.add(confirm_password_label)
    confirm_password_row.add(confirm_password_input)

    # Add everything to main box
    main_box.add(title_label)
    main_box.add(username_row)
    main_box.add(password_row)
    main_box.add(confirm_password_row)  # Initially visible
    main_box.add(submit_button)
    main_box.add(toggle_button)

    
     # Add "Return to Home" button
    return_button = toga.Button(
        "Return to Home", on_press=return_to_home_callback, style=Pack(padding=10)
    )
    main_box.add(return_button)

    return main_box
