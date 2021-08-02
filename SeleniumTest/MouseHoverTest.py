
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# Chrome Driver Location
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

''' Create the action object'''
actionObj = ActionChains(driver)

menu = driver.find_element_by_id("mousehover")

# Invoking the action Object here
actionObj.move_to_element(menu).perform()

childMenu = driver.find_element_by_link_text('Top')

# Invoking the Child element so that it goes to the hovered link
actionObj.move_to_element(childMenu).perform()

driver.quit()