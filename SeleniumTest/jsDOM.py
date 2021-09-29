from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name('name').send_keys('hello')
print(driver.find_element_by_name('name').text)
print(driver.find_element_by_name('name').get_attribute('value'))

value = driver.execute_script('return document.getElementsByName("name")[0].value')

shopbutton = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();" , shopbutton)

# Perform Scrolling operation using javascript
driver.execute_script("window. scrollTo(0,document.body.scrollHeight);")


assert value == 'hello'

