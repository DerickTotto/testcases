import time
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "/html//ui-view[@id='main-content']/home/div[@class='onecampus-homepage onecampus-view']//home-intro[@class='ng-isolate-scope']//div[@class='ng-scope']/div/div/p[3]/a[2]"
    _username_field = "Username"
    _password_field = "//input[@id='Password']"
    _submit_button = "//button[@type='submit']"
    _another_user ="//a[@href='/IdentityProvider/Login']"
    _lenguaje_dropdown = "/html//select[@id='Language']"
    _spanish_button = "//select[@id='Language']/option[@value='es']"
    _portuguese_button = "//select[@id='Language']/option[@value='pt']"
    _english_button = "//select[@id='Language']/option[@value='en']"
    _terms_conditions_anchor = "a"
    _trouble_loggin_button = "button-support"
    _office_username = "i0116"
    _office_nextButton = "idSIButton9"
    _office_password = "i0118"
    _office_noButton = "idBtn_Back"
    _university_logo = "/html/body/div/form/img"

    def verifyLogoUniversity(self):
        return self.isElementPresent(self._university_logo, locatorType="xpath")

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterUsername(self, email="test"):
        self.sendKeys(email, self._username_field)

    def enterOfficeUsername(self, officeEmail):
        self.sendKeys(officeEmail, self._office_username)

    def clickNextOffice(self):
        self.elementClick(self._office_nextButton)

    def clickOfficeNOButton(self):
        self.elementClick(self._office_noButton)

    def enterOfficePassword(self, officePassword):
        self.sendKeys(officePassword, self._office_password)

    def enterPassword(self, password="test"):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickSubmitButton(self):
        self.elementClick(self._submit_button, locatorType="xpath")

    def clickAnotherUser(self):
        self.elementClick(self._another_user, locatorType="xpath")

    def login(self, username="test", password="test"):
        time.sleep(1)
        self.enterUsername(username)
        time.sleep(1)
        self.clickSubmitButton()
        time.sleep(1)
        self.enterPassword(password)
        time.sleep(1)
        self.clickSubmitButton()
        time.sleep(1)

    def verifyUsername(self):
        return self.isElementPresent(locator=self._username_field, locatorType="id")

    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__hdg']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//div[@id='dashboard-onecampus-container']/dashboard-features[@class='ng-isolate-scope']//div[@class='one-feature-grid__hdg']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def logout(self):
        #self.nav.navigateToUserSettings()
        time.sleep(1)
        logoutLinkElement = self.waitForElement(locator="/html//oc-root//oc-header//one-header//one-user-menu//button[@title='Toggle user menu']",
                          locatorType="xpath", pollFrequency=2)
        self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="/html//oc-root//oc-header//one-header//one-user-menu//nav/div/ul[3]//a[@href='/logout']/span[.='Log Out']",
                          locatorType="xpath")

    def usernameError(self):
        return self.isElementPresent("//span[@class='field-validation-error']", locatorType="xpath")
    
    def passwordError(self):
        return self.isElementPresent("//ul/li", locatorType="xpath")
    
    def clearUsername(self):
        usernameField = self.getElement(locator=self._username_field)
        usernameField.clear()

    def lenguageSpanish(self):
        # Change the lenguage to Spanish
        time.sleep(3)
        self.elementClick(self._lenguaje_dropdown, locatorType="xpath")
        self.elementClick(self._spanish_button, locatorType="xpath")
        time.sleep(1)

    def verifySpanish(self):
        return  self.isElementPresent("//p[contains(text(), 'Por favor utilice su usuario para continuar')]", locatorType="xpath")

    def lenguagePortuguese(self):
        # Change the lenguage to Portuguese
        time.sleep(3)
        self.elementClick(self._lenguaje_dropdown, locatorType="xpath")
        self.elementClick(self._portuguese_button, locatorType="xpath")
        time.sleep(1)

    def verifyPortuguese(self):
        return  self.isElementPresent("//p[contains(text(), 'Por favor, digite seu nome de usuário para continuar')]", locatorType="xpath")

    def lenguageEnglish(self):
        # Change the lenguage to Portuguese
        time.sleep(3)
        self.elementClick(self._lenguaje_dropdown, locatorType="xpath")
        self.elementClick(self._english_button, locatorType="xpath")
        time.sleep(1)

    def verifyEnglish(self):
        return  self.isElementPresent("//p[contains(text(), 'Please enter your username to continue')]", locatorType="xpath")

    def termsUS(self):
        parentHandle = self.driver.current_window_handle
        self.lenguageEnglish()
        self.elementClick(self._terms_conditions_anchor, locatorType="css")
        handles = self.driver.window_handles
        # Change to the new tab
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                terms = self.driver.current_url
                time.sleep(2)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(parentHandle)
                return terms

    def verifyTermsUS(self, terms):
        if terms == "https://exchange.laureate.net/Content/TermsAndConditions.html":
            return True

    def termsES(self):
        parentHandle = self.driver.current_window_handle
        self.lenguageSpanish()
        self.elementClick(self._terms_conditions_anchor, locatorType="css")
        handles = self.driver.window_handles
        # Change to the new tab
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                terms = self.driver.current_url
                time.sleep(1)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(parentHandle)
                return terms

    def verifyTermsES(self, terms):
        if terms == "https://exchange.laureate.net/Content/TermsAndConditions-es.html":
            return True

    def termsPT(self):
        parentHandle = self.driver.current_window_handle
        self.lenguagePortuguese()
        self.elementClick(self._terms_conditions_anchor, locatorType="css")
        handles = self.driver.window_handles
        # Change to the new tab
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                terms = self.driver.current_url
                time.sleep(1)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(parentHandle)
                return terms

    def verifyTermsPT(self, terms):
        if terms == "https://exchange.laureate.net/Content/TermsAndConditions-pt.html":
            return True

    def problemsUS(self):
        parentHandle = self.driver.current_window_handle
        self.lenguageEnglish()
        self.elementClick(self._trouble_loggin_button)
        handles = self.driver.window_handles
        # change to the new tab
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                problems = self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                return problems

    def verifyProblemsUS(self, problems):
        if problems == "https://laureatesupport.zendesk.com/hc/en-us/categories/360000042568-OneCampus-by-Laureate":
            return True

    def problemsPT(self):
        parentHandle = self.driver.current_window_handle
        self.lenguagePortuguese()
        self.elementClick(self._trouble_loggin_button)
        handles = self.driver.window_handles
        # change to the new tab
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                problems = self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                return problems

    def verifyProblemsPT(self, problems):
        if problems == "https://laureatesupport.zendesk.com/hc/pt-br/categories/360000042568-OneCampus-by-Laureate":
            return True

    def problemsES(self):
        parentHandle = self.driver.current_window_handle
        self.lenguageSpanish()
        self.elementClick(self._trouble_loggin_button)
        handles = self.driver.window_handles
        # change to the new tab
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                problems = self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(parentHandle)
                return problems

    def verifyProblemsES(self, problems):
        if problems == "https://laureatesupport.zendesk.com/hc/es/categories/360000042568-OneCampus-by-Laureate":
            return True

    def TomarSS(self, message):
        self.screenShot(message)