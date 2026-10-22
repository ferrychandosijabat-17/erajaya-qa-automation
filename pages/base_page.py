import time
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from config.config import Config
from utils.logger import logger


class BasePage:
    """Base Page Object providing reusable mobile interactions and explicit waits."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)

    def find_element(self, locator: tuple, timeout: int = None):
        """Wait for element to be present in DOM and visible."""
        wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Timed out waiting for element visible: {locator}")
            self.take_screenshot(f"timeout_find_{locator[1][:20]}")
            raise

    def find_elements(self, locator: tuple, timeout: int = None):
        """Wait for elements to be present in DOM."""
        wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
        try:
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            logger.warning(f"No elements found for: {locator}")
            return []

    def click(self, locator: tuple, timeout: int = None):
        """Wait until element is clickable, then tap/click."""
        wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            logger.info(f"Clicking element: {locator}")
            element.click()
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            self.take_screenshot(f"timeout_click_{locator[1][:20]}")
            raise

    def send_keys(self, locator: tuple, text: str, clear: bool = True):
        """Send keys to element with optional clear."""
        element = self.find_element(locator)
        if clear:
            element.clear()
        logger.info(f"Typing into {locator}: '{text}'")
        element.send_keys(text)
        self.hide_keyboard_if_present()

    def get_text(self, locator: tuple) -> str:
        """Get element's visible text or content-desc/text attribute."""
        element = self.find_element(locator)
        text = element.text or element.get_attribute("text") or element.get_attribute("content-desc") or ""
        return text.strip()

    def is_displayed(self, locator: tuple, timeout: int = 5) -> bool:
        """Check if element is displayed within a short timeout."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def hide_keyboard_if_present(self):
        """Hides soft keyboard if it's currently showing."""
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except Exception:
            pass

    def take_screenshot(self, name_prefix: str = "screenshot") -> str:
        """Captures a screenshot of the current screen."""
        Config.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        filename = f"{name_prefix}_{int(time.time())}.png"
        filepath = Config.SCREENSHOTS_DIR / filename
        try:
            self.driver.save_screenshot(str(filepath))
            logger.info(f"Saved screenshot: {filepath}")
            return str(filepath)
        except Exception as e:
            logger.error(f"Failed to save screenshot: {e}")
            return ""

    def scroll_to_text(self, text: str):
        """Scrolls using Android UiScrollable until text is visible."""
        ui_scrollable = (
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            f'.scrollIntoView(new UiSelector().textContains("{text}").instance(0))'
        )
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_scrollable)
