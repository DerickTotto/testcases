from pages.home.login_page import LoginPage
from pages.home.dashboard_page import DashboardPage
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

dict_url = {
    'https://onecampus.laureate.net/#!/learning-series/jobs-future': 'https://onecampus.laureate.net/#/learning-series/jobs-future',
    'https://exchange.laureate.net/sso/9000/the-big-know-episode-six': 'https://onecampus.thebigknow.com/workbooks/jobs-of-the-future-design-thinking'
}

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Jobs_of_the_Future(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.dp = DashboardPage(self.driver)

    @pytest.mark.run(order=1)
    def test_Dashboard_JobsOfTheFuture(self):
        self.log.info("***" * 20)
        self.log.info("Test Dashboard_JobsOfTheFuture Started")
        self.log.info("***" * 20)
        self.lp.clickLoginLink()
        time.sleep(2)
        self.lp.login(username, password)
        time.sleep(2)
        modal_result = self.dp.verifyTourModal()
        if modal_result:
            self.dp.clickSkipTour()
            time.sleep(2)
            self.dp.clickGotItTour()
            time.sleep(2)
        self.dp.scrollDown("1250")
        time.sleep(2)
        result_big_card = self.dp.verifyJobsBigCard()
        self.ts.mark(result_big_card,"Is the big card of Jobs of the future present?","5819")
        result_card1_jobs = self.dp.verifyCard1Jobs()
        self.ts.mark(result_card1_jobs, "Is the card 1 of Jobs of the future present?", "5819")
        result_card2_jobs = self.dp.verifyCard2Jobs()
        self.ts.mark(result_card2_jobs, "Is the card 2 of Jobs of the future present?", "5819")
        result_card3_jobs = self.dp.verifyCard3Jobs()
        self.ts.mark(result_card3_jobs, "Is the card 3 of Jobs of the future present?", "5819")
        result_card4_jobs = self.dp.verifyCard4Jobs()
        self.ts.mark(result_card4_jobs, "Is the card 4 of Jobs of the future present?", "5819")
        time.sleep(2)
        href_big_card_jobs = self.dp.obtainHrefJobsBigCard()
        time.sleep(2)
        self.dp.clickJobsBigCard()
        time.sleep(2)
        url_big_card_jobs = self.dp.urlJobsMainCard()
        if dict_url[href_big_card_jobs] == url_big_card_jobs:
            self.ts.mark(True, "We are in Jobs of the future?", "5819")
        else:
            self.ts.mark(False, "We are in Jobs of the future?", "5819")
        time.sleep(1)
        self.dp.clickOCLogo()
        time.sleep(2)
        self.dp.scrollDown("1250")
        time.sleep(3)
        href_card1_jobs = self.dp.obtainHrefJobsCard1()
        time.sleep(1)
        url_card1_jobs = self.dp.clickCard1Jobs()
        time.sleep(2)
        if dict_url[href_card1_jobs] == url_card1_jobs:
            self.ts.mark(True, "We are in Card 1 of Jobs of the future?", "5819")
        else:
            self.ts.setResult(False, "We are in Card 1 of Jobs of the future?", "5819")
        time.sleep(1)
