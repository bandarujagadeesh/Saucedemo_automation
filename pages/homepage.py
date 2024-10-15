from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.reading_excel import logout_locators_data, homepage_locators_data, logout_navigate_data, product_names_data
from pages.login import Login
from library_.selenium_wrapper import SeleniumWrapper

locators_logout = logout_locators_data()
locators_homepage = homepage_locators_data()
total_products_and_items = product_names_data()
logo_name = logout_navigate_data()
# print(total_products_and_items[1][1])

class Logout(Login):
    def __init__(self, driver):
        super().__init__(driver)
        self.selenium_wrapper_obj = SeleniumWrapper(self.driver)

    def click_hamburger_button(self):
        # self.driver.find_element(*locators_logout['button_hamburger']).click()
        self.selenium_wrapper_obj.click_on_the_element(locators_logout['button_hamburger'])
        return self

    def click_logout_link(self):
        wait_obj = WebDriverWait(self.driver,10)
        logout = wait_obj.until(EC.element_to_be_clickable(locators_logout['link_logout']))
        logout.click()
        return self

    def logo_text(self,logo = logo_name[0]):
        ref_ele = self.driver.find_element(*locators_logout['text_logo'])
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.visibility_of_element_located(locators_logout['text_logo']))
        assert ref_ele.text.__eq__(logo), "both actual result an expected result are not same"
        return self


class Hamburger(Login):
    def __init__(self, driver):
        super().__init__(driver)

    def hamburger_button_option(self):
        wait_obj = WebDriverWait(self.driver,timeout=10)
        wait_obj.until(EC.visibility_of_element_located(locators_homepage['button_hamburger']))
        return self

    def click_hamburger_button(self):
        wait_obj = WebDriverWait(self.driver, 10)
        hamburger_button = wait_obj.until(EC.element_to_be_clickable(locators_homepage['button_hamburger']))
        hamburger_button.click()
        return self

    def click_close_hamburger_menu(self):
        self.driver.find_element('xpath','//button[@id="react-burger-cross-btn"]').click()
        return self

    def items_in_hamburger(self):
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 20)
        hamburger_button = wait.until(EC.element_to_be_clickable(locators_homepage['button_hamburger']))
        hamburger_button.click()
        menu_items = wait.until(EC.visibility_of_all_elements_located(locators_homepage['text_hamburger_items']))
        menu_items_list = [item.text for item in menu_items]
        assert menu_items_list.__eq__(['All Items', 'About', 'Logout', 'Reset App State'])
        return self

class Products(Login):
    def __init__(self,driver):
        super().__init__(driver)

    def product_names(self,products = total_products_and_items[1]):
        wait = WebDriverWait(self.driver, 10)
        inventory_items = wait.until(EC.visibility_of_all_elements_located(locators_homepage['text_product_items']))
        inventory_items_list = [item.text for item in inventory_items]
        assert inventory_items_list.__eq__(products), "The name of product-items doesn't match."
        # ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
        return self

    def total_products(self,total = total_products_and_items[0]):
        wait = WebDriverWait(self.driver, 10)
        inventory_items = wait.until(EC.visibility_of_all_elements_located(locators_homepage['text_product_items']))
        inventory_items_list = [item.text for item in inventory_items]
        self.total_no_of_product = len(inventory_items_list)
        assert self.total_no_of_product.__eq__(total),  "The number of product-items doesn't match."
        return self

    def total_add_to_cart(self,total = total_products_and_items[0]):
        add_to_carts = self.driver.find_elements('xpath', '//button[text()="Add to cart"]')
        add_to_carts_list = [button.text for button in add_to_carts]
        self.total_no_of_atc = len(add_to_carts_list)
        assert self.total_no_of_atc.__eq__(total), "The number of add to cart button doesn't match."
        return self

    def add_to_cart_for_all_products(self):
        assert self.total_no_of_product.__eq__(self.total_no_of_atc), f"Mismatch: Total Products ({self.total_products}) != Total Add to Cart Buttons ({self.total_atc})"
        return self

    def click_on_add_to_cart(self):
        for index,value in enumerate(total_products_and_items[1]):
            if value == 'Sauce Labs Bike Light':
                print(index)
                add_to_cart_button = self.driver.find_element('xpath',f'//div[text()="{value}"]/../../..//button[text()="Add to cart"]')
                add_to_cart_button.click()
        return self

    def check_remove_button(self):
        add_to_cart_button = self.driver.find_element(*locators_homepage['button_add_to_cart'])
        add_to_cart_button.click()
        wait_obj = WebDriverWait(self.driver,10)
        wait_obj.until(EC.visibility_of_element_located(locators_homepage['button_remove']))
        return self


class Cart(Login):
    def cart_icon_is_available(self):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.visibility_of_element_located(locators_homepage['clickable_cart_icon']))
        return self

    def cart_icon_is_clickable(self):
        wait_obj = WebDriverWait(self.driver, 10)
        add_to_cart_icon = wait_obj.until(EC.element_to_be_clickable(locators_homepage['clickable_cart_icon']))
        add_to_cart_icon.click()
        return self







