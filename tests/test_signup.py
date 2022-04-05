import logging

import pytest
from locators.Locators import HomePageLoc
from tests.BaseTest import BaseTest
from pages.HomePage import HomePage
from utility import dataGeter
from utility.logger import Log

log=Log(__name__,logging.DEBUG)
class TestSignUp(BaseTest):

    @pytest.mark.parametrize("mail,phone_no,password", dataGeter.dataGet("Sheet1"))
    def test_dosignup(self,mail,phone_no,password):
        page=HomePage(self.driver)
        page.gotoReg()
        page.register(mail,phone_no,password)
        log.logger.info("ending a test")
        assert page.textExtraction2(HomePageLoc.myprofile_XPATH)=="My Profile"


    @pytest.mark.skip
    def test_golog(self):
        pages=HomePage(self.driver)
        pages.gotoLogin()





