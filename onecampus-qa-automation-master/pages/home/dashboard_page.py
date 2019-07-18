import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class DashboardPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # OC Logo Direct to dashboard
    _OC_dashboard = "/html//oc-root//oc-header//one-header//a[@href='/#!/dashboard']/img[@alt='']"
    # University Logo and Welcome Text
    _logo_university = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__logo']"
    _welcome_text = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__hdg']"
    # Tour
    _modal_tour = "//*[@id='otour-step-0']/div"
    _skip_tour = "/html//oc-root/div/div/div[@class='ng-scope']//one-tour[@class='ng-isolate-scope']/div/div[1]/div[@class='one-infotip']//a[@href='']"
    _gotit_tour = "/html//oc-root/div/div[@class='main']/div[@class='ng-scope']//one-tour[@class='ng-isolate-scope']//div[@class='one-tour__step one-tour__step--centered']//div[@class='one-infotip__footer']/button[2]"
    # Dashboard 4 cards
    _main_card_ls = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__main-card']"
    _card_ls_button = "//div[@class='one-feature-grid__main-card']/one-feature-card[@class='ng-isolate-scope']/div//one-feature-card-action[@type='button']/button[@type='button']"
    _aux_cards = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__aux-cards']"
    _check_skill_card_button = "//*[@id='dashboard-onecampus-container']/dashboard-features/div/div/div[4]/div[1]/one-feature-card/div/div/one-feature-card-action/button"
    _youth_action_card_button = "//*[@id='dashboard-onecampus-container']/dashboard-features/div/div/div[4]/div[2]/one-feature-card/div/div/one-feature-card-action/button"
    _presentation_challenge_card_button = "//*[@id='dashboard-onecampus-container']/dashboard-features/div/div/div[4]/div[3]/one-feature-card/div/div/one-feature-card-action/button"
    # Pick up where you left
    _text_pickup = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//current-courses//div[.='Pick up where you left off']"
    _card1_pickup = "//current-courses//one-scrollgrid[@class='ng-isolate-scope']//one-scrollgrid-row//one-scrollgrid-item/div[@class='one-scrollgrid__item']"
    _text_card1_pickup = "//current-courses//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]//episode-status//h4"
    _continue_button_card1_pickup = "//current-courses//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row//one-scrollgrid-item//episode-status//div[@class='one-summary-tile--content']/a"
    # Jobs of the future
    _big_card_jobs_link = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[1]/div/div[2]/div[3]/a"
    _card1_jobs = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[1]/div/one-scrollgrid-item[1]/div/episode-status/div/div[2]/a"
    _card2_jobs = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[1]/div/one-scrollgrid-item[2]/div/episode-status/div/div[2]/a"
    _card3_jobs = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[2]/div/one-scrollgrid-item[1]/div/episode-status/div/div[2]/a"
    _card4_jobs = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[2]/div/one-scrollgrid-item[2]/div/episode-status/div/div[2]/a"
    # Laureate talks Brazil
    _back_button_slider = "/html//div[@id='dashboard-onecampus-container']/feature-section/div//one-scrollgrid[@class='ng-isolate-scope']/div[@class='one-scrollgrid__controls']/button[1]"
    _forward_button_slider = "/html//div[@id='dashboard-onecampus-container']/feature-section/div//one-scrollgrid[@class='ng-isolate-scope']/div[@class='one-scrollgrid__controls']/button[2]"
    _big_card_talks_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//div[@class='one-feature-section__main']"
    _card1_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]/div[@class='one-scrollgrid__item']/one-flexcard//a"
    _card2_talk_brazil = "//*[@id='dashboard-onecampus-container']/feature-section/div/div/div[2]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[2]/div/one-flexcard/div/div[3]/a"
    _alternate_card2_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[2]/div[@class='one-scrollgrid__item']/one-flexcard//a"
    _card3_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[3]/div[@class='one-scrollgrid__item']/one-flexcard//a"
    _card4_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[4]/div[@class='one-scrollgrid__item']/one-flexcard//a"
    _card5_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[5]/div[@class='one-scrollgrid__item']/one-flexcard//a"
    # Learning Topics
    _marketing_button = "//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[1]/label[@class='ng-binding']"
    _leadership_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[2]/label[@class='ng-binding']"
    _innovation_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[3]/label[@class='ng-binding']"
    _enterpreneurship_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[4]/label[@class='ng-binding']"
    _technology_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[5]/label[@class='ng-binding']"
    _humanresources_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[6]/label[@class='ng-binding']"
    _economics_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[7]/label[@class='ng-binding']"
    _management_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[8]/label[@class='ng-binding']"
    _psychology_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[9]/label[@class='ng-binding']"
    _sociology_button = "/html//div[@id='dashboard-onecampus-container']//form[@name='selectedPillTopics']/div[10]/label[@class='ng-binding']"
    # Learning Topic
    _main_card_Topic = "/html//div[@id='dashboard-onecampus-container']/div[1]//div[@class='one-feature-section__main']"
    _card1_Topic = "//*[@id='dashboard-onecampus-container']/div[1]/div/div[4]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[1]/div/one-flexcard/div/div[3]/a"
    _card2_Topic = "//*[@id='dashboard-onecampus-container']/div[1]/div/div[4]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[2]/div/one-flexcard/div/div[3]/a"
    _card3_Topic = "//*[@id='dashboard-onecampus-container']/div[1]/div/div[4]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[3]/div/one-flexcard/div/div[3]/a"
    _forward_topic = "//*[@id='dashboard-onecampus-container']/div[1]/div/div[4]/div/div[2]/one-scrollgrid/div[2]/button[2]"
    # Global Network
    _connect_global_network = "//div[@id='dashboard-onecampus-container']/global-network[@class='ng-isolate-scope']//div[@class='container container__standard']/div[3]/one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]//user-recommendation-card//span[@class='button connections--why__button ng-binding']"
    _learn_more_global_network = "//*[@id='dashboard-onecampus-container']/global-network/div/div/div[3]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[4]/div/a"
    _find_connections_button = "/html//div[@id='dashboard-onecampus-container']/global-network[@class='ng-isolate-scope']//a[.='Find Connections']"
    _connect_text = "//div[@id='dashboard-onecampus-container']/global-network[@class='ng-isolate-scope']//div[@class='container container__standard']/div[3]/one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]//user-recommendation-card//span[@class='button connections--why__button ng-binding' and contains(text(),'Connect')]"
    _connected_text = "//*[@id='dashboard-onecampus-container']/global-network/div/div/div[3]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[1]/div/user-recommendation-card/div/div/div/span[2]"
    _search_find_connections ="//*[@id='global-input']"
    _forward_GN = "//*[@id='dashboard-onecampus-container']/global-network/div/div/div[3]/one-scrollgrid/div[2]/button[2]"
    # Best of OC
    _best_OC_Label = "//*[@id='dashboard-onecampus-container']/div[2]/div"
    _card1_bestOC = "//*[@id='dashboard-onecampus-container']/div[2]/div/div[2]/dashboard-resources/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[1]/div/one-flexcard/div/div[3]/a"
    _card2_bestOC = "//*[@id='dashboard-onecampus-container']/div[2]/div/div[2]/dashboard-resources/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[2]/div/one-flexcard/div/div[3]/a"
    _card3_bestOC = "//*[@id='dashboard-onecampus-container']/div[2]/div/div[2]/dashboard-resources/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[3]/div/one-flexcard/div/div[3]/a"
    _card4_bestOC = "//*[@id='dashboard-onecampus-container']/div[2]/div/div[2]/dashboard-resources/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[4]/div/one-flexcard/div/div[3]/a"
    _card5_bestOC = "//*[@id='dashboard-onecampus-container']/div[2]/div/div[2]/dashboard-resources/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[5]/div/one-flexcard/div/div[3]/a"
    _forward_BestOC = "//*[@id='dashboard-onecampus-container']/div[2]/div/div[2]/dashboard-resources/one-scrollgrid/div[2]/button[2]"

    def clickForwardBestOC(self):
        self.elementClick(self._forward_BestOC,locatorType="xpath")

    def verifyBestOC(self):
        return self.isElementPresent(self._best_OC_Label, locatorType="xpath")

    def verifyCard1BestOC(self):
        return self.isElementPresent(self._card1_bestOC, locatorType="xpath")

    def verifyCard2BestOC(self):
        return self.isElementPresent(self._card2_bestOC, locatorType="xpath")

    def hrefCard2BestOC(self):
        href = self.getElement(self._card2_bestOC, locatorType="xpath")
        href_card = href.get_attribute("href")
        return href_card

    def clickCard2BestOC(self):
        self.elementClick(self._card2_bestOC, locatorType="xpath")
        url = self.driver.current_url
        time.sleep(2)
        self.driver.back()
        return url

    def verifyCard3BestOC(self):
        return self.isElementPresent(self._card3_bestOC, locatorType="xpath")

    def verifyCard4BestOC(self):
        return self.isElementPresent(self._card4_bestOC, locatorType="xpath")

    def verifyCard5BestOC(self):
        return self.isElementPresent(self._card5_bestOC, locatorType="xpath")

    def hrefCard5BestOC(self):
        href = self.getElement(self._card5_bestOC, locatorType="xpath")
        href_card = href.get_attribute("href")
        return href_card

    def clickCard5BestOC(self):
        self.elementClick(self._card5_bestOC, locatorType="xpath")
        url = self.driver.current_url
        time.sleep(2)
        self.driver.back()
        return url

    def clickSociology(self):
        self.elementClick(self._sociology_button,locatorType="xpath")

    def clickPsychology(self):
        self.elementClick(self._psychology_button,locatorType="xpath")

    def clickManagement(self):
        self.elementClick(self._management_button,locatorType="xpath")

    def clickEconomics(self):
        self.elementClick(self._economics_button,locatorType="xpath")

    def clickHumanResources(self):
        self.elementClick(self._humanresources_button,locatorType="xpath")

    def clickTechnology(self):
        self.elementClick(self._technology_button,locatorType="xpath")

    def clickEnterpreneurship(self):
        self.elementClick(self._enterpreneurship_button,locatorType="xpath")

    def clickInnovation(self):
        self.elementClick(self._innovation_button,locatorType="xpath")

    def clickMarketing(self):
        self.elementClick(self._marketing_button,locatorType="xpath")

    def clickLeadership(self):
        self.elementClick(self._leadership_button,locatorType="xpath")

    def verifyForwardTopic(self):
        return self.isElementPresent(self._forward_topic,locatorType="xpath")

    def forwardTopic(self):
        self.elementClick(self._forward_topic,locatorType="xpath")

    def verifyCard3Topic(self):
        return self.isElementPresent(self._card3_Topic,locatorType="xpath")

    def verifyCard2Topic(self):
        return self.isElementPresent(self._card2_Topic,locatorType="xpath")

    def hrefCard2Topic(self):
        href = self.getElement(self._card2_Topic, locatorType="xpath")
        href_card = href.get_attribute("href")
        return href_card

    def clickCard2Topic(self):
        time.sleep(2)
        self.elementClick(self._card2_Topic,locatorType="xpath")
        url = self.driver.current_url
        time.sleep(2)
        self.driver.back()
        return url


    def verifyCard1Topic(self):
        return self.isElementPresent(self._card1_Topic,locatorType="xpath")

    def verifyMainCardTopic(self):
        return self.isElementPresent(self._main_card_Topic,locatorType="xpath")

    def SS(self, message):
        self.screenShot(message)

    def verifyForwardGN(self):
        return self.isElementPresent(self._forward_GN, locatorType="xpath")

    def clickForwardGN(self):
        self.elementClick(self._forward_GN, locatorType="xpath")

    def clickOCLogo(self):
        self.elementClick(self._OC_dashboard, locatorType="xpath")
        return self.driver.current_url

    def verifyLogoUniversity(self):
        return self.isElementPresent(self._logo_university, locatorType="xpath")

    def verifyTextWelcome(self):
        return self.isElementPresent(self._welcome_text, locatorType="xpath")

    def verifyTourModal(self):
        return self.isElementPresent(self._modal_tour, locatorType="xpath")

    def clickSkipTour(self):
        self.elementClick(self._skip_tour,locatorType="xpath")

    def clickGotItTour(self):
        self.elementClick(self._gotit_tour,locatorType="xpath")

    def verifyMainCardDB(self):
        return self.isElementPresent(self._main_card_ls, locatorType="xpath")

    def verifyLSbuttonMainCard(self):
        return self.isElementPresent(self._card_ls_button, locatorType="xpath")

    def clickLearningSeriesButtonMain(self):
        self.elementClick(self._card_ls_button,locatorType="xpath")
        return self.driver.current_url

    def verifyAuxCardDB(self):
        return self.isElementPresent(self._aux_cards, locatorType="xpath")

    def verifyCheckSkillbuttonAux(self):
        return self.isElementPresent(self._check_skill_card_button, locatorType="xpath")

    def clickCheckSkillsbuttonAux(self):
        self.elementClick(self._check_skill_card_button, locatorType="xpath")
        return self.driver.current_url

    def verifyYouthActionbuttonAux(self):
        return self.isElementPresent(self._youth_action_card_button, locatorType="xpath")

    def clickYouthActionbuttonAux(self):
        self.elementClick(self._youth_action_card_button, locatorType="xpath")
        return self.driver.current_url

    def verifyPresentationChallengebuttonAux(self):
        return self.isElementPresent(self._presentation_challenge_card_button, locatorType="xpath")

    def clickPresentationChallengebuttonAux(self):
        self.elementClick(self._presentation_challenge_card_button, locatorType="xpath")
        return self.driver.current_url

    def verifyPickUpText(self):
        return self.isElementPresent(self._text_pickup, locatorType="xpath")

    def verifyPickUpCard(self):
        return self.isElementPresent(self._card1_pickup, locatorType="xpath")

    def verifyPickUpCardText(self):
        return self.getText(self._text_card1_pickup,locatorType="xpath")

    def clickPickUpContinueButton(self):
        self.elementClick(self._continue_button_card1_pickup, locatorType="xpath")

    def verifyContinuePickUpCard(self):
        return self.isElementPresent(self._continue_button_card1_pickup, locatorType="xpath")

    def scrollDown(self, cantity):
        self.webScroll(direction="down", pixels= cantity)

    def scrollUp(self, cantity):
        self.webScroll(direction="up", pixels= cantity)

    def verifyJobsBigCard(self):
        return self.isElementPresent(self._big_card_jobs_link, locatorType="xpath")

    def obtainHrefJobsBigCard(self):
        href = self.getElement(self._big_card_jobs_link, locatorType="xpath")
        url_jobs_main_card = href.get_attribute("href")
        return url_jobs_main_card

    def clickJobsBigCard(self):
        self.elementClick(self._big_card_jobs_link, locatorType="xpath")

    def urlJobsMainCard(self):
        return self.driver.current_url

    def verifyCard1Jobs(self):
        return self.isElementPresent(self._card1_jobs, locatorType="xpath")

    def clickCard1Jobs(self):
        parentHandle = self.driver.current_window_handle
        self.elementClick(self._card1_jobs, locatorType="xpath")
        handles = self.driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                url_new_tab = self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                return url_new_tab

    def obtainHrefJobsCard1(self):
        hrefJobs = self.getElement(self._card1_jobs, locatorType="xpath")
        url_jobs_card = hrefJobs.get_attribute("href")
        return url_jobs_card

    def urlJobsCard1(self):
        return self.driver.current_url

    def verifyCard2Jobs(self):
        return self.isElementPresent(self._card2_jobs, locatorType="xpath")

    def verifyCard3Jobs(self):
        return self.isElementPresent(self._card3_jobs, locatorType="xpath")

    def verifyCard4Jobs(self):
        return self.isElementPresent(self._card4_jobs, locatorType="xpath")

    def verifyBigCardFeaturedCollection(self):
        return self.isElementPresent(self. _big_card_talks_brazil, locatorType="xpath")

    def verifyCard1FeatureCollection(self):
        return self.isElementPresent(self._card1_talk_brazil, locatorType="xpath")

    def obtainHrefCard1FeatureCollection(self):
        href = self.getElement(self._card1_talk_brazil, locatorType="xpath")
        url_card1_feature_collection = href.get_attribute("href")
        return url_card1_feature_collection

    def clickCard1FeatureCollection(self):
        self.elementClick(self._card1_talk_brazil,locatorType="xpath")
        time.sleep(2)
        url= self.driver.current_url
        time.sleep(2)
        self.driver.back()
        return url

    def verifyCard2FeatureCollection(self):
        return self.isElementPresent(self._card2_talk_brazil, locatorType="xpath")

    def obtainHrefCard2FeatureCollection(self):
        href = self.getElement(self._card2_talk_brazil, locatorType="xpath")
        url_card2_feature_collection = href.get_attribute("href")
        return url_card2_feature_collection

    def clickCard2FeatureCollection(self):
        self.elementClick(self._card2_talk_brazil,locatorType="xpath")
        time.sleep(2)
        url= self.driver.current_url
        time.sleep(2)
        self.driver.back()
        return url

    def verifyForwardRowFeatureCollection(self):
        return self.isElementPresent(self._forward_button_slider, locatorType="xpath")

    def clickForwardFeatureCollection(self):
        self.elementClick(self._forward_button_slider,locatorType="xpath")

    def obtainHrefCard3FeatureCollection(self):
        href = self.getElement(self._card3_talk_brazil, locatorType="xpath")
        url_card3_feature_collection = href.get_attribute("href")
        return url_card3_feature_collection

    def clickCard3FeatureCollection(self):
        self.elementClick(self._card3_talk_brazil, locatorType="xpath")
        time.sleep(2)
        url = self.driver.current_url
        time.sleep(2)
        self.driver.back()
        return url

    def clickConnectButton(self):
        self.elementClick(self._connect_global_network,locatorType="xpath")

    def obtainhrefLearnMoreGN(self):
        href = self.getElement(self._learn_more_global_network, locatorType="xpath")
        url_learn_more = href.get_attribute("href")
        return url_learn_more

    def clickLearnMoreGN(self):
        self.elementClick(self._learn_more_global_network, locatorType="xpath")
        time.sleep(3)
        url_learn_more = self.driver.current_url
        return url_learn_more

    def goBack(self):
        self.driver.back()

    def clickFindConnections(self):
        self.elementClick(self._find_connections_button,locatorType="xpath")

    def verifySearchBox(self):
        return self.isElementPresent(self._search_find_connections, locatorType="xpath")

    def verifyTextConnect(self):
        return self.isElementDisplayed(self._connect_text,locatorType="xpath")

    def verifyTextConnected(self):
        return self.isElementDisplayed(self._connected_text, locatorType="xpath")

    def verifyMainCardLeadership(self):
        return self.isElementPresent(self._main_card_leadership, locatorType="xpath")

    def verifyCard1Leadership(self):
        return self.isElementPresent()
