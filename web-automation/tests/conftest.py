import json
import pytest
from pathlib import Path
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from pages.summary_page import SummaryPage

@pytest.fixture(scope="session")
def test_data():
    """Load test data from JSON file."""
    data_file = Path(__file__).parent.parent / "data" / "test_data.json"
    with open(data_file, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def login_page(page):
    """Fixture that initializes LoginPage and opens the CURA login page."""
    login_pg = LoginPage(page)
    login_pg.open()
    return login_pg

@pytest.fixture
def appointment_page(page):
    """Fixture that initializes the AppointmentPage."""
    return AppointmentPage(page)

@pytest.fixture
def summary_page(page):
    """Fixture that initializes the SummaryPage."""
    return SummaryPage(page)

def pytest_html_report_title(report):
    """Set custom title for the HTML test report."""
    report.title = "CURA Healthcare - Automation Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot to the pytest-html report when a test fails."""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                import base64
                import pytest_html.extras as html_extras
                screenshot_bytes = page.screenshot()
                encoded = base64.b64encode(screenshot_bytes).decode("ascii")
                extras.append(html_extras.png(encoded))
            except Exception:
                pass
        report.extras = extras
