import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Creating a new empty List
list_veg = []
list_veg_at_page2 = []

driver = webdriver.Chrome(
    executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/seleniumPractise/')

# Search items
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
time.sleep(4)

# count number of items returned in the search
count_item = len(driver.find_elements_by_xpath("//div[@class='product']"))

# count number of buttons returned
#button_list = driver.find_elements_by_xpath("//div[@class='product-action']/button")

button_list = driver.find_elements_by_xpath("//div[@class='product-action']/button")

# selecting every button from the button list
for button in button_list:
    list_veg.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print('list of items added to the cart == ', list_veg)

# clicking the cart image icon
driver.find_element_by_css_selector("img[alt='Cart']").click()

# Clicking the proceed to checkout button
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

# explicit wait
# it explicitly wait till the object find the #promocode class name appears on the page
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

list_items = driver.find_elements_by_class_name('product-name')

for item in list_items:
    list_veg_at_page2.append(item.text)

print('list of items displayed at checkout page == ', list_veg_at_page2)

# validate
assert list_veg == list_veg_at_page2

# adding promo code
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')

original_amount = driver.find_element_by_xpath("//span[@class='totAmt']").text

# clicking in the button to apply promo code
driver.find_element_by_css_selector(".promoBtn").click()

# Explicit wait until the promo applied object appears
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'span.promoInfo')))

promo_Text = driver.find_element_by_css_selector("span.promoInfo").text

amount_after_discount = driver.find_element_by_xpath("//span[@class='discountAmt']").text

# comparing that the amount after discount is less than the original amount
print('original Amount = ', float(original_amount))
print('Amount after discount = ', float(amount_after_discount))

assert float(original_amount) > float(amount_after_discount)

print(promo_Text)

assert promo_Text == "Code applied ..!"

list_amount_product = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in list_amount_product:
    sum = sum+float(amount.text)


assert float(sum) == float(original_amount)

print('Total Amount by adding the individual prices of items', sum)

driver.quit()
