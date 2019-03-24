
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Rikman/Documents/Devops/chromedriver.exe')


domain_file = open("C:\\Users\\Rikman\\Documents\\Devops\\domain_list.txt" , 'r', encoding='utf-8')

web_address = domain_file.read()

driver.get(web_address)

print

ttt


#driver.implicitly_wait(5)

#Show the list of Dropdown Price Point.  Make is visible
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[0].click()

#Choose a price for gift
price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[3].click()

#Show the list of Area. Make is visible
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[1].click()

#Choose an area from the list
price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[3].click()

#Show category list - make it visible
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[2].click()

#Choose category from the list
price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[2].click()



#Search gifts
my_submit2 = driver.find_element_by_class_name("ui-btn")
my_submit2.click()

#Choosing the business
business1 = driver.find_elements_by_class_name("supplier-logo")
business1[1].click()

#Enter price for Gift card
from selenium.webdriver.common.keys import Keys

money1 = driver.find_element_by_xpath("//input[@type='tel']")
money1.send_keys("200")

money1 = driver.find_element_by_xpath("//input[@type='tel']")
money1.send_keys(Keys.ENTER)

#Press Radio button for someone else


# Enter Receiver name
who = driver.find_elements_by_class_name("ui-input")
who[0].send_keys("אבא")
# Enter sender name
who[2].send_keys("עינת")

#Enter Blessings
blessings = driver.find_element_by_class_name("ui-textarea")
blessings.send_keys("מזל טוב אבא! תהנה מהמתנה :)")

# Pick the event
price_point = driver.find_elements_by_class_name("chosen-single")
price_point[10].click()

price_point2 = driver.find_elements_by_class_name("active-result")
price_point2[3].click()

#Upload a picture
driver.find_element_by_name("fileUpload").send_keys('C://Users/Einat/Pictures/2.jpg')

#Send by mail l
driver.find_element_by_class_name('icon-envelope').click()

#Email info
driver.find_element_by_class_name('inpnut-mail').send_keys("einat@gmail.com")
driver.find_element_by_class_name('input-mail').send_keys(Keys.ENTER)

#Final gift Submit
driver.find_element_by_class_name('shubmit-wrapper').click()

#Close Window
#driver.close()