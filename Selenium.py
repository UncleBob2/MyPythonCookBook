#Controlling the Browser with the Selenium Module
from selenium import webdriver
import time
browser = webdriver.Firefox()
#browser.get('https://automatetheboringstuff.com')
# elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
# elem.click()

browser.get('https://en.wikipedia.org/wiki/Wiki')
searchElemen = browser.find_element_by_css_selector('#searchInput')
searchElemen.send_keys('zombie')
searchElemen.submit()
browser.back()
browser.forward()
browser.refresh()
time.sleep(5.5)
browser.quit()



# type(browser)
# <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
# browser.get('http://inventwithpython.com')
#
# browser.find_element_by_class_name(name)

# browser.find_element_by_id(id)
# browser.find_element_by_link_text(text)
# browser.find_element_by_partial_link_text(text)
# browser.find_element_by_name(name)
# browser.find_element_by_tag_name(name)
# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# try:
# elem = browser.find_element_by_class_name('bookcover')
# print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
# print('Was not able to find an element with that name.')
# >>>emailElem = browser.find_element_by_id('login-username')
# emailElem.send_keys('not_my_real_email')
# passwordElem = browser.find_element_by_id('login-passwd')
# 260 Chapter 11
# passwordElem.send_keys('12345')
# passwordElem.submit()
# browser.back() Clicks the Back button.
# browser.forward() Clicks the Forward button.
# browser.refresh() Clicks the Refresh/Reload button.
# browser.quit() Clicks the Close Window button.
# 1)	cmd window, type py
# 2)	Import pyautogui
# 3)	Pyautogui.displayMousePosition()
# Python in cmd
# message = ''' I'm thinking
# ... of “thai food”
# ... '''
