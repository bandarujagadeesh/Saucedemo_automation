import pytest
from pages.homepage import Products,Cart
from pages.login import Login

@pytest.mark.usefixtures("driver_")
class TestProducts:

    ## TC -  Verify the Product names ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_product_names(self):
        login_obj = Login(self.driver)
        login_obj.login_username().login_password().login_button()
        products_obj = Products(self.driver)
        products_obj.product_names()

    ## TC - Verify total product count ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_count_product(self):
        products_obj = Products(self.driver)
        total_no_of_product = products_obj.total_products()

    ## TC - Verify total add to cart buttons ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_count_add_to_cart(self):
        products_obj = Products(self.driver)
        total_no_of_atc = products_obj.total_add_to_cart()

    ## TC - Verify that add to cart is available for all the products
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_add_to_cart_for_each_product(self):
        products_obj = Products(self.driver)
        total_no_of_product = products_obj.total_products()
        total_no_of_atc = products_obj.total_add_to_cart()
        products_obj.add_to_cart_for_all_products()

    ## TC - Verify the add to cart button functionality for the required product ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_add_to_cart_button(self):
        add_to_cart_obj = Products(self.driver)
        add_to_cart_obj.click_on_add_to_cart()

    ## TC - Verify that, button name should be changed to remove after clicking on add to cart ##
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_remove_button_is_available_after_click_on_add_to_cart(self):
        add_to_cart_obj = Products(self.driver)
        add_to_cart_obj.check_remove_button()

    ## TC - Verify that, cart icon is available on homepage
    # @pytest.mark.dependency(depends=['Login::test_login'])
    # @pytest.mark.skip
    def test_cart_icon_is_available(self):
        cart_obj = Cart(self.driver)
        cart_obj.cart_icon_is_available()

    ## TC - Verify that, cart icon on homepage is clickable ##
    def test_cart_icon_is_clickable(self):
        cart_obj = Cart(self.driver)
        cart_obj.cart_icon_is_clickable()
