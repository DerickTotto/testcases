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
    'https://onecampus.laureate.net/#/language-buddies' : 'https://onecampus.laureate.net/#/language-buddies'
}

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Global_Network(unittest.TestCase):
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
        self.dp.scrollDown("2600")
        time.sleep(2)
        result_connect = self.dp.verifyTextConnect()
        self.ts.mark(result_connect, "Is not connect?", "5814")
        self.dp.clickConnectButton()
        time.sleep(2)
        result_connected = self.dp.verifyTextConnected()
        self.ts.mark(result_connected,"Is Connected?","5814")
        time.sleep(2)
        self.dp.clickConnectButton()
        time.sleep(2)
        href_learn_more = self.dp.obtainhrefLearnMoreGN()
        time.sleep(2)
        verify_forward = self.dp.verifyForwardGN()
        if verify_forward is True:
            self.dp.clickForwardGN()
            time.sleep(1)
        learn_more_url = self.dp.clickLearnMoreGN()
        time.sleep(2)
        if dict_url[href_learn_more] == learn_more_url:
            self.ts.mark(True, "We go to Lenguage Buddies?", "5814")
        else:
            self.ts.mark(False, "We go to Lenguage Buddies?" + dict_url[href_learn_more] + "  ___  " + learn_more_url, "5814")
        self.dp.goBack()
        time.sleep(2)
        self.dp.clickFindConnections()
        result_find_connections = self.dp.verifySearchBox()
        self.ts.markFinal("Global Network", result_find_connections, "We go to find connections?", "5814")
