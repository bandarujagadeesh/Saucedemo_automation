from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.reading_excel import login_locators_data, login_logo, login_error_data, login
from library_.selenium_wrapper import SeleniumWrapper

locators_login = login_locators_data()
error_message = login_error_data()
after_login_title = login()
print(after_login_title[0])
login_page_logo = login_logo()


# selenium_wrapper_obj.click_on_the_element()
# selenium_wrapper_obj.clear_data()
# selenium_wrapper_obj.enter_data()

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.selenium_wrapper_obj = SeleniumWrapper(self.driver)

    def logo(self, logo=login_page_logo[0]):
        logo_ = self.driver.find_element(*locators_login['logo'])
        assert logo_.text == logo, "Logo mismatch"
        return self

    def login_username(self):
        # username = self.driver.find_element(*locators_login['input_username'])
        # username.clear()
        # username.send_keys('standard_user')
        self.selenium_wrapper_obj.clear_data(locators_login['input_username'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_username'],'standard_user')
        return self

    def login_password(self):
        # password = self.driver.find_element(*locators_login['input_password'])
        # password.clear()
        # password.send_keys('secret_sauce')
        self.selenium_wrapper_obj.clear_data(locators_login['input_password'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_password'],'secret_sauce')
        return self

    def login_button(self):
        # self.driver.find_element(*locators_login['button_login']).click()
        self.selenium_wrapper_obj.click_on_the_element(locators_login['button_login'])
        return self

class Loginvalidation(Login):
    def valid_login(self, title_expected=after_login_title[0]):
        wait_obj = WebDriverWait(self.driver,10)
        title = wait_obj.until(EC.visibility_of_element_located(locators_login['text_title']))
         # self.driver.find_element(*locators_login['text_title'])
        assert title.text == title_expected, "Login title mismatch"
        return self



class Invalid_login_username(Login):
    def login_username_invalid(self):
        # username = self.driver.find_element(*locators_login['input_username'])
        # username.clear()
        # username.send_keys('wronguser')
        self.selenium_wrapper_obj.clear_data(locators_login['input_username'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_username'],'wronguser')
        return self

    def login_password_valid(self):
        # password = self.driver.find_element(*locators_login['input_password'])
        # password.clear()
        # password.send_keys('secret_sauce')
        self.selenium_wrapper_obj.clear_data(locators_login['input_password'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_password'],'secret_sauce')
        return self

    def login_button(self):
        # self.driver.find_element(*locators_login['button_login']).click()
        self.selenium_wrapper_obj.click_on_the_element(locators_login['button_login'])
        return self

    def login_error_message(self, message=error_message[0]):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'], message))
        return self


class Invalid_login_password(Login):

    def login_username_valid(self):
        # username = self.driver.find_element(*locators_login['input_username'])
        # username.clear()
        # username.send_keys('standard_user')
        self.selenium_wrapper_obj.clear_data(locators_login['input_username'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_username'],'standard_user')
        return self

    def login_password_invalid(self):
        # password = self.driver.find_element(*locators_login['input_password'])
        # password.clear()
        # password.send_keys('wrongpassword')
        self.selenium_wrapper_obj.clear_data(locators_login['input_password'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_password'],'wrongpassword')
        return self

    def login_button(self):
        # self.driver.find_element(*locators_login['button_login']).click()
        self.selenium_wrapper_obj.click_on_the_element(locators_login['button_login'])
        return self

    def login_error_message(self, message=error_message[0]):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'], message))
        return self


class Invalid_username_password(Login):
    def login_username_invalid(self):
        # username = self.driver.find_element(*locators_login['input_username'])
        # username.clear()
        # username.send_keys('wronguser')
        self.selenium_wrapper_obj.clear_data(locators_login['input_username'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_username'],'wronguser')
        return self

    def login_password_invalid(self):
        # password = self.driver.find_element(*locators_login['input_password'])
        # password.clear()
        # password.send_keys('wrongpassword')
        self.selenium_wrapper_obj.clear_data(locators_login['input_username'])
        self.selenium_wrapper_obj.enter_data(locators_login['input_username'],'wrongpassword')
        return self

    def login_button(self):
        # self.driver.find_element(*locators_login['button_login']).click()
        self.selenium_wrapper_obj.click_on_the_element(locators_login['button_login'])
        return self

    def login_error_message(self, message=error_message[0]):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'], message))
        return self

    def error_message_text(self, message=error_message[0]):
        error_message = self.driver.find_element(*locators_login['text_error_message'])
        assert error_message.text == message, "Error message mismatch"
        return self
