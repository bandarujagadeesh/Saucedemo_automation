import pandas as pd
path_sausedemo_locatorsdata = r'C:\Users\Jagadeesh Bandaru\PycharmProjects\saucedemo_automation\file\sausedemo_locatorsdata.xlsx'
path_sausedemo_data = r'C:\Users\Jagadeesh Bandaru\PycharmProjects\saucedemo_automation\file\sausedemo_data.xlsx'
def login_locators_data():
    df = pd.read_excel(path_sausedemo_locatorsdata,sheet_name='login_locators')
    logical_name_list = df['logical_name'].tolist()
    locator_name_list = df['locator_name'].tolist()
    locator_value_list = df['locator_value'].tolist()
    loc_name_value_list = list(zip(locator_name_list,locator_value_list))
    login_dict = dict(zip(logical_name_list,loc_name_value_list))
    return login_dict
def logout_locators_data():
    df = pd.read_excel(path_sausedemo_locatorsdata,sheet_name='logout_locators')
    logical_name_list = df['logical_name'].tolist()
    locator_name_list = df['locator_name'].tolist()
    locator_value_list = df['locator_value'].tolist()
    loc_name_value_list = list(zip(locator_name_list,locator_value_list))
    logout_dict = dict(zip(logical_name_list,loc_name_value_list))
    return logout_dict
def homepage_locators_data():
    df = pd.read_excel(path_sausedemo_locatorsdata,sheet_name='homepage_locators')
    logical_name_list = df['logical_name'].tolist()
    locator_name_list = df['locator_name'].tolist()
    locator_value_list = df['locator_value'].tolist()
    loc_name_value_list = list(zip(locator_name_list,locator_value_list))
    homepage_dict = dict(zip(logical_name_list,loc_name_value_list))
    return homepage_dict
def cartpage_locators_data():
    df = pd.read_excel(path_sausedemo_locatorsdata,sheet_name='cartpage_locators')
    logical_name_list = df['logical_name'].tolist()
    locator_name_list = df['locator_name'].tolist()
    locator_value_list = df['locator_value'].tolist()
    loc_name_value_list = list(zip(locator_name_list,locator_value_list))
    cartpage_dict = dict(zip(logical_name_list,loc_name_value_list))
    return cartpage_dict

def login_logo():
    df = pd.read_excel(path_sausedemo_data,sheet_name='Login')
    logo_text = df['Logo'].tolist()
    return logo_text

def login_error_data():
    df = pd.read_excel(path_sausedemo_data,sheet_name='Login')
    message = df['Error_Message'].tolist()
    return message

def login():
    df = pd.read_excel(path_sausedemo_data, sheet_name='Login')
    login_title = df['Title'].tolist()
    return login_title

def logout_navigate_data():
    df =pd.read_excel(path_sausedemo_data,sheet_name='Logout')
    logo_name = df['Navigate_back_login_logo'].tolist()
    return logo_name


def product_names_data():
    df = pd.read_excel(path_sausedemo_data,sheet_name='Products')
    product_name_list = df['Product_name'].tolist()
    total = len(product_name_list)
    return total,product_name_list





