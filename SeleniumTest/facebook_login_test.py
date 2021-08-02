#Facebook Login Page Test
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://en-gb.facebook.com/reg/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjI3Mjk5OTY5LCJjYWxsc2l0ZV9pZCI6MzYzOTY5MDQ0ODc4OTI4fQ%3D%3D')
#driver.get('www.facebook.abcd')

driver.find_element_by_name('firstname').send_keys('Amit')
driver.find_element_by_name('lastname').send_keys('Kumar')
driver.find_element_by_css_selector('Input[name="reg_email__"]').send_keys('amit@gmail.com')

driver.find_element_by_css_selector('Input[name="reg_email_confirmation__"]').send_keys('amit@gmail.com')
driver.find_element_by_css_selector('Input[name="reg_passwd__"]').send_keys('amit@gmail.com')

driver.find_element_by_name('sex').click()

driver.find_element_by_name("birthday_day").send_keys('5')
driver.find_element_by_name("birthday_month").send_keys('June')
driver.find_element_by_name("birthday_year").send_keys('1990')

driver.find_element_by_xpath("//button[@type='submit']").click()

dob_text = driver.find_element_by_class_name('_2_68').text


assert 'Date' in dob_text

print(driver.title)

driver.quit()