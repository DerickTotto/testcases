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
    'https://onecampus.laureate.net/#!/video/1976': 'https://onecampus.laureate.net/#/video/1976',
    'https://onecampus.laureate.net/#!/video/1974': 'https://onecampus.laureate.net/#/video/1974',
    'https://onecampus.laureate.net/#!/video/1975': 'https://onecampus.laureate.net/#/video/1975'
}

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Feature_Collection(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.dp = DashboardPage(self.driver)

    @pytest.mark.run(order=1)
    def test_Dashboard_FeatureCollection(self):
        self.log.info("***" * 20)
        self.log.info("Test Dashboard_JobsOfTheFuture Started")
        self.log.info("***" * 20)
        self.lp.clickLoginLink()
        time.sleep(4)
        self.lp.login(username, password)
        time.sleep(4)
        modal_result = self.dp.verifyTourModal()
        if modal_result:
            self.dp.clickSkipTour()
            time.sleep(2)
            self.dp.clickGotItTour()
            time.sleep(2)
        self.dp.scrollDown("1750")
        time.sleep(4)
        big_card_feature_result = self.dp.verifyBigCardFeaturedCollection()
        self.ts.mark(big_card_feature_result, "Big Card of Feature Collection is present?", "5796")
        card1_feature_result = self.dp.verifyCard1FeatureCollection()
        self.ts.mark(card1_feature_result, "Card 1 of Feature Collection is present?", "5796")
        card2_feature_result = self.dp.verifyCard2FeatureCollection()
        self.ts.mark(card2_feature_result, "Card 2 of Feature Collection is present?", "5796")
        forward_row_feature_result= self.dp.verifyForwardRowFeatureCollection()
        self.ts.mark(forward_row_feature_result, "Forward row of Feature Collection is present?", "5796")
        href_card1_feature = self.dp.obtainHrefCard1FeatureCollection()
        url_card1_feature = self.dp.clickCard1FeatureCollection()
        if dict_url[href_card1_feature] == url_card1_feature:
            self.ts.mark(True, "The Redirect to Card 1?", "5796")
        else:
            self.ts.mark(False, "The Redirect to Card 1?", "5796")
        time.sleep(4)
        href_card2_feature = self.dp.obtainHrefCard2FeatureCollection()
        url_card2_feature = self.dp.clickCard2FeatureCollection()
        if dict_url[href_card2_feature] == url_card2_feature:
            self.ts.mark(True, "The Redirect to Card 2?", "5796")
        else:
            self.ts.mark(False, "The Redirect to Card 2?", "5796")
        time.sleep(4)
        self.dp.clickForwardFeatureCollection()
        href_card3_feature = self.dp.obtainHrefCard3FeatureCollection()
        url_card3_feature = self.dp.clickCard3FeatureCollection()
        if dict_url[href_card3_feature] == url_card3_feature:
            self.ts.mark(True, "The Redirect to Card 3?", "5796")
        else:
            self.ts.mark(False, "The Redirect to Card 3?", "5796")
        time.sleep(4)