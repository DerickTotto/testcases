"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://onecampus.laureate.net/#/home"
        if self.browser == "iexplorer":
            # Set ie driver
            driverLocation = "..\\..\\drivers\\headless_ie_selenium.exe"
            os.environ["webdriver.ie.driver"] = driverLocation
            driver = webdriver.Ie(driverLocation)
        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driverLocation = "..\\drivers\\geckodriver.exe"
            os.environ["webdriver.firefox.driver"] = driverLocation
            driver = webdriver.Firefox(options=options)
        elif self.browser == "chrome":
            # Set chrome driver
            #chromedriver = "/Users/atomar/Documents/workspace_personal/selenium/chromedriver"
            #os.environ["webdriver.chrome.driver"] = chromedriver
            #driver = webdriver.Chrome(chromedriver)
            #driver.set_window_size(1440, 900)

            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            # options.binary_location = "..\\drivers\\chromedriver"
            driver = webdriver.Chrome()
        else:
            driverLocation = "..\\..\\drivers\\chromedriver.exe"
            os.environ["webdriver.ie.driver"] = driverLocation
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = webdriver.Chrome(driverLocation, options=options)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
