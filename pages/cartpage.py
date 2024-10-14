from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.reading_excel import homepage_locators_data, cartpage_locators_data, product_names_data
from pages.login import Login

locators_homepage = homepage_locators_data()
locators_cartpage = cartpage_locators_data()
total_products_and_items = product_names_data()

class Cartpage(Login):
    def click_on_cart_icon_and_verify_home_page_navigated_to_cart_page(self):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.visibility_of_element_located(locators_cartpage['text_title_cartpage']))
        return self

    def click_continue_shopping(self):
        self.driver.find_element('id', 'continue-shopping').click()
        return self

    def add_item_to_cart_from_home_page_and_check_same_item_is_available_on_cart_page(self,product_name = total_products_and_items[1][1]):
        wait_obj = WebDriverWait(self.driver, 10)
        item_name = wait_obj.until(EC.visibility_of_element_located(locators_cartpage['text_productname']))
        assert item_name.text.__eq__(product_name)
        return self

    def click_on_remove_button_cart_page_then_item_should_not_be_available(self):
        remove_button = self.driver.find_element(*locators_cartpage['clickable_button_remove'])
        remove_button.click()
        wait_obj = WebDriverWait(self.driver, 10)
        is_invisible = wait_obj.until(EC.invisibility_of_element_located(locators_cartpage['text_productname']))
        assert is_invisible, "The product name is still visible in the cart, but it should not be."
        return self




