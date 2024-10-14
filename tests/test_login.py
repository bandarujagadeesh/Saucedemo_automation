import pytest
from pages.login import Login, Invalid_login_username, Invalid_login_password, Invalid_username_password, Loginvalidation

@pytest.mark.usefixtures("driver_")
class TestLogin:
    ## TC - Verify the, logo text in login page ##
    def test_logo(self):
        logo_obj = Login(self.driver)
        logo_obj.logo()

    ## TC - Verify with invalid credentials and check the error message (invalid username and valid password) ##
    def test_invalid_login_username(self):
        invalid_login_obj = Invalid_login_username(self.driver)
        invalid_login_obj.login_username_invalid().login_password_valid().login_button().login_error_message()

    ## TC - Verify with invalid credentials and check the error message (valid username and invalid password) ##
    def test_invalid_login_password(self):
        invalid_login_obj = Invalid_login_password(self.driver)
        invalid_login_obj.login_username_valid().login_password_invalid().login_button().login_error_message()

    ## TC - Verify with invalid credentials and check the error message (invalid username and invalid password) ##
    def test_both_invalid(self):
        invalid_login_obj = Invalid_username_password(self.driver)
        invalid_login_obj.login_username_invalid().login_password_invalid().login_button().login_error_message()

    ## TC - Verify the login error message text if user enters invalid login details ##
    def test_login_message_error_text(self):
        invalid_login_obj = Invalid_username_password(self.driver)
        invalid_login_obj.login_username_invalid().login_password_invalid().login_button().login_error_message().error_message_text()

    ## TC - Verify login button with valid credentials ##
    @pytest.mark.dependency()
    def test_login(self):
        login_obj = Login(self.driver)
        login_obj.login_username().login_password().login_button()

    ## TC - Verify the Login validation ##
    @pytest.mark.dependency(depends=['test_login'])
    def test_login_validation(self):
        validation_login_obj = Loginvalidation(self.driver)
        validation_login_obj.valid_login()


