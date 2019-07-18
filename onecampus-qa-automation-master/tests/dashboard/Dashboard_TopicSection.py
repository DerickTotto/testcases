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
    'https://onecampus.laureate.net/#!/wobi/video/1696' : 'https://onecampus.laureate.net/#/wobi/video/1696',
    'https://onecampus.laureate.net/#!/wobi/video/1364' : 'https://onecampus.laureate.net/#/wobi/video/1364',
    'https://onecampus.laureate.net/#!/wobi/video/1044' : 'https://onecampus.laureate.net/#/wobi/video/1044',
    'https://onecampus.laureate.net/#!/wobi/video/1368' : 'https://onecampus.laureate.net/#/wobi/video/1368',
    'https://onecampus.laureate.net/#!/wobi/video/1046' : 'https://onecampus.laureate.net/#/wobi/video/1046',
    'https://onecampus.laureate.net/#!/wobi/video/1367' : 'https://onecampus.laureate.net/#/wobi/video/1367',
    'https://onecampus.laureate.net/#!/wobi/video/1305' : 'https://onecampus.laureate.net/#/wobi/video/1305',
    'https://onecampus.laureate.net/#!/wobi/video/1043' : 'https://onecampus.laureate.net/#/wobi/video/1043',
    'https://onecampus.laureate.net/#!/wobi/video/1359' : 'https://onecampus.laureate.net/#/wobi/video/1359',
    'https://onecampus.laureate.net/#!/wobi/video/1499' : 'https://onecampus.laureate.net/#/wobi/video/1499'
}


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Topic_Section(unittest.TestCase):
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
        self.dp.scrollDown("3400")
        time.sleep(6)
        self.dp.clickSociology()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result,"The Main Card of Sociology is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Sociology is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Sociology is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Sociology is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Sociology?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Sociology?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickPsychology()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Psychology is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Psychology is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Psychology is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Psychology is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Psychology?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Psychology?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickManagement()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Management is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Management is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Management is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Management is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Management?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Management?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickEconomics()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Economics is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Economics is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Economics is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Economics is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Economics?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Economics?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickHumanResources()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of HumanResources is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of HumanResources is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of HumanResources is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of HumanResources is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of HumanResources?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of HumanResources?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickTechnology()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Technology is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Technology is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Technology is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Technology is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Technology?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Technology?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickEnterpreneurship()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Enterpreneurship is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Enterpreneurship is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Enterpreneurship is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Enterpreneurship is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Enterpreneurship?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Enterpreneurship?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickInnovation()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Innovation is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Innovation is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Innovation is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Innovation is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Innovation?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Innovation?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickLeadership()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Leadership is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Leadership is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Leadership is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Leadership is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.mark(True, "We go to the Card 2 of Leadership?", "5815")
        else:
            self.ts.mark(False, "We go to the Card 2 of Leadership?" + href + " -- " + url, "5815")
        time.sleep(6)
        self.dp.clickMarketing()
        main_card_result = self.dp.verifyMainCardTopic()
        self.ts.mark(main_card_result, "The Main Card of Marketing is present?", "5815")
        card1_result = self.dp.verifyCard1Topic()
        self.ts.mark(card1_result, "The Card 1 of Marketing is present?", "5815")
        card2_result = self.dp.verifyCard2Topic()
        self.ts.mark(card2_result, "The Card 2 of Marketing is present?", "5815")
        self.dp.forwardTopic()
        card3_result = self.dp.verifyCard3Topic()
        self.ts.mark(card3_result, "The Card 3 of Marketing is present?", "5815")
        href = self.dp.hrefCard2Topic()
        url = self.dp.clickCard2Topic()
        if dict_url[href] == url:
            self.ts.markFinal("Learning Topic",True, "We go to the Card 2 of Marketing?", "5815")
        else:
            self.ts.markFinal("Learning Topic",False, "We go to the Card 2 of Marketing?" + href + " -- " + url, "5815")
