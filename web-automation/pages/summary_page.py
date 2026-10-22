from playwright.sync_api import Page
from pages.base_page import BasePage

class SummaryPage(BasePage):
    """
    Page Object for Appointment Confirmation / Summary Page.
    Displayed after successfully booking an appointment.
    """
    SUMMARY_SECTION = "#summary"
    HEADER = "#summary h2"
    FACILITY_VALUE = "#facility"
    READMISSION_VALUE = "#hospital_readmission"
    PROGRAM_VALUE = "#program"
    VISIT_DATE_VALUE = "#visit_date"
    COMMENT_VALUE = "#comment"
    GO_TO_HOMEPAGE_BTN = "a.btn:has-text('Go to Homepage')"

    def __init__(self, page: Page):
        super().__init__(page)

    def is_summary_page_displayed(self, timeout: int = 10000) -> bool:
        """Verify that the Appointment Confirmation page is displayed."""
        try:
            self.wait_for_selector(self.SUMMARY_SECTION, timeout=timeout)
            return self.is_visible(self.SUMMARY_SECTION)
        except Exception:
            return False

    def get_header_text(self) -> str:
        """Retrieve confirmation header text (e.g. 'Appointment Confirmation')."""
        return self.get_text(self.HEADER)

    def get_facility(self) -> str:
        """Get the booked facility name."""
        return self.get_text(self.FACILITY_VALUE)

    def get_readmission(self) -> str:
        """Get the booked readmission value ('Yes' or 'No')."""
        return self.get_text(self.READMISSION_VALUE)

    def get_program(self) -> str:
        """Get the booked healthcare program."""
        return self.get_text(self.PROGRAM_VALUE)

    def get_visit_date(self) -> str:
        """Get the booked visit date."""
        return self.get_text(self.VISIT_DATE_VALUE)

    def get_comment(self) -> str:
        """Get the booked comment."""
        return self.get_text(self.COMMENT_VALUE)

    def click_go_to_homepage(self):
        """Click the Go to Homepage button."""
        self.click(self.GO_TO_HOMEPAGE_BTN)
