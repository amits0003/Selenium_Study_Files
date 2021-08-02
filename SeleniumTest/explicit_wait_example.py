import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/seleniumPractise/')

'''
Diferent type of wait mechanish

2. explicit wait 
explicitly targeting only for any specific object
'''
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
time.sleep(4)

count_item = len(driver.find_elements_by_xpath("//div[@class='product']"))

button_list = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(count_item)

for button in button_list:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
#explicit wait
# it explicitly wait till the object find the #promocode class name appears on the page
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
#adding promo code
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'span.promoInfo')))
promo_Text = driver.find_element_by_css_selector("span.promoInfo").text
print(promo_Text)
assert promo_Text == "Code applied ..!"

driver.quit()


