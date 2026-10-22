from appium.options.android import UiAutomator2Options
from config.config import Config


def get_android_options() -> UiAutomator2Options:
    """
    Constructs and returns UiAutomator2Options tailored for Android Virtual Devices (AVD, Genymotion, BlueStacks).
    """
    options = UiAutomator2Options()
    options.platform_name = Config.PLATFORM_NAME
    options.automation_name = Config.AUTOMATION_NAME
    options.device_name = Config.DEVICE_NAME

    if Config.UDID:
        options.udid = Config.UDID

    # If APK file is provided, install/launch from file; otherwise launch by package & activity
    if Config.APP_PATH:
        options.app = Config.APP_PATH
    else:
        options.app_package = Config.APP_PACKAGE
        options.app_activity = Config.APP_ACTIVITY

    options.no_reset = Config.NO_RESET
    options.full_reset = Config.FULL_RESET
    options.new_command_timeout = Config.COMMAND_TIMEOUT

    # Additional options for virtual devices
    options.set_capability("autoGrantPermissions", True)
    options.set_capability("ensureWebviewsHavePages", True)
    options.set_capability("nativeWebScreenshot", True)
    options.set_capability("connectHardwareKeyboard", True)
    options.set_capability("enforceXPath1", True)
    options.set_capability("appWaitActivity", "*")
    options.set_capability("appWaitDuration", 20000)

    return options
