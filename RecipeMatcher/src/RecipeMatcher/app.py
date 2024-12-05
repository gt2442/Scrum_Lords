import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .pages.homePage import create_home_page
from .pages.loginPage import create_login_page
from .pages.mealdbTest import create_mealdb_test_page
from .pages.chatBotPage import create_chatbot_page
from .pages.api import ChatBot  # Import the ChatBot class from api.py
import os
from dotenv import load_dotenv

load_dotenv()

class MyApp(toga.App):
    def startup(self):
        print("Starting up MyApp...")
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create a ChatBot instance
        self.chatbot = ChatBot(api_key=os.getenv("OPEN_AI_KEY"))

        # Result display area for showing outputs
        self.result_display = toga.MultilineTextInput(
            readonly=True,
            style=Pack(height=200, padding=5)
        )

        # Page switching buttons
        nav_box = toga.Box(style=Pack(direction=COLUMN, padding=10, width=150))
        home_button = toga.Button(
            "Home Page",
            on_press=self.show_home_page,
            style=Pack(padding=5)
        )
        login_button = toga.Button(
            "Login Page",
            on_press=self.show_login_page,
            style=Pack(padding=5)
        )
        mealdb_button = toga.Button(
            "MealDB Test Page",
            on_press=self.show_mealdb_test_page,
            style=Pack(padding=5)
        )
        chatbot_button = toga.Button(
            "ChatBot Page",
            on_press=self.show_chatbot_page,
            style=Pack(padding=5)
        )

        nav_box.add(home_button)
        nav_box.add(login_button)
        nav_box.add(mealdb_button)
        nav_box.add(chatbot_button)

        # Content area for displaying selected page
        self.content_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Main content area (nav_box and content_box side by side)
        content_area = toga.Box(style=Pack(direction="row"))
        content_area.add(nav_box)
        content_area.add(self.content_box)

        # Main layout (content_area above result_display)
        main_box = toga.Box(style=Pack(direction="column"))
        main_box.add(content_area)
        main_box.add(self.result_display)

        self.main_window.content = main_box

        # Show the home page by default
        self.show_home_page()

        self.main_window.show()

    # Methods for page switching
    def show_home_page(self, widget=None):
        self._load_page(create_home_page(self))

    def show_login_page(self, widget=None):
        self._load_page(create_login_page(self.result_display))

    def show_mealdb_test_page(self, widget=None):
        self._load_page(create_mealdb_test_page(self.result_display))

    def show_chatbot_page(self, widget=None):
        # Remove existing children
        for child in self.content_box.children[:]:
            self.content_box.remove(child)

        # Add the ChatBot page widget
        self.content_box.add(create_chatbot_page(self.result_display, self.chatbot))

    def _load_page(self, page_content):
        # Remove existing children
        for child in self.content_box.children[:]:
            self.content_box.remove(child)
        # Add the new page widget
        self.content_box.add(page_content)

# import toga
# from toga.style import Pack

# from RecipeMatcher.user_profile import build_user_profile_page
# from RecipeMatcher.user_auth import build_auth_page
# from RecipeMatcher.home_page import build_app


# class RecipeMatcher(toga.App):
#     def startup(self):
#         self.main_window = toga.MainWindow(title=self.formal_name)

#         # Create main content box that will hold pages
#         self.content_box = toga.Box(style=Pack(direction="column"))

#         # Display the initial home page
#         self.show_app()

#         # Set the main window content
#         self.main_window.content = self.content_box
#         self.main_window.show()

#     def show_app(self, widget=None):
#         # Clear current content and add home page
#         self.clear_content_box()
#         app = build_app(self.show_sign_up_page, self.show_user_profile_page)
#         self.content_box.add(app)

#     def show_sign_up_page(self, widget):
#         # Clear current content and add sign up page
#         self.clear_content_box()
#         user_auth = build_auth_page(self.show_app)
#         self.content_box.add(user_auth)

#     def show_user_profile_page(self, widget):
#         # Clear current content and add user profile page
#         self.clear_content_box()
#         user_profile = build_user_profile_page(self.show_app)
#         self.content_box.add(user_profile)

#     def clear_content_box(self):
#         # This method clears all children from the content box
#         self.content_box.clear()


# def main():
#     return RecipeMatcher()


