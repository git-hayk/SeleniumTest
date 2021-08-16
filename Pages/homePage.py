import sys

sys.path.insert(1, '../../SeleniumTest/Base')
# from base import WebDriver
from WebDriver import WebDriver

class HomePage():
    # def __init__(self, driver):
    def __init__(self):
        # self.__driver = driver

        self.__driver = WebDriver().getDriver()
        self.__logo_id = "l"
        self.__myAcount_id = "ma"
        self.__postAd_id = "ap"

    def isLogoDisplayed(self):
        return self.__driver.find_element_by_id(self.__logo_id).is_displayed()

    def isMyAcountDisplayed(self):
        return self.__driver.find_element_by_id(self.__myAcount_id).is_displayed()

    def isPostAdDisplayed(self):
        return self.__driver.find_element_by_id(self.__postAd_id).is_displayed()
