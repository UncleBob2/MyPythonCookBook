from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.python.org/")
try:
    elem = browser.find_element_by_link_text('#top > nav > ul > li.jobs-meta > a  ')
    print('Found <%s> element with that class name!' % (elem.tag_name))
    type(elem)
    time.sleep(5)
    elem.click()
except:
    print('Was not able to find an element with that name.')
