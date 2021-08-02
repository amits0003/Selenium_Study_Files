import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")
driver.get("https://www.sportsadda.com/")
driver.find_element_by_class_name('team-a').click()
time.sleep(5)
driver.find_element_by_xpath("//li[@data-si-tabs='match-info']/span[1]").click()

driver.close()