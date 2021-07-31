import allure
import time
import sys

from allure_commons.types import AttachmentType
from allure_commons.reporter import AllureReporter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest

class CustomError(Exception):
	pass



@pytest.fixture(scope="class")
def webdriverRunner():
	global driver
	driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")

	driver.maximize_window()
	yield
	driver.close()
	driver.quit()

# from .steps import imported_step
@pytest.fixture()
def tst():
	print("Hello")

@pytest.mark.usefixtures("webdriverRunner")
class TestListAM:

	def setup(self):
		driver.get("https://www.list.am")
		self.__msgPASS = ""
		self.__msgFAIL = ""
		self.__errCount = 0

	def teardown(self):
		logger = AllureReporter()
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
	# @allure.severity("critical")
	def test_areShownHomePage(self):
		driver.find_element_by_id("lbar").click()

		v = driver.find_element_by_id("l").is_displayed()
		self.__report(v, "PASS: Logo is displayed", "FAIL: Logo isn't displayed")
		


		v = driver.find_element_by_id("ma").is_displayed()
		self.__report(v,
	          "PASS: 'My Account' is displayed", 
	          "FAIL: 'My Account' isn't displayed")
		


		v = driver.find_element_by_id("ap").is_displayed()
		self.__report(v,
	          "PASS: 'Post an Ad' is displayed", 
	          "FAIL: 'Post an Ad' isn't displayed")
		




	@allure.feature("list.am registration page")
	@allure.story("Story 2")
	def test_LoginButtonTextboxPassword(self):
		driver.find_element_by_id("ma").click()

		rgBtn = driver.find_elements_by_xpath("//*[@href='/register']")[0]
		print ("rgBtn.text: {0}".format(rgBtn.text))
		if rgBtn.text not in ["Գրանցում", "Регистрация", "Registration"]:
			# assert False, "Incorrect opened page. 'Registration' buttom doesn't exist"
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
	def test_radiobuttons(self):
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


		v = driver.find_element_by_id("idcmtype1").is_displayed()
		self.__report(v,
	          "PASS: 'Agency' radiobutton is displayed", 
	          "FAIL: 'Agency' radiobutton isn't displayed")
		

if __name__ == "__main__":
	pytest.main(["-v", "-s", "--alluredir", "res1"])
