from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import logger


class HomePage(BasePage):
    """Page Object for Eraspace Mobile App Home / Post-Login Screen."""

    # Locators for Homepage and post-login verification
    CONTAINER_HOME = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'bnvMain') or contains(@resource-id, 'container_home') or contains(@resource-id, 'home_fragment') or contains(@resource-id, 'nav_view')]",
    )
    BOTTOM_NAV_ITEMS = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'bnvMain')]//android.widget.TextView | //*[contains(@resource-id, 'navigation_bar_item_small_label_view') or contains(@resource-id, 'navigation_bar_item_large_label_view')]",
    )
    TXT_ACCOUNT_NAME = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'tv_user_name') or contains(@resource-id, 'tv_name') or contains(@resource-id, 'profile_name') or contains(@text, 'Hai,') or contains(@text, 'Halo')]",
    )
    TXT_POINTS = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'tv_point') or contains(@resource-id, 'point_balance') or contains(@resource-id, 'eraspace_point') or contains(@text, 'Poin') or contains(@text, 'Point')]",
    )
    TAB_AKUN = (
        AppiumBy.XPATH,
        "//*[@text='Akun' or contains(@content-desc, 'Akun') or contains(@resource-id, 'navigation_account')]",
    )

    def is_redirected_to_homepage(self, timeout: int = 15) -> bool:
        """
        TC 1.2 Expected Result 2: Redirect ke homepage.
        Verifies that user is redirected to the home screen.
        """
        logger.info("Verifying redirect to homepage...")
        return self.is_displayed(self.CONTAINER_HOME, timeout=timeout) or self.is_displayed(
            self.BOTTOM_NAV_ITEMS, timeout=timeout
        )

    def get_list_menu(self) -> list[str]:
        """
        TC 1.2 Expected Result 3: Menampilkan list menu.
        Retrieves all visible navigation menu items.
        """
        logger.info("Verifying display of menu list...")
        elements = self.find_elements(self.BOTTOM_NAV_ITEMS, timeout=10)
        menu_items = []
        for el in elements:
            text = el.text or el.get_attribute("content-desc") or ""
            if text.strip():
                menu_items.append(text.strip())
        logger.info(f"Detected menu items: {menu_items}")
        return menu_items

    def is_menu_list_displayed(self) -> bool:
        """Verifies at least one or more navigation menus are displayed."""
        menus = self.get_list_menu()
        return len(menus) > 0 or self.is_displayed(self.CONTAINER_HOME)

    def open_account_tab_if_needed(self):
        """Navigate to Account tab to view account name & points if not directly on homepage header."""
        if self.is_displayed(self.TAB_AKUN, timeout=3):
            self.click(self.TAB_AKUN)

    def is_account_name_displayed(self) -> bool:
        """
        TC 1.2 Expected Result 4: Menampilkan nama akun.
        """
        logger.info("Verifying account name displayed...")
        if not self.is_displayed(self.TXT_ACCOUNT_NAME, timeout=5):
            self.open_account_tab_if_needed()
        return self.is_displayed(self.TXT_ACCOUNT_NAME, timeout=8)

    def get_account_name(self) -> str:
        """Retrieves user's account name displayed on screen."""
        if not self.is_displayed(self.TXT_ACCOUNT_NAME, timeout=5):
            self.open_account_tab_if_needed()
        return self.get_text(self.TXT_ACCOUNT_NAME)

    def is_points_displayed(self) -> bool:
        """
        TC 1.2 Expected Result 5: Menampilkan list point.
        """
        logger.info("Verifying points list/balance displayed...")
        if not self.is_displayed(self.TXT_POINTS, timeout=5):
            self.open_account_tab_if_needed()
        return self.is_displayed(self.TXT_POINTS, timeout=8)

    def get_points_info(self) -> str:
        """Retrieves points balance/indicator displayed on screen."""
        if not self.is_displayed(self.TXT_POINTS, timeout=5):
            self.open_account_tab_if_needed()
        return self.get_text(self.TXT_POINTS)
