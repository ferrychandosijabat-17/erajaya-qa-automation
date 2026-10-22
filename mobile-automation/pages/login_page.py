from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import logger


class LoginPage(BasePage):
    """Page Object for Eraspace Mobile App Login Screen."""

    # Locators
    FIELD_USERNAME = (
        AppiumBy.XPATH,
        "//android.widget.EditText[contains(@resource-id, 'edtPhoneNumber') or contains(@resource-id, 'email') or contains(@resource-id, 'username') or contains(@hint, 'email') or contains(@hint, 'handphone')]",
    )
    FIELD_PASSWORD = (
        AppiumBy.XPATH,
        "//android.widget.EditText[contains(@resource-id, 'edtPassword') or contains(@resource-id, 'password') or contains(@hint, 'password') or @password='true']",
    )
    BTN_LOGIN = (
        AppiumBy.XPATH,
        "//android.widget.Button[contains(@resource-id, 'com.eraspace.app.membership:id/btnLogin') or contains(@resource-id, 'btn_login') or @text='Masuk' or @text='Login']",
    )
    TXT_ERROR_MESSAGE = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'tvError') or contains(@resource-id, 'tv_error') or contains(@resource-id, 'snackbar_text') or contains(@resource-id, 'textinput_error') or contains(@text, 'salah') or contains(@text, 'tidak sesuai') or contains(@text, 'gagal') or contains(@text, 'belum terdaftar')]",
    )
    BTN_CLOSE_BANNER = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'btn_close') or @content-desc='Close']",
    )
    TAB_AKUN = (
        AppiumBy.XPATH,
        "//*[@text='Akun' or contains(@content-desc, 'Akun') or contains(@resource-id, 'navigationProfile') or contains(@resource-id, 'navigation_account')]",
    )
    BTN_MASUK_HOMEPAGE = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.eraspace.app.home:id/btnLogin' or @text='Masuk / Daftar' or @text='Masuk']",
    )
    BTN_PERMISSION_ALLOW = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'permission_allow') or @text='Saat aplikasi digunakan' or @text='Izinkan' or @text='Allow']",
    )
    BTN_SKIP_TUTORIAL = (
        AppiumBy.XPATH,
        "//*[contains(@resource-id, 'btnSkip') or @text='Lewati' or @text='Skip']",
    )
    BTN_CLOSE_PLAY_STORE = (
        AppiumBy.XPATH,
        "//*[@package='com.android.vending' and (@content-desc='Close' or @content-desc='Tutup' or contains(@resource-id, 'close'))]",
    )

    def dismiss_initial_popups_if_any(self):
        """Dismiss initial onboarding tutorial, Play Store dialog, or promo banners if displayed."""
        logger.info("Checking for onboarding / promotional popups...")
        play_close = self.find_elements(self.BTN_CLOSE_PLAY_STORE, timeout=1)
        if play_close:
            try:
                play_close[0].click()
                logger.info("Dismissed Play Store popup.")
            except Exception:
                pass

        skip_btn = self.find_elements(self.BTN_SKIP_TUTORIAL, timeout=1)
        if skip_btn:
            try:
                skip_btn[0].click()
                logger.info("Dismissed onboarding tutorial (Lewati).")
            except Exception:
                pass

        perm_btn = self.find_elements(self.BTN_PERMISSION_ALLOW, timeout=1)
        if perm_btn:
            try:
                perm_btn[0].click()
                logger.info("Dismissed system permission popup.")
            except Exception:
                pass

        close_btn = self.find_elements(self.BTN_CLOSE_BANNER, timeout=1)
        if close_btn:
            try:
                close_btn[0].click()
                logger.info("Dismissed initial popup/banner.")
            except Exception:
                pass

    def navigate_to_login_screen(self):
        """Navigate to Login screen from homepage/account tab if needed."""
        self.dismiss_initial_popups_if_any()

        if self.is_displayed(self.FIELD_USERNAME, timeout=2):
            logger.info("Already on Login screen.")
            return

        logger.info("Waiting for main screen / Akun tab...")
        try:
            self.click(self.TAB_AKUN, timeout=15)
            logger.info("Navigated to Akun tab.")
        except Exception as e:
            logger.warning(f"Could not click Akun tab: {e}")

        if self.is_displayed(self.BTN_MASUK_HOMEPAGE, timeout=5):
            logger.info("Clicking Masuk button on Account/Home screen...")
            self.click(self.BTN_MASUK_HOMEPAGE)

        self.find_element(self.FIELD_USERNAME, timeout=15)

    def enter_username(self, username: str) -> str:
        """
        Inputs username/email.
        Step Expected Result: Data berhasil terinput.
        """
        logger.info(f"Step: Input username '{username}'")
        self.send_keys(self.FIELD_USERNAME, username)
        return self.get_entered_username()

    def get_entered_username(self) -> str:
        """Returns the text currently present in the username field."""
        return self.get_text(self.FIELD_USERNAME)

    def enter_password(self, password: str) -> str:
        """
        Inputs password.
        Step Expected Result: Data berhasil terinput.
        """
        logger.info("Step: Input password")
        self.send_keys(self.FIELD_PASSWORD, password)
        return self.get_entered_password()

    def get_entered_password(self) -> str:
        """Returns the text or placeholder confirmation from password field."""
        element = self.find_element(self.FIELD_PASSWORD)
        return element.text or element.get_attribute("text") or "********"

    def click_login(self):
        """
        Clicks the Login / Masuk button.
        """
        logger.info("Step: Klik Login")
        self.click(self.BTN_LOGIN)

    def is_error_message_displayed(self) -> bool:
        """Checks if login error message is displayed (for TC 1.1)."""
        return self.is_displayed(self.TXT_ERROR_MESSAGE, timeout=8)

    def get_error_message(self) -> str:
        """Retrieves the error message text displayed upon failed login."""
        return self.get_text(self.TXT_ERROR_MESSAGE)

    def is_login_failed(self) -> bool:
        """Verifies login failed by checking user is still on login screen or error is shown."""
        return self.is_error_message_displayed() or self.is_displayed(self.BTN_LOGIN, timeout=3)
