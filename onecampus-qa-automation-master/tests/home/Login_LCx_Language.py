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
    def test_spanishLenguage(self):
        self.log.info("***" * 20)
        self.log.info("Test Login_LCx_Language in Spanish Started")
        self.log.info("***" * 20)
        time.sleep(2)
        self.lp.clickLoginLink()
        self.lp.lenguageSpanish()
        result = self.lp.verifySpanish()
        self.ts.setResult(result, "Test Login_LCx_Language in Spanish", "4124")
        assert result == True

    @pytest.mark.run(order=3)
    def test_portugueseLenguage(self):
        self.log.info("***" * 20)
        self.log.info("Test Login_LCx_Language in portuguese Started")
        self.log.info("***" * 20)
        time.sleep(2)
        self.lp.lenguagePortuguese()
        result = self.lp.verifyPortuguese()
        self.ts.setResult(result, "Test Login_LCx_Language in portuguese", "4124")
        assert result == True

    @pytest.mark.run(order=2)
    def test_englishLenguage(self):
        self.log.info("***" * 20)
        self.log.info("Test Login_LCx_Language in english Started")
        self.log.info("***" * 20)
        time.sleep(2)
        self.lp.lenguageEnglish()
        result = self.lp.verifyEnglish()
        self.ts.setResult(result, "Test Login_LCx_Language in english", "4124")
        assert result == True
