import time
from appium import webdriver
from config.config import Config
from config.capabilities import get_android_options
from utils.logger import logger


class DriverFactory:
    """Manages creation and lifecycle of Appium WebDriver instances for Virtual / Physical devices."""

    @staticmethod
    def create_driver():
        logger.info(
            f"Connecting to Appium server at: {Config.APPIUM_SERVER_URL} for device: {Config.DEVICE_NAME}"
        )
        options = get_android_options()
        try:
            driver = webdriver.Remote(
                command_executor=Config.APPIUM_SERVER_URL,
                options=options,
            )
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            logger.info("Appium driver session initialized successfully. Waiting for splash screen...")
            time.sleep(4)
            return driver
        except Exception as e:
            logger.error(f"Failed to initialize Appium driver session: {e}")
            raise e
