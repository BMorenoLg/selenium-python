from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "ul.nav.navbar-nav > li:nth-child(4) > a").click()

driver.find_element(By.NAME, "name").send_keys("Laura Basto")


driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("lauragbasto@gmail.com")


driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

time.sleep(3)
driver.find_element(By.ID, "id_gender2").click()

driver.find_element(By.NAME, "password").send_keys("Simona30130")

driver.find_element(By.XPATH, "//select[@data-qa='days']").click()
driver.find_element(By.XPATH, "//select[@data-qa='days']//option[@value='16']").click()

driver.find_element(By.XPATH, "//select[@data-qa='months']").click()
driver.find_element(By.XPATH, "//select[@data-qa='months']//option[@value='10']").click()

driver.find_element(By.XPATH, "//select[@data-qa='years']").click()
driver.find_element(By.XPATH, "//option[@value='1995']").click()


driver.find_element(By.XPATH, "//input[@data-qa='first_name']").send_keys("Laura")
driver.find_element(By.XPATH, "//input[@data-qa='last_name']").send_keys("Basto")
driver.find_element(By.XPATH, "//input[@data-qa='address']").send_keys("C19")

driver.find_element(By.XPATH, "//select[@data-qa='country']//option[@value='United States']").click()

driver.find_element(By.XPATH, "//input[@data-qa='state']").send_keys("Yucatan")
driver.find_element(By.XPATH, "//input[@data-qa='city']").send_keys("Mérida")
driver.find_element(By.XPATH, "//input[@data-qa='zipcode']").send_keys("00000")
driver.find_element(By.XPATH, "//input[@data-qa='mobile_number']").send_keys("999999")

driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()