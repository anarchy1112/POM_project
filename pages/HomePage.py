from locators.Locators import HomePageLoc
from locators.Locators import GlobalLoc
from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super.__init__(self)

    def gotoLogin(self):
        self.click(GlobalLoc.login_CSS)

    def gotoReg(self):
        self.click(GlobalLoc.register_CSS)

    def browsecateg(self):
        self.mouseOver(HomePageLoc.browseCategories_CSS)
        pass

    def 
