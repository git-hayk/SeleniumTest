from selenium import webdriver

class WebDriver:
	__driver = None
	@staticmethod
	def createDriver():
		WebDriver.__driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
		WebDriver.__driver.get("https://www.list.am")
		WebDriver.__driver.maximize_window()

	@staticmethod
	def getDriver():
		return WebDriver.__driver

	@staticmethod
	def closeDriver():
		WebDriver.__driver.close()
		WebDriver.__driver.quit()