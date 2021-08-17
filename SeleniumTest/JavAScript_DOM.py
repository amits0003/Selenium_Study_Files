# javascript DOM can access any element in web age just like how selenium does
# selenium have a method to execute javascript code in it


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name('name').send_keys('hello')
print(driver.find_element_by_name('name').text)
print(driver.find_element_by_name('name').get_attribute('value'))
driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
#shopButton = driver.find_element_by_css_selector("a[href* = 'shop']")
#driver.execute_script("argument[0].click();",shopButton)

driver.quit()