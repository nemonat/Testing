#1
#a
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Rikman/Documents/Devops/chromedriver.exe')

#driver.get("https://www.walla.co.il/")

#driver = webdriver.Firefox('C:\\Users\\Rikman\\Documents\\Devops\\geckodriver.exe')

driver.get("https://www.ynet.co.il/")
#
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get('http://google.com')
# print driver.title
# driver.quit()
#
# #2
title = driver.title
print(title)
driver.refresh()

if title == driver.title:
    print ("same")

#3
#yes

#4
driver.get("https://translate.google.com/")
driver.find_element_by_id("source").send_keys("עינת")

# #5
driver.get("https://www.youtube.com/")
driver.find_element_by_id("search").send_keys("באסה סבבה")
mysong = driver.find_element_by_id("search-icon-legacy")
mysong.click()

# #6
driver.get("https://translate.google.com/")
driver.find_element_by_id("source").send_keys("hello")
driver.find_element_by_class_name("orig").send_keys("hello")
driver.find_element_by_xpath("//*[@id='source']").send_keys("hello")

#7
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("1@1.com")
driver.find_element_by_id("pass").send_keys("1234")
mylogin = driver.find_element_by_xpath("//input[@type='submit']").click()