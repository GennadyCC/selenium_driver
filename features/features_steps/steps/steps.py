# from time import time, sleep
import time
import sys
from selenium import webdriver

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.get('https://skryabin.com/webdriver/html/sample.html')
# time.sleep(5)
element = driver.find_element_by_xpath("//label[@class='required']").text
print(element)

element = driver.find_element_by_xpath("//label[contains(text(),'Country of Origin')]").text
print(element)

element = driver.find_element_by_xpath("//input[@name='confirmPassword'][@disabled='']").text
print(element)
time.sleep(1)

element = driver.find_element_by_xpath("//select[@name='carMake']/option[@value='Toyota']").click()
time.sleep(1)

element = driver.find_element_by_xpath("//select[@name='countryOfOrigin']/option[@value='Canada']").text
print(element)
driver.find_element_by_xpath("//select[@name='countryOfOrigin']").click()

time.sleep(1)
driver.find_element_by_xpath("//select[@name='countryOfOrigin']/option[@value='Canada']").click()

time.sleep(1)
for x in range(3):
    driver.find_element_by_xpath("//input[@name='gender'][contains(@value,'female')]").click()
    time.sleep(0.2)
    driver.find_element_by_xpath("//input[@name='gender'][contains(@value,'male')]").click()
    time.sleep(0.2)

element = driver.find_element_by_xpath("//label[contains(text(),'Phone Number')]")
print(element)
driver.find_element_by_xpath("//label[contains(text(),'Phone Number')]/../input[@name='phone']").click()
driver.find_element_by_xpath("//label[contains(text(),'Phone Number')]/../input[@name='phone']").send_keys('303-321-21-21')
time.sleep(1)

driver.find_element_by_xpath("//input[@id='name']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='firstName']").send_keys('Ivan')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='middleName']").send_keys('IvaNovich')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='lastName']").send_keys('IvanoV')
time.sleep(2)
driver.find_element_by_xpath("//span[@class='ui-button-text'][contains(text(),'Save')]").click()
time.sleep(1)

element = driver.find_element_by_xpath("//label//*[contains(text(),'I have read and accept Privacy Policy')]").text
print(element)

driver.find_element_by_xpath("//input[@ng-model='formData.username']").send_keys('TestName')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='password']").send_keys('123')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='confirmPassword']").click()

time.sleep(1)

element = driver.find_element_by_xpath("//label[text()='Please enter at least 5 characters.']")
print(element)

driver.find_element_by_xpath("//button[text()='Related documents (click)']").click()
time.sleep(1)
# driver.switch_to.window('Sample Page')
time.sleep(1)

print("done")