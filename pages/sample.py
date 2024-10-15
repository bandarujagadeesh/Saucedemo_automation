import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.saucedemo.com/')
handle1 = driver.window_handles
driver.find_element('xpath','//input[@id="user-name"]').send_keys('standard_user')
driver.find_element('xpath','//input[@id="password"]').send_keys('secret_sauce')
driver.find_element('xpath','//input[@id="login-button"]').click()
# wait = WebDriverWait(driver, 10)
# hamburger_button = wait.until(EC.element_to_be_clickable(('id', "react-burger-menu-btn")))
#
# # Click the hamburger menu button
# hamburger_button.click()
#
# # Wait for the menu items to appear (locating the elements under the class 'bm-item')
# menu_items = wait.until(EC.visibility_of_all_elements_located(('class name', "bm-item")))
#
# # Extract and print the text for each menu item
# print([item.text for item in menu_items])
#
# # assert menu_list_splitted == ['All Items', 'About', 'Logout', 'Reset App State']

add_to_carts = driver.find_elements('xpath','//button[text()="Add to cart"]')
wait = WebDriverWait(driver, 10)
inventory_items = wait.until(EC.visibility_of_all_elements_located(('class name','inventory_item_name ')))
inventory_items_list = [item.text for item in inventory_items]
add_to_carts_list = [button.text for button in add_to_carts]
# print(inventory_items_list)
# print(add_to_carts_list)
# handle2 = driver.window_handles
# print(handle1)
# print(handle2)

# for index,value in enumerate(inventory_items_list):
#     if value == 'Sauce Labs Bike Light':
#         print(index)
#         add_to_cart_button = driver.find_element('xpath',f'//div[text()="{value}"]/../../..//button[text()="Add to cart"]')
#         add_to_cart_button.click()
#     else:
#         print('not able to click')
#
# driver.find_element('xpath','//button[text()="Add to cart"]').click()

    # else:
    #     driver.find_element('xpath',f'(//button[text()="Add to cart"])[{index}]').click()
# # except:
#     add_to_cart_button = driver.find_element('xpath',
#                                              '(//button[text()="Add to cart"])[1]')
#     add_to_cart_button.click()

# for i in inventory_items_list:
#     if i.text == 'Sauce Labs Bike Light':
#         add_to_cart.click()
dropdown_element = driver.find_element('class name', 'product_sort_container')

# Use Select class to handle the dropdown
select = Select(dropdown_element)

# Retrieve all options from the dropdown
options = select.options  # This returns a list of all available options

select.select_by_index(2)
# Loop through each option and print its text or interact with it
# for index,option in enumerate(options):
#     # print(option.text)
#     # print(index)
#     # print("Option Text:", option.text)  # Print the visible text of the option
#     # select.select_by_visible_text(option.text)
#     # select.select_by_visible_text(option.text)
#     dropdown_element.click()
#     time.sleep(2)
#     select.select_by_index(index)
