import allure
import time
import sys

from allure_commons.types import AttachmentType
from allure_commons.reporter import AllureReporter

sys.path.insert(1, '../../SeleniumTest/Base')
# from base import *
from WebDriver    import WebDriver
from TestFixtures import TestFixtures

sys.path.insert(1, '../../SeleniumTest/Pages')
from homePage import HomePage

import pytest


class TestListAM(TestFixtures):
    def setup(self):
        self.__msgPASS = ""
        self.__msgFAIL = ""
        self.__errCount = 0

    def teardown(self):
        if self.__errCount != 0:
            c = self.__errCount
            self.__errCount = 0
            assert False, "There is/are {0} fail(s) in the test. Formore details see above report".format(c)
        else:
            assert True, "Test case passed"

    def __report(self, status, msgPass, msgErr):
        if status:
            st = "PASSED"
            msg = msgPass
        else:
            st = "FAILED"
            msg = msgErr
            self.__errCount += 1
        allure.attach(st,
                      name=msg,
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step
    def passing_step():
        pass

    def __errorNotification(self, count):
        allure.attach("Error",
                      name="FAILED: There are {0} asserts in the test. See report above".format(count),
                      attachment_type=allure.attachment_type.TEXT)

    @allure.feature("list.am HomePage")
    @allure.story("Story 1")
    def test_areShownHomePage(self, RunStopDriver):
        hp = HomePage()

        v = hp.isLogoDisplayed()
        self.__report(v, "PASS: Logo is displayed", "FAIL: Logo isn't displayed")

        v = hp.isMyAcountDisplayed()
        self.__report(v, "PASS: 'My Account' is displayed", "FAIL: 'My Account' isn't displayed")

        v = hp.isPostAdDisplayed()
        self.__report(v, "PASS: 'Post an Ad' is displayed", "FAIL: 'Post an Ad' isn't displayed")


    @allure.feature("list.am registration page")
    @allure.story("Story 2")
    @pytest.mark.usefixtures("RunStopDriver")
    def test_LoginButtonTextboxPassword(self):
        driver = WebDriver().getDriver()

        driver.find_element_by_id("ma").click()
        rgBtn = driver.find_elements_by_xpath("//*[@href='/register']")[0]

        if rgBtn.text not in ["Գրանցում", "Регистрация", "Registration"]:
            raise Exception("Incorrect opened page. 'Registration' buttom doesn't exist")

        v = driver.find_element_by_id("loginaction__form_action0").is_displayed()
        self.__report(v, "PASS: 'LogIn' button is displayed", "FAIL: 'LogIn' button isn't displayed")


        v = driver.find_element_by_id("_idyour_email").is_displayed()
        self.__report(v,
              "PASS: 'LogIn' testbox is displayed",
              "FAIL: 'LogIn' testbox isn't displayed")


        v = driver.find_element_by_id("loginaction__form_action0").is_displayed()
        self.__report(v,
              "PASS: 'Password' testbox is displayed",
              "FAIL: 'Password' testbox isn't displayed")


    @allure.feature("list.am 'Real Estate' page")
    @allure.story("Story 3")
    def test_radiobuttons(self, RunStopDriver):
        driver = WebDriver().getDriver()

        ps = driver.find_elements_by_xpath("//*[@data-c='54']")
        if ps[0].text in ["Անշարժ գույք", "Недвижимость", "Real Estate"] :
            ps[0].click()
        else:
            print("the name wasn't found" )
            raise Exception("'Real Estate' button doesn't exist")

        v = driver.find_element_by_class_name("off").is_displayed()
        self.__report(v,
              "PASS: 'Favorites' button is displayed",
              "FAIL: 'Favorites' button isn't displayed")


        v = driver.find_element_by_id("idcmtype0").is_displayed()
        self.__report(v,
              "PASS: 'Private' button is displayed",
              "FAIL: 'Private' button isn't displayed")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--alluredir", "../res1"])
