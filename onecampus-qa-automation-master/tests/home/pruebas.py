import os
from selenium import webdriver
import time
"""
cur_path = os.path.dirname(__file__)
new_path = os.path.relpath("..\\..\\drivers\\phantomjs.exe", cur_path)
os.environ["webdriver.chrome.driver"] = new_path
driver = webdriver.PhantomJS(new_path)
driver.get("https://www.google.com/")
driver.save_screenshot("prueba phantom.png")

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
"""
driverLocation = "..\\..\\drivers\\headless_ie_selenium.exe"
os.environ["webdriver.ie.driver"] = driverLocation
driver = webdriver.Ie(driverLocation)


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