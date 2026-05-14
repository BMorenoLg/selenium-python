from .base_actions import BaseActions
from pages.page_objects.register import Register
from selenium.webdriver.common.keys import Keys

class RegisterActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    def type_name(self, name:str):
        self.type_info(Register.nameInput, name)

    def type_lastname(self, lastname:str):
        self.type_info(Register.lastnameInput, lastname)

    def type_email(self, email:str):
        self.type_info(Register.emailInput, email)
        
    def type_password(self, password:str):
        self.type_info(Register.passInput, password)
        
    def type_mobile(self, mobile:int):
        self.type_info(Register.mobileInput, mobile)

    def click_gender(self):
        self.element_click(Register.gender)

    def click_birth(self):
        self.element_click(Register.birth)

    def click_month(self):
        self.element_click(Register.month)

    def click_year(self):
        self.element_click(Register.year)

    def click_day(self):
        self.element_click(Register.day)

    def type_subject(self, subject:str):
        self.type_info(Register.subjectInput, subject)
    
    def click_optionSubject(self):
        self.element_click(Register.optionSubject)  
        
    def click_login(self):
        self.element_click(Register.loginButton)
    
    def click_hobbie(self):
        self.element_click(Register.hobbie)
    
        
    def upload_file(self):
        self._upload_file(Register.upload_file)
        

    