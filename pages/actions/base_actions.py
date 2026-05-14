from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time

class BaseActions:

    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def _wait_for_element(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(by_locator)
            )
            return self.driver.find_element(*by_locator)
        except TimeoutException:
            print("The element was not found")
            return None

    def element_click(self, by_locator):
        user = self._wait_for_element(by_locator)
        if user:
            user.click()
        else:
            raise Exception("Cant click on the element")

    def type_info(self, by_locator, keyword):
        user = self._wait_for_element(by_locator)
        if user:
            user.send_keys(keyword)
        else:
            raise Exception("Cant click on the element")    
        
    def is_displayed(self, by_locator)-> bool:
        user = self._wait_for_element(by_locator)
        if user:
            user.is_displayed()
        else:
            return False
        
    def is_enabled(self, by_locator)-> bool:
        user = self._wait_for_element(by_locator)
        if user:
            user.is_enabled()
        else:
            return False
        
    def _upload_file(self, by_locator):
        user = self._wait_for_element(by_locator)
        if user:
            user.is_displayed()
            upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "avatar.jpg"))
            #print(f"variable: {upload_file}")
            user.send_keys(upload_file)
        else:
            raise Exception("Cant click on the element")
        
    def remove_ads(self):
        self.driver.execute_script("""var ads = document.querySelectorAll('#fixedban, .bannerad, iframe'); ads.forEach(function(ad) { ad.remove(); });""")

    def element_double_click(self, by_locator, by_locator_2):
        user = self._wait_for_element(by_locator)
        
        if user :
            user.click()
            user2 = self._wait_for_element(by_locator_2)
            if user2:
                user2.click()
            else:
                raise Exception("Cant click on the second element")
        else:
            raise Exception("Cant click on the element")
        
    def scroll_to_element(self, by_locator):
        user = self._wait_for_element(by_locator)
        if user:
            self.driver.execute_script("arguments[0].scrollIntoView();", user)
        else:
            raise Exception("Element not found to scroll")
        