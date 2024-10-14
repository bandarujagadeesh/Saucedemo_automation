import pytest
from pages.homepage import Hamburger
from pages.login import Login
@pytest.mark.usefixtures("driver_")
class TestHamburger:

    ## TC -  Verify that user able to see the hamburger button is available or not after login ##
    def test_hamburger_button(self):
        login_obj = Login(self.driver)
        login_obj.login_username().login_password().login_button()
        hamburger = Hamburger(self.driver)
        hamburger.hamburger_button_option()

    ## TC - Verify that user able to click the hamburger button ##
    def test_hamburger_functionality(self):
        hamburger_obj = Hamburger(self.driver)
        hamburger_obj.click_hamburger_button()

    ## TC - Verify the, hamburger menu items ##
    # @pytest.mark.dependency(depends=['test_hamburger_functionality'])
    def test_hamburger_items(self):
        hamburger_obj = Hamburger(self.driver)
        hamburger_obj.click_hamburger_button().items_in_hamburger()

    def test_hamburger_menu_close_option(self):
        hamburger_obj = Hamburger(self.driver)
        hamburger_obj.click_close_hamburger_menu()


