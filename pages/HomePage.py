import time

from locators.Locators import HomePageLoc, RegisterPageLoc
from locators.Locators import GlobalLoc
from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gotoLogin(self):
        self.click(GlobalLoc.login_CSS)

    def gotoReg(self):
        self.click(GlobalLoc.register_CSS)

    def register(self):
        self.clearing(RegisterPageLoc.email_ID)
        self.type(RegisterPageLoc.email_ID, "fdsfdsfdsf@dfgdf.com")
        self.clearing(RegisterPageLoc.phoneField_XPATH)
        self.type(RegisterPageLoc.phoneField_XPATH, "435435345")
        self.click(RegisterPageLoc.privacyCheckbox_ID)
        self.click(RegisterPageLoc.signUpbtn_XPATH)
        # assert self.textExtraction(RegisterPageLoc.passwordPageText_XPATH) == "Let's Get Started", "Not in registration process"
        self.type(RegisterPageLoc.password_XPATH, "Testtest")
        # assert self.textExtraction(HomePageLoc.loggedInOptions_XPATH.text) == "Edureka", "you are not logged in"

    def browsecateg(self):
        self.mouseOver(HomePageLoc.browseCategories_CSS)
        self.click(HomePageLoc.cloudComp_CSS)
        pass


