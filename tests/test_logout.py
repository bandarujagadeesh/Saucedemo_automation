import pytest
from pages.homepage import Logout
from pages.login import Login

@pytest.mark.usefixtures("driver_")
class Testlogout:
    ## TC - Verify the logout button ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    def test_logout(self):
        login_obj = Login(self.driver)
        login_obj.login_username().login_password().login_button()
        logout_obj = Logout(self.driver)
        logout_obj.click_hamburger_button().click_logout_link()

    # @pytest.mark.dependency(depends=['test_logout'])
    ## TC - Verify that, after logout user got navigated back to login page ##
    def test_logout_navigation_to_login(self):
        logout_obj = Logout(self.driver)
        logout_obj.logo_text()
