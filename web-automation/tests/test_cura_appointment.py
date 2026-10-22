import pytest

class TestCuraAppointment:
    """
    Scenario 2: Make Appointment on CURA Healthcare Service
    Target URL: https://katalon-demo-cura.herokuapp.com/#appointment
    """

    @pytest.mark.regression
    def test_tc_2_1_make_appointment_without_mandatory_field(
        self, login_page, appointment_page, test_data
    ):
        """
        TC ID: 2.1
        Test Case Description: Make Appointment - without input mandatory field (visit date)
        """
        # Step 1: Call TC 1.2 (Perform valid login to reach Make Appointment)
        valid_user = test_data["valid_user"]
        login_page.input_username(valid_user["username"])
        login_page.input_password(valid_user["password"])
        login_page.click_login()
        assert appointment_page.is_appointment_page_displayed(), (
            "Precondition failed: Expected redirection to Make Appointment homepage"
        )

        appt_data = test_data["appointment_data"]

        # Step 2: Kosongkan tanggal
        appointment_page.clear_visit_date()
        # Expected 2: Tanggal kosong
        actual_date = appointment_page.get_visit_date_value()
        assert actual_date == "", f"Expected visit date to be empty, but got '{actual_date}'"

        # Step 3: Input data (kecuali tanggal)
        appointment_page.select_facility(appt_data["facility"])
        appointment_page.set_hospital_readmission(appt_data["hospital_readmission"])
        appointment_page.select_program(appt_data["program"])
        appointment_page.fill_comment(appt_data["comment"])

        # Expected 3: Data berhasil terinput
        assert appointment_page.get_selected_facility() == appt_data["facility"], (
            f"Expected facility '{appt_data['facility']}', but got '{appointment_page.get_selected_facility()}'"
        )
        assert appointment_page.is_hospital_readmission_checked() == appt_data["hospital_readmission"], (
            "Readmission checkbox state did not match expected value"
        )
        assert appointment_page.get_selected_program() == appt_data["program"], (
            f"Expected program '{appt_data['program']}', but got '{appointment_page.get_selected_program()}'"
        )
        assert appointment_page.get_comment_value() == appt_data["comment"], (
            f"Expected comment '{appt_data['comment']}', but got '{appointment_page.get_comment_value()}'"
        )

        # Step 4: Klik Make Appointment
        appointment_page.click_book_appointment()

        # Expected 4: Menampilkan error message, mandatory field harus diisi
        assert appointment_page.is_visit_date_invalid(), (
            "Expected visit date field to be flagged as invalid (mandatory field)"
        )
        validation_message = appointment_page.get_visit_date_validation_message()
        assert len(validation_message) > 0, (
            "Expected browser validation message to appear for mandatory field"
        )
        assert appointment_page.is_appointment_page_displayed(), (
            "Expected form submission to be blocked and user to remain on Make Appointment page"
        )

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_tc_2_2_make_appointment_success(
        self, login_page, appointment_page, summary_page, test_data
    ):
        """
        TC ID: 2.2
        Test Case Description: Make Appointment - Success
        """
        # Precondition: Login with valid data (Call TC 1.2)
        valid_user = test_data["valid_user"]
        login_page.input_username(valid_user["username"])
        login_page.input_password(valid_user["password"])
        login_page.click_login()
        assert appointment_page.is_appointment_page_displayed(), (
            "Precondition failed: Expected redirection to Make Appointment homepage"
        )

        appt_data = test_data["appointment_data"]

        # Step 1: Input semua data
        appointment_page.select_facility(appt_data["facility"])
        appointment_page.set_hospital_readmission(appt_data["hospital_readmission"])
        appointment_page.select_program(appt_data["program"])
        selected_date = appointment_page.select_date_from_picker()
        appointment_page.fill_comment(appt_data["comment"])

        # Expected 1: Data berhasil terinput
        assert appointment_page.get_selected_facility() == appt_data["facility"], (
            "Facility data was not set properly"
        )
        assert appointment_page.is_hospital_readmission_checked() == appt_data["hospital_readmission"], (
            "Readmission checkbox was not checked"
        )
        assert appointment_page.get_selected_program() == appt_data["program"], (
            "Healthcare program radio was not selected properly"
        )
        assert appointment_page.get_visit_date_value() == selected_date, (
            "Visit date was not entered properly"
        )
        assert appointment_page.get_comment_value() == appt_data["comment"], (
            "Comment was not entered properly"
        )

        # Step 2: Klik Make Appointment
        appointment_page.click_book_appointment()

        # Expected 2: Berhasil membuat appointment dan Menampilkan data appointment yang sudah diinput sebelumnya
        assert summary_page.is_summary_page_displayed(), (
            "Expected redirection to Appointment Confirmation summary page"
        )
        assert "Appointment Confirmation" in summary_page.get_header_text(), (
            f"Expected header 'Appointment Confirmation', got '{summary_page.get_header_text()}'"
        )

        # Verify summary data matches what was input
        assert summary_page.get_facility() == appt_data["facility"], (
            f"Expected summary facility '{appt_data['facility']}', got '{summary_page.get_facility()}'"
        )
        expected_readmission = "Yes" if appt_data["hospital_readmission"] else "No"
        assert summary_page.get_readmission() == expected_readmission, (
            f"Expected summary readmission '{expected_readmission}', got '{summary_page.get_readmission()}'"
        )
        assert summary_page.get_program() == appt_data["program"], (
            f"Expected summary program '{appt_data['program']}', got '{summary_page.get_program()}'"
        )
        assert summary_page.get_visit_date() == selected_date, (
            f"Expected summary visit date '{selected_date}', got '{summary_page.get_visit_date()}'"
        )
        assert summary_page.get_comment() == appt_data["comment"], (
            f"Expected summary comment '{appt_data['comment']}', got '{summary_page.get_comment()}'"
        )
