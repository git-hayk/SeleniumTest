from selenium import webdriver
import time


driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")
# driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")

# driver.get("https://www.google.com")
driver.get("https://www.list.am")



time.sleep(3)
driver.close()
