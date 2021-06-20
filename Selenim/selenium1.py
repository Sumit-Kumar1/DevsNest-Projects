#-------------------------steps to perform----------------------------------------
# 1. Import webdirver from selenium
# 2. Open Firefox browser or any browser (must have related webdriver).
# 3. Maximize the window
# 4. Navigate to google homepage.
# 5. Identify the Google Search test box and pass the value linkedin.
# 6. Click on google search button 
# 7. Close the browser
#------------------------------------------------------------------------------------


#---------IMPORTING  LIBRARIES---------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.maximize_window()
link = "https://www.linkedin.com/home"
browser.get(link)
# assert "MytitleCustom" in browswer.title

#------click on sign in button:-------
browser.find_element_by_class_name("nav__button-secondary").click()
#-------------------

#--------- on next page filling in username and password and then click on login.-----
browser.find_element_by_id("username").send_keys("Kumarsumitjat298@gmail.com")
browser.find_element_by_id("password").send_keys("Madhu@7796")
    #browser.set_window_size(1280, 720)
browser.find_element_by_class_name("btn__primary--large.from__button--floating").click()
#----------------------------------------------

#------------ go to my network link--------------
browser.find_element_by_id("ember21").click()
#------------------------------------------------

#---------- wait for some time ------------------
browser.implicitly_wait(10) # in seconds

browser.close()
