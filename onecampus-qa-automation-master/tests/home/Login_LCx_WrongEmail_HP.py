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
    def test_Login_LCx_WrongEmail_HP(self):
        self.log.info("***" * 20)
        self.log.info("Test Login.LCx.WrongCredentials.HP in Username Started")
        self.log.info("***" * 20)
        time.sleep(1)
        self.lp.clickLoginLink()
        time.sleep(1)
        self.lp.login()
        result = self.lp.usernameError()
        self.ts.setResult(result, "Test Login.LCx.WrongCredentials.HP in Username", "4127")
        assert result == True
        self.lp.clearUsername()