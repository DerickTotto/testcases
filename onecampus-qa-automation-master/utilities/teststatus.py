"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
from Testrail.testrail import APIClient
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

testrail = os.getenv('APIClient')
testrail_user = os.getenv('user')
testrail_password = os.getenv('password')


class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)
    client = APIClient(testrail)
    client.user = testrail_user
    client.password = testrail_password

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage, testRun):
        if result is True:
            self.client.send_post('add_result/' + testRun, {'status_id': '1', 'comment': resultMessage + ' Passed'})
            self.resultList.append("PASS")
            self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
            print(self.resultList)
        else:
            self.client.send_post('add_result/' + testRun, {'status_id': '5', 'comment': resultMessage + ' Failed'})
            self.resultList.append("FAIL")
            self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
            print(self.resultList)

    def mark(self, result, resultMessage, testRun):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage, testRun)

    def markFinal(self, testName, result, resultMessage, testRun):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage, testRun)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
