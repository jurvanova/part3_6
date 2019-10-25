from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

#additional link for checking test fails
#link = 'http://selenium1py.pythonanywhere.com/ru/'

#function for determination an element

def check_element_is(css, browser):
    try:
        browser.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True

#cheking for 'Add to cart' button

def test_check_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(10)
    btn = check_element_is('.btn-add-to-basket', browser)
    assert btn , 'Button \'Add to cart\' is undefined'
