import os
from pathlib import Path
from dotenv import load_dotenv

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Config:
    """Project-wide configuration settings for Mobile Automation."""

    # Appium Server
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    # Virtual Device / Capabilities
    PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
    PLATFORM_VERSION = os.getenv("PLATFORM_VERSION", "13.0")
    DEVICE_NAME = os.getenv("DEVICE_NAME", "Android Emulator")
    UDID = os.getenv("UDID", "emulator-5554")
    AUTOMATION_NAME = os.getenv("AUTOMATION_NAME", "UiAutomator2")

    # Application details for Eraspace
    APP_PACKAGE = os.getenv("APP_PACKAGE", "com.eraspace.app")
    APP_ACTIVITY = os.getenv(
        "APP_ACTIVITY", "com.eraspace.app.presentation.SplashScreenActivity"
    )
    APP_PATH = os.getenv("APP_PATH", "")

    # Execution Options
    NO_RESET = os.getenv("NO_RESET", "false").lower() == "true"
    FULL_RESET = os.getenv("FULL_RESET", "false").lower() == "true"
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "300"))

    # Timeouts
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

    # Paths
    REPORTS_DIR = BASE_DIR / "reports"
    SCREENSHOTS_DIR = BASE_DIR / "screenshots"
    DATA_DIR = BASE_DIR / "data"
