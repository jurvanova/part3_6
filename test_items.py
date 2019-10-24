from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#link = 'http://selenium1py.pythonanywhere.com/ru/'

def check_element_is(css):
    try:
        browser.find_element_by_css_selector(css)
    except:
        return False
    return True

def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)

    assert check_element_is('.btn-add-to-basket'), 'Button \'Add to cart\' is undefined'
