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
    def test_Login_LCx_HavingTroubleLogginInEN(self):
        self.log.info("***" * 20)
        self.log.info("	Login.HavingTroubleLogginIn in English Started")
        self.log.info("***" * 20)
        self.lp.clickLoginLink()
        time.sleep(1)
        self.lp.login(username)
        time.sleep(1)
        problemURL = self.lp.problemsUS()
        result = self.lp.verifyProblemsUS(problemURL)
        self.ts.setResult(result, "Login.HavingTroubleLogginIn in English Successful", "4126")
        assert result == True

    @pytest.mark.run(order=2)
    def test_Login_LCx_HavingTroubleLogginInPT(self):
        self.log.info("***" * 20)
        self.log.info("	Login.HavingTroubleLogginIn in Portuguese Started")
        self.log.info("***" * 20)
        time.sleep(1)
        problemURL = self.lp.problemsPT()
        result = self.lp.verifyProblemsPT(problemURL)
        self.ts.setResult(result, "Login.HavingTroubleLogginIn in Portuguese Successful", "4126")
        assert result == True

    @pytest.mark.run(order=3)
    def test_Login_LCx_HavingTroubleLogginInES(self):
        self.log.info("***" * 20)
        self.log.info("	Login.HavingTroubleLogginIn in Spanish Started")
        self.log.info("***" * 20)
        time.sleep(2)
        problemURL = self.lp.problemsES()
        result = self.lp.verifyProblemsES(problemURL)
        self.ts.setResult(result, "Login.HavingTroubleLogginIn in Spanish Successful", "4126")
        assert result == True
