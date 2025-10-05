from selenium.webdriver.common.by import By

class Register:
    emailInput=(By.XPATH, "//input[@data-qa='login-email']")
    passInput=(By.XPATH, "//input[@data-qa='login-password']")
    loginButton=(By.XPATH, "//button[@data-qa='login-button']")
