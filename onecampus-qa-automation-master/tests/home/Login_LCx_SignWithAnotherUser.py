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
    def test_Login_LCx_SignWithAnotherUser(self):
        self.log.info("***" * 20)
        self.log.info("Test Login_LCx_SignWithAnotherUser Started")
        self.log.info("***" * 20)
        time.sleep(1)
        self.lp.clickLoginLink()
        self.lp.login("test@test.net","test")
        time.sleep(1)
        self.lp.clickAnotherUser()
        result = self.lp.verifyUsername()
        self.ts.setResult(result, "Test Login_LCx_SignWithAnotherUser Successful", "4125")
        assert result == True
