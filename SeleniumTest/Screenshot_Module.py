from selenium import webdriver

from PIL import Image

from screenshots import *

driver = webdriver.Chrome(
    executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.save_screenshot('abc.jpg')

screenshot = Image.open('abc.jpg')

screenshot.show()

driver.quit()