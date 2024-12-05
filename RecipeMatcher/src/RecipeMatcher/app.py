import toga
from toga.style import Pack

from RecipeMatcher.user_profile import build_user_profile_page
from RecipeMatcher.user_auth import build_auth_page
from RecipeMatcher.home_page import build_app


class RecipeMatcher(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create main content box that will hold pages
        self.content_box = toga.Box(style=Pack(direction="column"))

        # Display the initial home page
        self.show_app()

        # Set the main window content
        self.main_window.content = self.content_box
        self.main_window.show()

    def show_app(self, widget=None):
        # Clear current content and add home page
        self.clear_content_box()
        app = build_app(self.show_sign_up_page, self.show_user_profile_page)
        self.content_box.add(app)

    def show_sign_up_page(self, widget):
        # Clear current content and add sign up page
        self.clear_content_box()
        user_auth = build_auth_page(self.show_app)
        self.content_box.add(user_auth)

    def show_user_profile_page(self, widget):
        # Clear current content and add user profile page
        self.clear_content_box()
        user_profile = build_user_profile_page(self.show_app)
        self.content_box.add(user_profile)

    def clear_content_box(self):
        # This method clears all children from the content box
        self.content_box.clear()


def main():
    return RecipeMatcher()


