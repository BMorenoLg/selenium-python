from .base_actions import BaseActions
from pages.page_objects.register import Register

class RegisterActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    
    def type_email(self, email:str):
        self.type_info(Register.emailInput, email)
        
    def type_password(self, password:str):
        self.type_info(Register.passInput, password)
        
    def click_login(self):
        self.element_click(Register.loginButton)