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
    'https://onecampus.laureate.net/#!/wobi/video/1048' : 'https://onecampus.laureate.net/#/wobi/video/1048',
    'https://onecampus.laureate.net/#!/wobi/video/1424' : 'https://onecampus.laureate.net/#/wobi/video/1424'
}


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Best_OC(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.dp = DashboardPage(self.driver)

    @pytest.mark.run(order=1)
    def test_Dashboard_GlobalNetwork(self):
        self.log.info("***" * 20)
        self.log.info("Test Dashboard_GlobalNetwork Started")
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
        self.dp.scrollDown("3800")
        label_best_oc = self.dp.verifyBestOC()
        self.ts.mark(label_best_oc, "Is the label of best of OC present?", "5816")
        card1_best_oc = self.dp.verifyCard1BestOC()
        self.ts.mark(card1_best_oc, "Is the card 1 of best of OC present?", "5816")
        card2_best_oc = self.dp.verifyCard2BestOC()
        self.ts.mark(card2_best_oc, "Is the card 2 of best of OC present?", "5816")
        href = self.dp.hrefCard2BestOC()
        url = self.dp.clickCard2BestOC()
        time.sleep(2)
        if dict_url[href] == url:
            self.ts.mark(True, "we go to the card 2 of Best of OC?", "5816")
        else:
            self.ts.mark(False,"we go to the card 2 of Best of OC?", "5816")
        card3_best_oc = self.dp.verifyCard3BestOC()
        self.ts.mark(card3_best_oc, "Is the card 3 of best of OC present?", "5816")
        self.dp.clickForwardBestOC()
        time.sleep(1)
        card4_best_oc = self.dp.verifyCard4BestOC()
        self.ts.mark(card4_best_oc, "Is the card 4 of best of OC present?", "5816")
        self.dp.clickForwardBestOC()
        time.sleep(1)
        card5_best_oc = self.dp.verifyCard5BestOC()
        self.ts.mark(card5_best_oc, "Is the card 5 of best of OC present?", "5816")
        href = self.dp.hrefCard5BestOC()
        url = self.dp.clickCard5BestOC()
        time.sleep(2)
        if dict_url[href] == url:
            self.ts.mark(True, "we go to the card 5 of Best of OC?", "5816")
        else:
            self.ts.mark(False, "we go to the card 5 of Best of OC?", "5816")

