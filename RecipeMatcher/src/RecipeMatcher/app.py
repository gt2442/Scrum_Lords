import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from RecipeMatcher.user_profile import build_user_profile_page
from RecipeMatcher.user_auth import build_auth_page
from RecipeMatcher.home_page import build_app
from .pages.homePage import create_home_page
from .pages.loginPage import create_login_page
from .pages.mealdbTest import create_mealdb_test_page
from .pages.chatBotPage import create_chatbot_page
from .pages.api import ChatBot  # Import the ChatBot class from api.py
import os
from dotenv import load_dotenv

load_dotenv()

class RecipeMatcher(toga.App):
    def startup(self):
        print("Starting up RecipeMatcher...")

        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create a ChatBot instance
        self.chatbot = ChatBot(api_key=os.getenv("OPEN_AI_KEY"))

        # Main content box for displaying pages
        self.content_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Result display area for showing outputs
        # self.result_display = toga.MultilineTextInput(
        #     readonly=True,
        #     style=Pack(height=200, padding=5)
        # )

        # Navigation buttons
        self.nav_box = self.build_navigation_box()

        # Combine navigation and content into a layout
        main_layout = toga.Box(style=Pack(direction=COLUMN, padding=10))
        content_area = toga.Box(style=Pack(direction="row", flex=1))
        content_area.add(self.nav_box)
        content_area.add(self.content_box)

        # Add the result display area below the content
        main_layout.add(content_area)
        # main_layout.add(self.result_display)

        # Set the content of the main window
        self.main_window.content = main_layout

        # Show the home page by default
        self.show_home_page()

        self.main_window.show()

    def build_navigation_box(self):
        """Create the navigation box with buttons."""
        nav_box = toga.Box(style=Pack(direction=COLUMN, padding=10, width=150))

        buttons = [
            ("Home Page", self.show_home_page),
            ("Login Page", self.show_login_page),
            ("MealDB Test Page", self.show_mealdb_test_page),
            ("ChatBot Page", self.show_chatbot_page),
            ("User Profile", self.show_user_profile_page),
            ("Sign Up", self.show_sign_up_page)
        ]

        for label, handler in buttons:
            button = toga.Button(label, on_press=handler, style=Pack(padding=5))
            nav_box.add(button)

        return nav_box

    def show_home_page(self, widget=None):
        self.clear_content_box()
        home_page = create_home_page(self, self.show_sign_up_page, self.show_user_profile_page)
        self.content_box.add(home_page)

    def show_login_page(self, widget=None):
        self.clear_content_box()
        login_page = create_login_page(self)
        self.content_box.add(login_page)

    def show_mealdb_test_page(self, widget=None):
        self.clear_content_box()
        mealdb_page = create_mealdb_test_page(self)
        self.content_box.add(mealdb_page)

    def show_chatbot_page(self, widget=None):
        self.clear_content_box()
        chatbot_page = create_chatbot_page(self.chatbot)
        self.content_box.add(chatbot_page)

    def show_user_profile_page(self, widget=None):
        self.clear_content_box()
        user_profile = build_user_profile_page(self.show_home_page)
        self.content_box.add(user_profile)

    def show_sign_up_page(self, widget=None):
        self.clear_content_box()
        sign_up_page = build_auth_page(self.show_home_page)
        self.content_box.add(sign_up_page)

    def clear_content_box(self):
        """Clears the current content in the content box."""
        for child in self.content_box.children[:]:
            self.content_box.remove(child)

def main():
    return RecipeMatcher()
