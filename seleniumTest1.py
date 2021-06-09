from selenium import webdriver
import time

def firstExmple():
	driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
	driver.get("https://www.list.am")
	time.sleep(3)
	driver.close()


def p1(driver):
	print ("Begin: proc1")
	driver.find_element_by_id("lbar").click()
	logo = driver.find_element_by_id("l")
	print ("logo displayed: " + str(logo.is_displayed()))

	ma = driver.find_element_by_id("ma")
	print ("'my account' displayed: " + str(ma.is_displayed()))

	pa = driver.find_element_by_id("ap")
	print ("'post an ad' displayed: " + str(pa.is_displayed()))

	print ("End: Proc1")
	print ("")
	print ("")


def p2(driver):
	print ("Begin: proc2")
	driver.find_element_by_id("ma").click()

	login = driver.find_element_by_id("loginaction__form_action0")
	print (" Button 'LogIn' displayed: " + str(login.is_displayed()))

	email = driver.find_element_by_id("_idyour_email")
	print (" Textbox 'LogIn' displayed: " + str(email.is_displayed()))

	passw = driver.find_element_by_id("loginaction__form_action0")
	print (" Textbox 'Password' displayed: " + str(passw.is_displayed()))

	driver.back()
	print ("End: Proc2")
	print ("")
	print ("")


def p3(driver):
	print ("Begin: proc3")
	ps = driver.find_elements_by_xpath("//*[@data-c='54']")
	for p in ps:
		if p.text in ["Անշարժ գույք", "Недвижимость", "Real Estate"] :
			p.click()
		else:
			print("the name wasn't found" )
			return

	like = driver.find_element_by_class_name("off")
	print ("Button 'favorites' displayed: " + str(like.is_displayed()))

	l1 = driver.find_element_by_id("idcmtype0")
	print (" radio button 'private' displayed: " + str(l1.is_displayed()))

	l2 = driver.find_element_by_id("idcmtype1")
	print (" radio button 'agency' displayed: " + str(l2.is_displayed()))


	print ("End: Proc3")
	print ("")
	print ("")



if __name__ == "__main__":
	driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
	driver.get("https://www.list.am")
	driver.maximize_window()
	p1(driver)
	p2(driver)
	p3(driver)

	time.sleep(10)
	driver.close()

#	1. open without sign in
#		check existeness of some elements
#	2. my page (do appropriate elements exist?)
#		check existeness of some elements
#	3. eneter (ansharj guyq) 
#		(do appropriate elements exist?)
# click on the link and check 