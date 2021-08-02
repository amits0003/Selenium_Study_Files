import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.maximize_window()

driver.find_element_by_id('autosuggest').send_keys('ind')

time.sleep(5)

list_country = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

print('length of country = ', len(list_country))

for country in list_country:
    #if country found is india then loop breaks out
    if country.text == 'India':
        country.click()
        break

print(driver.find_element_by_id('autosuggest').text)

assert driver.find_element_by_id('autosuggest').get_attribute('value') == "India"


#extract all the checkboxes in a single list so that it can be iterated in a for loop
driver.quit()