import logging
import time


from utility.logger import Log
from locators.Locators import HomePageLoc, RegisterPageLoc
from locators.Locators import GlobalLoc
from pages.BasePage import BasePage
log=Log(__name__,logging.DEBUG)


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gotoLogin(self):
        self.click(GlobalLoc.login_XPATH)

    def gotoReg(self):
        self.click(GlobalLoc.register_XPATH)


    def register(self,mail,phone_no,password):
        self.clearing(RegisterPageLoc.email_XPATH)
        self.type(RegisterPageLoc.email_XPATH, mail)
        self.clearing(RegisterPageLoc.phoneField_XPATH)
        log.logger.debug("debugging a homepage")
        self.type(RegisterPageLoc.phoneField_XPATH, phone_no)
        self.click(RegisterPageLoc.privacyCheckbox_XPATH)
        self.click(RegisterPageLoc.signUpbtn_XPATH)
        self.wait(RegisterPageLoc.password_XPATH)           #proba implementacije eksplicitnog waita, ne valja, probaj opet promenio uslov, RADI!!!!
        self.type(RegisterPageLoc.password_XPATH, password)
        self.click(RegisterPageLoc.startLearningBtn_XPATH)
        self.click(HomePageLoc.loggedInOptions_XPATH)




    def browsecateg(self):
        self.mouseOver(HomePageLoc.browseCategories_XPATH)
        self.click(HomePageLoc.cloudComp_XPATH)
        pass


