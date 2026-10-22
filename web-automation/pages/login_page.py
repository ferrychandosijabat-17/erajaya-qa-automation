from playwright.sync_api import Page
from pages.base_page import BasePage
from config.settings import Config

class LoginPage(BasePage):
    """
    Page Object for CURA Healthcare Login Page.
    Encapsulates locators and user actions for the login screen.
    """
    # Locators
    MAKE_APPOINTMENT_BTN = "#btn-make-appointment"
    USERNAME_INPUT = "#txt-username"
    PASSWORD_INPUT = "#txt-password"
    LOGIN_BUTTON = "#btn-login"
    ERROR_MESSAGE = "p.lead.text-danger"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        """Navigate directly to the CURA Login page."""
        self.navigate(Config.LOGIN_URL)

    def open_via_homepage(self):
        """Navigate to Homepage then click 'Make Appointment' to reach Login page."""
        self.navigate(Config.BASE_URL)
        self.click(self.MAKE_APPOINTMENT_BTN)

    def input_username(self, username: str):
        """Type username into the username input field."""
        self.fill(self.USERNAME_INPUT, username)

    def get_username_input_value(self) -> str:
        """Retrieve the current value of the username input field."""
        return self.get_input_value(self.USERNAME_INPUT)

    def input_password(self, password: str):
        """Type password into the password input field."""
        self.fill(self.PASSWORD_INPUT, password)

    def get_password_input_value(self) -> str:
        """Retrieve the current value of the password input field."""
        return self.get_input_value(self.PASSWORD_INPUT)

    def click_login(self):
        """Click the Login submit button."""
        self.page.click(self.LOGIN_BUTTON, no_wait_after=True)

    def login(self, username: str, password: str):
        """Convenience method to fill credentials and submit login."""
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Get the text of the error message alert."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self, timeout: int = 10000) -> bool:
        """Check if the login error message is visible, waiting for it to appear."""
        try:
            self.wait_for_selector(self.ERROR_MESSAGE, timeout=timeout)
            return True
        except Exception:
            return False
