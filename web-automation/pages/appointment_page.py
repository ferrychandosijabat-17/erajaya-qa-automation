from playwright.sync_api import Page
from pages.base_page import BasePage

class AppointmentPage(BasePage):
    """
    Page Object for CURA Healthcare Appointment (Homepage after login).
    Handles form inputs, date picker, validations, and submission.
    """
    HEADER = "h2"
    APPOINTMENT_SECTION = "#appointment"
    FACILITY_DROPDOWN = "#combo_facility"
    READMISSION_CHECKBOX = "#chk_hospotal_readmission"
    PROGRAM_MEDICARE = "#radio_program_medicare"
    PROGRAM_MEDICAID = "#radio_program_medicaid"
    PROGRAM_NONE = "#radio_program_none"
    VISIT_DATE_INPUT = "#txt_visit_date"
    DATEPICKER_ACTIVE_DAYS = ".datepicker-days td.day:not(.old):not(.new)"
    COMMENT_INPUT = "#txt_comment"
    BOOK_APPOINTMENT_BTN = "#btn-book-appointment"

    def __init__(self, page: Page):
        super().__init__(page)

    def is_appointment_page_displayed(self, timeout: int = 10000) -> bool:
        """Verify that the user is on the Make Appointment page."""
        try:
            self.wait_for_selector(self.APPOINTMENT_SECTION, timeout=timeout)
            return self.is_visible(self.APPOINTMENT_SECTION)
        except Exception:
            return False

    def get_header_text(self) -> str:
        """Get the main heading text of the page."""
        return self.get_text(self.HEADER)

    def select_facility(self, facility_name: str):
        """Select a healthcare facility from the dropdown."""
        self.page.select_option(self.FACILITY_DROPDOWN, facility_name)

    def get_selected_facility(self) -> str:
        """Get the currently selected facility name."""
        return self.page.eval_on_selector(
            self.FACILITY_DROPDOWN, 
            "sel => sel.options[sel.selectedIndex].text"
        )

    def set_hospital_readmission(self, enable: bool):
        """Check or uncheck the hospital readmission checkbox."""
        self.close_datepicker()
        self.page.set_checked(self.READMISSION_CHECKBOX, enable)

    def is_hospital_readmission_checked(self) -> bool:
        """Check if the hospital readmission checkbox is checked."""
        return self.page.is_checked(self.READMISSION_CHECKBOX)

    def select_program(self, program_name: str):
        """Select a healthcare program radio button (Medicare, Medicaid, None)."""
        self.close_datepicker()
        program_lower = program_name.lower()
        if "medicaid" in program_lower:
            self.page.set_checked(self.PROGRAM_MEDICAID, True)
        elif "none" in program_lower:
            self.page.set_checked(self.PROGRAM_NONE, True)
        else:
            self.page.set_checked(self.PROGRAM_MEDICARE, True)

    def get_selected_program(self) -> str:
        """Get the currently selected program value."""
        if self.page.is_checked(self.PROGRAM_MEDICAID):
            return "Medicaid"
        elif self.page.is_checked(self.PROGRAM_NONE):
            return "None"
        return "Medicare"

    def close_datepicker(self):
        """Ensure Bootstrap datepicker popup overlay is dismissed so it doesn't block other elements."""
        self.page.evaluate("() => document.querySelectorAll('.datepicker').forEach(e => e.style.display = 'none')")

    def clear_visit_date(self):
        """Clear the visit date input field and dismiss the datepicker popup."""
        self.page.fill(self.VISIT_DATE_INPUT, "")
        self.page.dispatch_event(self.VISIT_DATE_INPUT, "change")
        self.close_datepicker()

    def get_visit_date_value(self) -> str:
        """Get the current value of the visit date input."""
        return self.get_input_value(self.VISIT_DATE_INPUT)

    def select_date_from_picker(self) -> str:
        """Open the datepicker widget and select an available day."""
        self.page.click(self.VISIT_DATE_INPUT)
        self.page.wait_for_selector(self.DATEPICKER_ACTIVE_DAYS, timeout=3000)
        self.page.locator(self.DATEPICKER_ACTIVE_DAYS).first.click()
        self.close_datepicker()
        return self.get_visit_date_value()

    def set_visit_date(self, date_str: str):
        """Directly type date and dismiss the datepicker."""
        self.page.fill(self.VISIT_DATE_INPUT, date_str)
        self.page.dispatch_event(self.VISIT_DATE_INPUT, "change")
        self.close_datepicker()

    def fill_comment(self, comment: str):
        """Type comment into the comment textarea."""
        self.fill(self.COMMENT_INPUT, comment)

    def get_comment_value(self) -> str:
        """Get the current text in the comment textarea."""
        return self.get_input_value(self.COMMENT_INPUT)

    def click_book_appointment(self):
        """Click the Book Appointment button."""
        self.page.click(self.BOOK_APPOINTMENT_BTN, no_wait_after=True)

    def get_visit_date_validation_message(self) -> str:
        """Retrieve the HTML5 browser validation message for the mandatory visit date."""
        return self.page.eval_on_selector(
            self.VISIT_DATE_INPUT, 
            "el => el.validationMessage"
        )

    def is_visit_date_invalid(self) -> bool:
        """Check if the visit date field is currently evaluated as invalid by the browser."""
        return self.page.eval_on_selector(
            self.VISIT_DATE_INPUT, 
            "el => el.matches(':invalid')"
        )
