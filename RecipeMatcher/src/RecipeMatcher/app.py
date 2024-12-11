import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from RecipeMatcher.user_profile import build_user_profile_page
from .pages.homePage import create_home_page
from .pages.loginPage import create_login_page
from .pages.mealdbTest import create_mealdb_test_page
from .pages.chatBotPage import create_chatbot_page
from .pages.mealQueryPage import create_meal_query_page
from .pages.api import ChatBot  
import os
from dotenv import load_dotenv

load_dotenv()

class RecipeMatcher(toga.App):
    def startup(self):
        print("Starting up RecipeMatcher...")

        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create a ChatBot instance
        self.chatbot = ChatBot(api_key=os.getenv("OPEN_AI_KEY"))

        # Create the navigation bar and content box
        self.nav_box = self.build_navigation_box()
        self.content_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        # Layout combining navigation and content areas
        layout = toga.Box(style=Pack(direction=ROW, padding=10))
        layout.add(self.nav_box)
        layout.add(self.content_box)

        # Set the content of the main window
        self.main_window.content = layout

        # Show the home page by default
        self.show_home_page()

        # Display the main window
        self.main_window.show()

    def build_navigation_box(self):
        """Create the navigation box with buttons."""
        nav_box = toga.Box(style=Pack(direction=COLUMN, padding=10, width=200))

        buttons = [
            ("Home Page", self.show_home_page),
            ("Login Page", self.show_login_page),
            ("Meal catalog", self.show_mealdb_test_page),
            ("Chatbot Page", self.show_chatbot_page),
            ("Meal Query Page", self.show_meal_query_page),
        ]

        for label, handler in buttons:
            button = toga.Button(label, on_press=handler, style=Pack(padding=5, width=180))
            nav_box.add(button)

        return nav_box

    def show_home_page(self, widget=None):
        """Display the Home Page."""
        self.clear_content_box()
        home_page = create_home_page(self, self.show_login_page, self.show_mealdb_test_page)
        self.content_box.add(home_page)

    def show_login_page(self, widget=None):
        """Display the Login Page."""
        self.clear_content_box()
        login_page = create_login_page(self)
        self.content_box.add(login_page)

    def show_mealdb_test_page(self, widget=None):
        """Display the MealDB Test Page."""
        self.clear_content_box()
        mealdb_page = create_mealdb_test_page(self)
        self.content_box.add(mealdb_page)

    def show_chatbot_page(self, widget=None):
        """Display the ChatBot Page."""
        self.clear_content_box()
        chatbot_page = create_chatbot_page(self.chatbot)
        self.content_box.add(chatbot_page)

    def show_meal_query_page(self, widget=None):
        """Display the Meal Query Page."""
        self.clear_content_box()
        meal_query_page = create_meal_query_page(self.chatbot)
        self.content_box.add(meal_query_page)

    def show_user_profile_page(self, widget=None):
        """Display the User Profile Page."""
        self.clear_content_box()
        user_profile = build_user_profile_page(self.show_home_page)
        self.content_box.add(user_profile)


    def clear_content_box(self):
        """Clears the current content in the content box."""
        for child in self.content_box.children[:]:
            self.content_box.remove(child)

def main():
    return RecipeMatcher()
