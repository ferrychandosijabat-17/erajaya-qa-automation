import pytest

class TestCuraLogin:
    """
    Scenario 1: Login Functionality on CURA Healthcare Service
    Target URL: https://katalon-demo-cura.herokuapp.com/
    """

    @pytest.mark.regression
    def test_tc_1_1_login_with_invalid_data(self, login_page, test_data):
        """
        TC ID: 1.1
        Test Case Description: Login with invalid data
        """
        user = test_data["invalid_user"]

        # Step 1: Input invalid username
        login_page.input_username(user["username"])
        # Expected 1: Data berhasil terinput
        actual_username = login_page.get_username_input_value()
        assert actual_username == user["username"], (
            f"Expected username '{user['username']}', but got '{actual_username}'"
        )

        # Step 2: Input invalid password
        login_page.input_password(user["password"])
        # Expected 2: Data berhasil terinput
        actual_password = login_page.get_password_input_value()
        assert actual_password == user["password"], (
            "Password data was not entered correctly into input field"
        )

        # Step 3: Klik Login
        login_page.click_login()
        # Expected 3: Login gagal dan Tampil pesan error
        assert login_page.is_error_displayed(), (
            "Expected error message alert to be displayed after invalid login"
        )
        assert user["expected_error"] in login_page.get_error_message(), (
            f"Expected error message containing '{user['expected_error']}', "
            f"but got '{login_page.get_error_message()}'"
        )

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_tc_1_2_login_with_valid_data(self, login_page, appointment_page, test_data):
        """
        TC ID: 1.2
        Test Case Description: Login with valid data
        """
        user = test_data["valid_user"]

        # Step 1: Input valid username
        login_page.input_username(user["username"])
        # Expected 1: Data berhasil terinput
        actual_username = login_page.get_username_input_value()
        assert actual_username == user["username"], (
            f"Expected username '{user['username']}', but got '{actual_username}'"
        )

        # Step 2: Input valid password
        login_page.input_password(user["password"])
        # Expected 2: Data berhasil terinput
        actual_password = login_page.get_password_input_value()
        assert actual_password == user["password"], (
            "Valid password was not entered correctly into input field"
        )

        # Step 3: Klik Login
        login_page.click_login()
        # Expected 3: Login sukses dan Redirect ke homepage (Make Appointment)
        assert appointment_page.is_appointment_page_displayed(), (
            "Expected successful redirection to the Appointment page (#appointment)"
        )
        assert "Make Appointment" in appointment_page.get_header_text(), (
            f"Expected page header 'Make Appointment', but got '{appointment_page.get_header_text()}'"
        )
