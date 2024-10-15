import time
import pytest
from selenium import webdriver

@pytest.fixture(autouse=True, scope ='class',params=['chrome'])
def driver_(request):
    parameter = request.param
    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    time.sleep(2)
    # Attach the driver to the test class
    request.cls.driver = driver
    yield driver
    # Teardown: Quit the driver
    driver.quit()


