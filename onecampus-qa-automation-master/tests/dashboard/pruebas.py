import os
from selenium import webdriver
import time
from pages.home.dashboard_page import DashboardPage
# OC Logo Direct to dashboard
_OC_dashboard = "/html//oc-root//oc-header//one-header//a[@href='/#/dashboard']/img"
# University Logo
_logo_university = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__logo']"
_welcome_text = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__hdg']"
# Tour
_skip_tour = "/html//oc-root/div/div/div[@class='ng-scope']//one-tour[@class='ng-isolate-scope']/div/div[1]/div[@class='one-infotip']//a[@href='']"
_gotit_tour = "/html//oc-root/div/div[@class='main']/div[@class='ng-scope']//one-tour[@class='ng-isolate-scope']//div[@class='one-tour__step one-tour__step--centered']//div[@class='one-infotip__footer']/button[2]"
# Dashboard 4 cards
_main_card_ls = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__main-card']"
_card_ls_button = "//div[@class='one-feature-grid__main-card']/one-feature-card[@class='ng-isolate-scope']/div//one-feature-card-action[@type='button']/button[@type='button']"
_aux_cards = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__aux-cards']"
_check_skill_card_button ="//*[@id='dashboard-onecampus-container']/dashboard-features/div/div/div[4]/div[1]/one-feature-card/div/div/one-feature-card-action/button"
_youth_action_card_button = "//*[@id='dashboard-onecampus-container']/dashboard-features/div/div/div[4]/div[2]/one-feature-card/div/div/one-feature-card-action/button"
_presentation_challenge_card_button = "//*[@id='dashboard-onecampus-container']/dashboard-features/div/div/div[4]/div[3]/one-feature-card/div/div/one-feature-card-action/button"
# Pick up where you left
_text_pickup = "//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//current-courses//div[.='Pick up where you left off']"
_card1_pickup = "//current-courses//one-scrollgrid[@class='ng-isolate-scope']//one-scrollgrid-row//one-scrollgrid-item/div[@class='one-scrollgrid__item']"
_text_card1_pickup = "//current-courses//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]//episode-status//h4"
_continue_button_card1_pickup = "//current-courses//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row//one-scrollgrid-item//episode-status//div[@class='one-summary-tile--content']/a"
# Jobs of the future
_big_card = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[1]/div/div[2]/div[3]/a"
_card1 = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[1]/div/one-scrollgrid-item[1]/div/episode-status/div/div[2]/a"
_card2 = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[1]/div/one-scrollgrid-item[2]/div/episode-status/div/div[2]/a"
_card3 = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[2]/div/one-scrollgrid-item[1]/div/episode-status/div/div[2]/a"
_card4 = "//*[@id='dashboard-onecampus-container']/featured-learning-series/div/div/div[3]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row[2]/div/one-scrollgrid-item[2]/div/episode-status/div/div[2]/a"
# Laureate talks Brazil
_back_button_slider = "/html//div[@id='dashboard-onecampus-container']/feature-section/div//one-scrollgrid[@class='ng-isolate-scope']/div[@class='one-scrollgrid__controls']/button[1]"
_forward_button_slider = "/html//div[@id='dashboard-onecampus-container']/feature-section/div//one-scrollgrid[@class='ng-isolate-scope']/div[@class='one-scrollgrid__controls']/button[2]"
_big_card_talks_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//div[@class='one-feature-section__main']"
_card1_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]/div[@class='one-scrollgrid__item']/one-flexcard//a"
#_card2_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[2]/div[@class='one-scrollgrid__item']/one-flexcard//a"
_card2_talk_brazil = "//*[@id='dashboard-onecampus-container']/feature-section/div/div/div[2]/div/div[2]/one-scrollgrid/div[1]/div/one-scrollgrid-row/div/one-scrollgrid-item[2]/div/one-flexcard/div/div[3]/a"
_alternate_card2_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[2]/div[@class='one-scrollgrid__item']/one-flexcard//a"
_card3_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[3]/div[@class='one-scrollgrid__item']/one-flexcard//a"
_card4_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[4]/div[@class='one-scrollgrid__item']/one-flexcard//a"
_card5_talk_brazil = "/html//div[@id='dashboard-onecampus-container']/feature-section//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[5]/div[@class='one-scrollgrid__item']/one-flexcard//a"
# Find Connections
_find_connections_button = "/html//div[@id='dashboard-onecampus-container']/global-network[@class='ng-isolate-scope']//a[.='Find Connections']"
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
# marketing
_card1_marketing = ""
_card2_marketing = ""
_card3_marketing = ""
# leadership
_card1_leadership = "/html//div[@id='dashboard-onecampus-container']//one-scrollgrid[@class='ng-isolate-scope one-scrollgrid--animated']//div[@class='one-scrollgrid__items one-scrollgrid__items--rows']/one-scrollgrid-row/div/one-scrollgrid-item[1]/div[@class='one-scrollgrid__item']/one-flexcard//a"
_card2_leadership = ""
_card3_leadership = ""
# innovation
_card1_innovation = ""
_card2_innovation = ""
_card3_innovation = ""
# enterpreneurship
_card1_enterpreneurship = ""
_card2_enterpreneurship = ""
_card3_enterpreneurship = ""
# technology
_card1_technology = ""
_card2_technology = ""
_card3_technology = ""
# human resources
_card1_humanresources = ""
_card2_humanresources = ""
_card3_humanresources = ""
# economics
_card1_economics = ""
_card2_economics = ""
_card3_economics = ""
# management
_card1_management = ""
_card2_management = ""
_card3_management = ""
# psychology
_card1_psychology = ""
_card2_psychology = ""
_card3_psychology = ""
# sociology
_card1_sociology = ""
_card2_sociology = ""
_card3_sociology = ""
# dictionary of learning series
dict_url = {
    "https://onecampus.laureate.net/#/redirectLogin":"https://exchange.laureate.net/IdentityProvider/Login"
}
driverLocation = "..\\..\\drivers\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.maximize_window()
driver.get("https://onecampus.laureate.net/#/home")
time.sleep(3)
login = driver.find_element_by_xpath("/html//ui-view[@id='main-content']/home/div[@class='onecampus-homepage onecampus-view']//home-intro[@class='ng-isolate-scope']//div[@class='ng-scope']/div/div/p[3]/a[2]")
login_key_url = login.get_attribute("href")
print(login_key_url)
login.click()
time.sleep(3)
login_value_url = driver.current_url
print(login_value_url)
if dict_url[login_key_url] == login_value_url:
    print("la redirrecion fue correcta")
time.sleep(3)