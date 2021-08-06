from selenium import webdriver

from selenium.webdriver import ActionChains

# Chrome Driver Location
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")
driver.maximize_window()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

actionObj =  ActionChains(driver)
actionObj.double_click(driver.find_element_by_id("double-click")).perform()

# Context - Click  - Right Mouse Click
#actionObj.context_click(driver.find_element_by_id("double-click")).perform()


# alertObj

alertObj  = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alertObj.text

alertObj.accept()


#driver.quit()