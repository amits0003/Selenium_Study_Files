import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

'''Global Wait - Wait till 5 Seconds if the object is not displayed
if object displays at 1.5 seconds, it resumes the applcation
adding IMPLICIT WAIT
'''
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

'''
Diferent type of wait mechanish

1. implicit wait - driver.implicity_wait
advantages : 

when to use :
2. explicit wait
'''
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
#time.sleep(4)

count_item = len(driver.find_elements_by_xpath("//div[@class='product']"))

button_list = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(count_item)

for button in button_list:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

#adding promo code
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
promo_Text = driver.find_element_by_css_selector("span.promoInfo").text
print(promo_Text)
assert promo_Text == "Code applied ..!"

driver.quit()


