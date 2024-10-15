class SeleniumWrapper:
    def __init__(self,driver):
        self.driver = driver
    def click_on_the_element(self,locators_login):
        self.driver.find_element(*locators_login).click()

    def clear_data(self,locators_login):
        self.driver.find_element(*locators_login).clear()

    def enter_data(self,locators_login,data):
        self.driver.find_element(*locators_login).send_keys(data)

    def click_on_the_element(self,locators_logout):
        self.driver.find_element(*locators_logout).click()
