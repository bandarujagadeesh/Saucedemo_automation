import pytest

from pages.login import Login
from pages.cartpage import Cartpage
from pages.homepage import Products, Cart

@pytest.mark.usefixtures("driver_")
class TestCart:

    ## TC - Verify that, after click on cart icon on homepage then user navigated to cart page ##
    # @pytest.mark.skip
    def test_click_on_cart_icon_and_verify_home_page_navigated_to_cart_page(self):
        login_obj = Login(self.driver)
        login_obj.login_username().login_password().login_button()
        homepage_cart_obj = Cart(self.driver)
        homepage_cart_obj.cart_icon_is_clickable()
        cartpage_obj = Cartpage(self.driver)
        cartpage_obj.click_on_cart_icon_and_verify_home_page_navigated_to_cart_page()

    def test_click_continue_shopping(self):
        cart_obj = Cartpage(self.driver)
        cart_obj.click_continue_shopping()


    ## TC - Verify that, add an item to cart from home page and check same item will be available on cart page ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_add_item_to_cart_from_home_page_and_check_same_item_is_available_on_cart_page(self):
        add_to_cart_obj = Products(self.driver)
        add_to_cart_obj.click_on_add_to_cart()
        homepage_cart_obj = Cart(self.driver)
        homepage_cart_obj.cart_icon_is_clickable()
        cartpage_obj = Cartpage(self.driver)
        cartpage_obj.add_item_to_cart_from_home_page_and_check_same_item_is_available_on_cart_page()

    ## TC - verify that, item which is added previously from homepage, click on remove button on the cart page for the same then item should not be available ##
    @pytest.mark.dependency(depends=['test_add_item_to_cart_from_home_page_and_check_same_item_is_available_on_cart_page'])
    def test_click_on_remove_button_cart_page_then_item_should_not_be_available(self):
        cartpage_obj = Cartpage(self.driver)
        cartpage_obj.click_on_remove_button_cart_page_then_item_should_not_be_available()

