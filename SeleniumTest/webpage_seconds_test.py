
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://login.salesforce.com/")

assert driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text == 'Username'
driver.find_element_by_css_selector('.username').send_keys('Amit')
driver.find_element_by_css_selector('.password').send_keys('amitK')
driver.find_element_by_link_text('Forgot Your Password?').click()
driver.find_element_by_xpath("//form[@name='forgotPassword']/div['verifyform']/input[3]").click()


driver.close()
