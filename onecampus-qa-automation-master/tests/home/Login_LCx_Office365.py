from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from os.path import join, dirname
from dotenv import load_dotenv
import os
import time

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

username = os.getenv('email')
password = os.getenv('oc_password')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_Login_LCx_Office365(self):
        self.log.info("***" * 20)
        self.log.info("Test Login_LCx_Office365 Started")
        self.log.info("***" * 20)
        self.lp.clickLoginLink()
        time.sleep(1)
        self.lp.enterUsername("docentetest@unitec.edu")
        self.lp.clickSubmitButton()
        time.sleep(10)
        self.lp.enterOfficeUsername("docentetest@unitec.edu")
        time.sleep(1)
        self.lp.clickNextOffice()
        time.sleep(1)
        self.lp.enterOfficePassword("Luxo0429")
        time.sleep(1)
        self.lp.clickNextOffice()
        time.sleep(1)
        self.lp.clickOfficeNOButton()
        time.sleep(1)
        result = self.lp.verifyLoginSuccessful()
        self.ts.setResult(result, "Test Login_LCx_Office365 Successful", "4122")
        assert result == True
