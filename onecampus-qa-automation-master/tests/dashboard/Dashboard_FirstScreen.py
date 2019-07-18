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

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class First_Screen(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.dp = DashboardPage(self.driver)

    @pytest.mark.run(order=1)
    def test_Dashboard_FirstScreen(self):
        self.log.info("***" * 20)
        self.log.info("Test Dashboard.FirstScreen Started")
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
        logo_result = self.dp.verifyLogoUniversity()
        self.ts.mark(logo_result, "Logo of the university present?","5818")
        welcome_result = self.dp.verifyTextWelcome()
        self.ts.mark(welcome_result, "The Welcome text present?","5818")
        main_card_result = self.dp.verifyMainCardDB()
        self.ts.mark(main_card_result, "The main card of OC is present?", "5818")
        profskill_link_result = self.dp.verifyCheckSkillbuttonAux()
        self.ts.mark(profskill_link_result, "The Check Skill link is present?", "5818")
        youthact_link_result = self.dp.verifyYouthActionbuttonAux()
        self.ts.mark(youthact_link_result, "The youth action link is present?", "5818")
        presenskill_link_result = self.dp.verifyPresentationChallengebuttonAux()
        self.ts.mark(presenskill_link_result, "The Presentation challenge link is present?", "5818")
        time.sleep(3)
        # Step 2,3
        LS_url = self.dp.clickLearningSeriesButtonMain()
        if LS_url == "https://onecampus.laureate.net/#/learning-series/how-ready-are-you":
            self.ts.mark(True, "The redirect to Learning series?","5818")
        else:
            self.ts.mark(False, "The redirect to Learning series?", "5818")
        time.sleep(4)
        OC_url = self.dp.clickOCLogo()
        if OC_url == "https://onecampus.laureate.net/#/dashboard":
            self.ts.mark(True, "The redirect to OneCampus?", "5818")
        else:
            self.ts.mark(False, "The redirect to OneCampus?", "5818")
        time.sleep(4)
        # step 4, 5
        CS_url = self.dp.clickCheckSkillsbuttonAux()
        if CS_url == "https://onecampus.laureate.net/#/professional-skills":
            self.ts.mark(True, "The redirect to CheckSkill?", "5818")
        else:
            self.ts.mark(False, "The redirect to CheckSkill?", "5818")
        time.sleep(4)
        OC_url = self.dp.clickOCLogo()
        if OC_url == "https://onecampus.laureate.net/#/dashboard":
            self.ts.mark(True, "The redirect to OneCampus?", "5818")
        else:
            self.ts.mark(False, "The redirect to OneCampus?", "5818")
        time.sleep(4)
        # step 6 7
        YA_url = self.dp.clickYouthActionbuttonAux()
        if YA_url == "https://onecampus.laureate.net/#/v2/youth-action-net":
            self.ts.mark(True, "The redirect to YouthAction?", "5818")
        else:
            self.ts.mark(False, "The redirect to YouthAction?", "5818")
        time.sleep(4)
        OC_url = self.dp.clickOCLogo()
        if OC_url == "https://onecampus.laureate.net/#/dashboard":
            self.ts.mark(True, "The redirect to OneCampus?", "5818")
        else:
            self.ts.mark(False, "The redirect to OneCampus?", "5818")
        time.sleep(4)
        # step 8, 9
        PC_url= self.dp.clickPresentationChallengebuttonAux()
        if PC_url == "https://onecampus.laureate.net/#/presentation-challenge/cycle-4":
            self.ts.mark(True, "The redirect to Presentation Challenge?", "5818")
        else:
            self.ts.mark(False, "The redirect to Presentation Challenge?", "5818")
        time.sleep(4)
        OC_url = self.dp.clickOCLogo()
        if OC_url == "https://onecampus.laureate.net/#/dashboard":
            self.ts.mark(True, "The redirect to OneCampus?", "5818")
        else:
            self.ts.mark(False, "The redirect to OneCampus?", "5818")
        time.sleep(4)
        pick_up_card_link = self.dp.verifyContinuePickUpCard()
        self.ts.markFinal("Dashboard_FirstScreen",pick_up_card_link, "The card of pick up where you left off is present?", "5818")