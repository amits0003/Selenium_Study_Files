
#extract all the checkboxes in a single list so that it can be iterated in a for loop


import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.maximize_window()
#//input[@type='']

radio_button_list = driver.find_elements_by_xpath("//input[@type='radio']")

print(len(radio_button_list))

radio_button_list[1].click()

assert radio_button_list[1].is_selected()


driver.quit()