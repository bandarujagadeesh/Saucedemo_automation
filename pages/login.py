# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from data.reading_excel import login_locators_data, login_logo, login_error_data, login
#
# locators_login = login_locators_data()
# error_message = login_error_data()
# after_login_title = login()
# login_page_logo = login_logo()
# # print(login_page_logo[0])
#
# class Login:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def login_username(self):
#         self.driver.find_element(*locators_login['input_username']).send_keys('standard_user')
#         return self
#
#     def login_password(self):
#         self.driver.find_element(*locators_login['input_password']).send_keys('secret_sauce')
#         return self
#
#     def login_button(self):
#         self.driver.find_element(*locators_login['button_login']).click()
#         return self
#
#     def valid_login(self,title_expected = after_login_title[0]):
#         title = self.driver.find_element(*locators_login['text_title'])
#         assert title.text.__eq__(title_expected), "after login title is not matched as expected"
#         return self
#
#     def logo(self,logo = login_page_logo[0]):
#         logo_ = self.driver.find_element(*locators_login['logo'])
#         assert logo_.text.__eq__(logo)
#
#
# class Invalid_login_password:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login_username_valid(self):
#         self.driver.find_element(*locators_login['input_username']).send_keys('standard_user')
#         return self
#
#     def login_password_invalid(self):
#         self.driver.find_element(*locators_login['input_password']).send_keys('wrongpassword')
#         return self
#
#     def login_button(self):
#         self.driver.find_element(*locators_login['button_login']).click()
#         return self
#
#     def login_error_message(self,message = error_message[0]):
#         wait_obj = WebDriverWait(self.driver,10)
#         wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'],message))
#         return self
#
#
# class Invalid_login_username:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login_username_invalid(self):
#         self.driver.find_element(*locators_login['input_username']).send_keys('wronguser')
#         return self
#
#     def login_password_valid(self):
#         self.driver.find_element(*locators_login['input_password']).send_keys('secret_sauce')
#         return self
#
#     def login_button(self):
#         self.driver.find_element(*locators_login['button_login']).click()
#         return self
#
#     def login_error_message(self,message = error_message[0]):
#         wait_obj = WebDriverWait(self.driver,10)
#         wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'],message))
#         return self
#
#
# class Invalid_username_password:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login_username_invalid(self):
#         self.driver.find_element(*locators_login['input_username']).send_keys('wronguser')
#         return self
#
#     def login_password_invalid(self):
#         self.driver.find_element(*locators_login['input_password']).send_keys('wrongpassword')
#         return self
#
#     def login_button(self):
#         self.driver.find_element(*locators_login['button_login']).click()
#         return self
#
#     def login_error_message(self,message = error_message[0]):
#         wait_obj = WebDriverWait(self.driver,10)
#         wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'],message))
#         return self
#
#     def error_message_text(self,message = error_message[0]):
#         error_message = self.driver.find_element(*locators_login['text_error_message'])
#         assert error_message.text.__eq__(message)
#         return self
#
#
#
#


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.reading_excel import login_locators_data, login_logo, login_error_data, login

locators_login = login_locators_data()
error_message = login_error_data()
after_login_title = login()
print(after_login_title[0])
login_page_logo = login_logo()

class Login:
    def __init__(self, driver):
        self.driver = driver

    def logo(self, logo=login_page_logo[0]):
        logo_ = self.driver.find_element(*locators_login['logo'])
        assert logo_.text == logo, "Logo mismatch"
        return self

    def login_username(self):
        username = self.driver.find_element(*locators_login['input_username'])
        username.clear()
        username.send_keys('standard_user')
        return self

    def login_password(self):
        password = self.driver.find_element(*locators_login['input_password'])
        password.clear()
        password.send_keys('secret_sauce')
        return self

    def login_button(self):
        self.driver.find_element(*locators_login['button_login']).click()
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
        username = self.driver.find_element(*locators_login['input_username'])
        username.clear()
        username.send_keys('wronguser')
        return self

    def login_password_valid(self):
        password = self.driver.find_element(*locators_login['input_password'])
        password.clear()
        password.send_keys('secret_sauce')
        return self

    def login_button(self):
        self.driver.find_element(*locators_login['button_login']).click()
        return self

    def login_error_message(self, message=error_message[0]):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'], message))
        return self


class Invalid_login_password(Login):

    def login_username_valid(self):
        username = self.driver.find_element(*locators_login['input_username'])
        username.clear()
        username.send_keys('standard_user')
        return self

    def login_password_invalid(self):
        password = self.driver.find_element(*locators_login['input_password'])
        password.clear()
        password.send_keys('wrongpassword')
        return self

    def login_button(self):
        self.driver.find_element(*locators_login['button_login']).click()
        return self

    def login_error_message(self, message=error_message[0]):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'], message))
        return self


class Invalid_username_password(Login):
    def login_username_invalid(self):
        username = self.driver.find_element(*locators_login['input_username'])
        username.clear()
        username.send_keys('wronguser')
        return self

    def login_password_invalid(self):
        password = self.driver.find_element(*locators_login['input_password'])
        password.clear()
        password.send_keys('wrongpassword')
        return self

    def login_button(self):
        self.driver.find_element(*locators_login['button_login']).click()
        return self

    def login_error_message(self, message=error_message[0]):
        wait_obj = WebDriverWait(self.driver, 10)
        wait_obj.until(EC.text_to_be_present_in_element(locators_login['text_error_message'], message))
        return self

    def error_message_text(self, message=error_message[0]):
        error_message = self.driver.find_element(*locators_login['text_error_message'])
        assert error_message.text == message, "Error message mismatch"
        return self
