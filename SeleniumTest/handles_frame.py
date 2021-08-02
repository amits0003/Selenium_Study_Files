from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/iframe")

#sWITCH TO iFRAME

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Hi, i am amit kumar")
print(driver.find_element_by_css_selector("#tinymce").text)
assert "Hi, i am amit kumar" == driver.find_element_by_css_selector("#tinymce").text

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

driver.quit()