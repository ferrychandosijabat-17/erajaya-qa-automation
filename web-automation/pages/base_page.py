from playwright.sync_api import Page

class BasePage:
    """
    Base Page class containing common actions used across all pages.
    All Page Objects inherit from this class.
    """
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specified URL and wait for DOM to load."""
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        """Click on an element. Playwright automatically waits for it to be clickable."""
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        """Clear and type text into an input field."""
        self.page.fill(selector, value)

    def get_input_value(self, selector: str) -> str:
        """Get the current value of an input field (used to verify input success)."""
        return self.page.input_value(selector)

    def get_text(self, selector: str) -> str:
        """Get inner text of an element."""
        return self.page.inner_text(selector).strip()

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible on the screen."""
        return self.page.is_visible(selector)

    def wait_for_selector(self, selector: str, timeout: int = 10000):
        """Explicitly wait for an element with timeout."""
        self.page.wait_for_selector(selector, timeout=timeout)
