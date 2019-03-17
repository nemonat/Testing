from selenium import webdriver

from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Rikman/Documents/Devops/chromedriver.exe')
driver.implicity_wait(10)

driver.get("https://translate.google.com/")

#Prints the url we chose before
print(driver.current_url)

#מדפיס את שם הטאב כמו "הורדו"
print(driver.title)

print(driver.page_source)

#close closes the current tab
#driver.quit quit the session שלא יהיו זליגות של זכרון
#driver.close();
#driver.quit();

my_list = driver.find_elements_by_id("source")
#print(len(my_list))
#my_list(2).click()
#x = my_list[30]

my_list = driver.find_elements_by_class_name("")

#driver.find_element_by_xpath("//textarea[@id-'source']")

#locator הכי אמין
#locator שמשתנה הכי פחות

#driver.find_element_by_id("source").click()



driver.find_element_by_id("source").send_keys("hello")

import time

print("hello")
time.sleep(5)
print("world")

from selenium.webdriver.common.keys import keys
driver.find_element(By.id.value="123").send_keys(keys.ENTER)

driver.excute_script)
