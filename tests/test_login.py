from selenium import webdriver
from pages.actions.register_actions import RegisterActions
# import allure

import pytest
import time

# @allure.suite("lading page")
# @allure.title("registration from userpyt")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    
    register = RegisterActions(driver)
    register.load("https://demoqa.com/automation-practice-form")
    register.type_name("Laura")
    register.type_lastname("Basto")
    register.type_email("lauragbasto@gmail.com")
    register.click_gender()
    register.type_mobile("9991169056")
    register.click_birth()
    register.click_month()
    register.click_year()
    register.click_day()
    register.type_subject("M")
    register.click_optionSubject()
    register.click_hobbie()
    register.upload_file()
    register.scroll_to_state()
    time.sleep(2)
    register.state()
    register.city()
    register.click_submit()
    time.sleep(10)
    