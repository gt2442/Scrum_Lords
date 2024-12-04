# src/RecipeMatcher/app.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .pages.homePage import create_home_page
from .pages.loginPage import create_login_page
from .pages.mealdbTest import create_mealdb_test_page
from .pages.chatBotPage import create_chatbot_page  # Import the ChatBot page function

class MyApp(toga.App):
    def startup(self):
        print("Starting up MyApp...")
        self.main_window = toga.MainWindow(title=self.formal_name)

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
    on_press=self.show_chatbot_page,  # Update to the correct handler
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
        # Remove existing children
        for child in self.content_box.children[:]:
            self.content_box.remove(child)
        # Add the new home page widget
        self.content_box.add(create_home_page(self))

    def show_login_page(self, widget=None):
        # Remove existing children
        for child in self.content_box.children[:]:
            self.content_box.remove(child)
        # Add the new login page widget
        self.content_box.add(create_login_page(self.result_display))

    def show_mealdb_test_page(self, widget=None):
        # Remove existing children
        for child in self.content_box.children[:]:
            self.content_box.remove(child)
        # Add the new MealDB test page widget
        self.content_box.add(create_mealdb_test_page(self.result_display))

    def show_chatbot_page(self, widget=None):
        # Remove existing children
        for child in self.content_box.children[:]:
            self.content_box.remove(child)
        # Add the ChatBot page widget
        self.content_box.add(create_chatbot_page(self.result_display))

