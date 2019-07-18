import os
from selenium import webdriver
import time
driverLocation = "..\\..\\drivers\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://onecampus.laureate.net/#/home")
time.sleep(2)
driver.save_screenshot("prueba phantom FF.png")
login = driver.find_element_by_xpath("/html//ui-view[@id='main-content']/home/div[@class='onecampus-homepage onecampus-view']//home-intro[@class='ng-isolate-scope']//div[@class='ng-scope']/div/div/p[3]/a[2]")
login.click()
time.sleep(2)
driver.save_screenshot("login FF.png")
time.sleep(2)
username = driver.find_element_by_id("Username")
username.send_keys("arlene.salgado@gmail.com")
time.sleep(2)
driver.save_screenshot("username FF.png")