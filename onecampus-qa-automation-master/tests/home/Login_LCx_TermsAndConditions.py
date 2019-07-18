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
    def test_termsUS(self):
        self.log.info("***" * 20)
        self.log.info("Test Login.TermsAndConditions in English Started")
        self.log.info("***" * 20)
        self.lp.clickLoginLink()
        time.sleep(1)
        urlTerms = self.lp.termsUS()
        time.sleep(1)
        verification = self.lp.verifyTermsUS(urlTerms)
        self.ts.setResult(verification, "Test Login.TermsAndConditions in English", "4123")
        assert verification == True
        time.sleep(1)

    @pytest.mark.run(order=2)
    def test_termsPT(self):
        self.log.info("***" * 20)
        self.log.info("Test Login.TermsAndConditions in Portuguese Started")
        self.log.info("***" * 20)
        time.sleep(1)
        urlTerms = self.lp.termsPT()
        time.sleep(1)
        verification = self.lp.verifyTermsPT(urlTerms)
        self.ts.setResult(verification, "Test Login.TermsAndConditions in Portuguese", "4123")
        assert verification == True
        time.sleep(1)

    @pytest.mark.run(order=3)
    def test_termsES(self):
        self.log.info("***" * 20)
        self.log.info("Test Login.TermsAndConditions in Spanish Started")
        self.log.info("***" * 20)
        time.sleep(1)
        urlTerms = self.lp.termsES()
        time.sleep(1)
        verification = self.lp.verifyTermsES(urlTerms)
        self.ts.setResult(verification, "Test Login.TermsAndConditions in Spanish", "4123")
        assert verification == True
        time.sleep(1)