import json
import pytest
from pathlib import Path
from config.config import Config
from drivers.driver_factory import DriverFactory
from utils.logger import logger


@pytest.fixture(scope="session")
def test_data():
    """Loads static test data from data/test_data.json."""
    data_path = Config.DATA_DIR / "test_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def driver(request):
    """Initializes Appium driver before test and tears it down after."""
    logger.info(f"=== Starting Test: {request.node.name} ===")
    driver_instance = DriverFactory.create_driver()

    yield driver_instance

    # Capture screenshot if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        Config.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        screenshot_path = (
            Config.SCREENSHOTS_DIR / f"FAILURE_{request.node.name}.png"
        )
        try:
            driver_instance.save_screenshot(str(screenshot_path))
            logger.info(f"Test failed. Saved failure screenshot to: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot on test failure: {e}")

    logger.info(f"=== Tearing down driver & cleaning screenshot for: {request.node.name} ===")
    try:
        driver_instance.terminate_app(Config.APP_PACKAGE)
        logger.info(f"Successfully terminated {Config.APP_PACKAGE} and cleared screen.")
    except Exception as e:
        logger.warning(f"Error terminating app during teardown: {e}")

    try:
        driver_instance.quit()
    except Exception as e:
        logger.warning(f"Error while quitting driver session: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to track test pass/fail state for screenshot capture."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def pytest_html_report_title(report):
    report.title = "Eraspace Mobile Automation Test Report - Erajaya"


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Application"] = "Eraspace Android App"
        config._metadata["Platform"] = Config.PLATFORM_NAME
        config._metadata["Device"] = Config.DEVICE_NAME
        config._metadata["Automation Engine"] = Config.AUTOMATION_NAME
