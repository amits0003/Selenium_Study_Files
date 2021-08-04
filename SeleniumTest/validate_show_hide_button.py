from selenium import webdriver

from selenium.webdriver import ActionChains

# Chrome Driver Location
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.find_element_by_id("show-textbox").click()

assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_id("displayed-text").is_displayed()