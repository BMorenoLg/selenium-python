from selenium import webdriver
from pages.actions.register_actions import RegisterActions

import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    
    register = RegisterActions(driver)
    register.load("https://automationexercise.com/login")
    register.type_email("lauragbasto@gmail.com")
    register.type_password("Simona30130")
    register.click_login()