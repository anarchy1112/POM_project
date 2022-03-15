import time

import pages.HomePage
from tests.BaseTest import BaseTest
from pages.HomePage import HomePage


class TestSignUp(BaseTest):


    def test_dosignup(self):
        page=HomePage(self.driver)
        page.gotoReg()
        time.sleep(1)
        page.register()

    def test_golog(self):
        pages=HomePage(self.driver)
        pages.gotoLogin()
        time.sleep(1)




