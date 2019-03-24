# A.
# Enter the website

from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Rikman/Documents/Devops/chromedriver.exe')

driver.get("https://buyme.co.il/")

# Enter הרשמה
subscribe = driver.find_element_by_class_name("seperator-link")
subscribe.click()

# Press button "להרשמה"
subscribe2 = driver.find_element_by_class_name("text-btn")
subscribe2.click()

# Enter 1st name
my_name = driver.find_element_by_xpath("//input[@type='text']")
my_name.send_keys("עינת")



# Enter email address
my_email = driver.find_element_by_xpath("//input[@type='email']")
my_email.send_keys("222@22.com")

# Enter Password
my_password = driver.find_element_by_xpath("//input[@type='password']")
my_password.send_keys("Hello1qaz")

# Enter Password 2nd time
my_password = driver.find_element_by_id("ember1025")
my_password.send_keys("Hello1qaz")

# Press "אני מסכים" using script for none-interactible elements +
driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("fa-check"))

# Import Keys
from selenium.webdriver.common.keys import Keys

# Press "הרשמה"
my_submit = driver.find_element_by_class_name('ui-btn')
my_submit.send_keys(Keys.ENTER)

# Allow Page to Load
import time

time.sleep(5)
driver.implicitly_wait(5)

# B.
# Show the list of Dropdown Price Point.  Make is visible
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[0].click()

# Choose a price for gift
price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[3].click()

# Show the list of Area. Make is visible
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[1].click()

# Choose an area from the list
price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[3].click()

# Show category list - make it visible
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[2].click()

# Choose category from the list
price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[2].click()

# Search gifts
my_submit2 = driver.find_element_by_class_name("ui-btn")
my_submit2.click()

# C.
# Choosing the business
business1 = driver.find_elements_by_class_name("supplier-logo")
business1[1].click()

# Enter price for Gift card
from selenium.webdriver.common.keys import Keys

money1 = driver.find_element_by_xpath("//input[@type='tel']")
money1.send_keys("200")

money1 = driver.find_element_by_xpath("//input[@type='tel']")
money1.send_keys(Keys.ENTER)

# D.
# Press Radio button for someone else
driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("circle"))

# Enter Receiver name
who = driver.find_elements_by_class_name("ui-input")
who[0].send_keys("אבא")
# Enter sender name
who[1].send_keys("עינת")

# Enter Blessings
blessings = driver.find_element_by_class_name("ui-textarea")
blessings.send_keys("מזל טוב אבא! תהנה מהמתנה :)")

# Pick the event
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[6].click()

event = driver.find_elements_by_class_name("active-result")
event[2].click()

# Upload a picture
driver.find_element_by_name("fileUpload").send_keys('C://Users/Einat/Pictures/2.jpg')

# Send by mail
driver.find_element_by_class_name('icon-envelope').click()

# Email info
driver.find_element_by_class_name('input-mail').send_keys("einat@gmail.com")
driver.find_element_by_class_name('input-mail').send_keys(Keys.ENTER)

# Final gift Submit
driver.find_element_by_class_name('submit-wrapper').click()

# Close Window
driver.close()
