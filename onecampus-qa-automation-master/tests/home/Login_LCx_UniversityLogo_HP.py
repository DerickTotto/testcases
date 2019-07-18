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
    def test_Login_LCx_UniversityLogo_HP(self):
        self.log.info("***" * 20)
        self.log.info("Test Login_LCx_UniversityLogo_HP Started")
        self.log.info("***" * 20)
        self.lp.clickLoginLink()
        self.lp.enterUsername(username)
        self.lp.clickSubmitButton()
        time.sleep(1)
        verification = self.lp.verifyLogoUniversity()
        self.ts.setResult(verification, "Test Login_LCx_UniversityLogo_HP", "4129")
        assert verification == True
