

from selenium import webdriver

validateText  = 'Amit'
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element_by_css_selector("#name").send_keys('Amit')
driver.find_element_by_id('confirmbtn').click()

alertObj = driver.switch_to.alert
alertText = alertObj.text
assert  validateText in alertText
print(alertObj.text)

#Positive Scenario  - clicking on accept / Ok Button
#alertObj.accept()

#Negetive Scenario - selct the cancel button
alertObj.dismiss()


driver.quit()

