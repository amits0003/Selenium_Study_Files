

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

shopbutton = driver.find_element_by_css_selector("a[href* ='hop')]")

driver.execute_script( 'argument[0].click;', shopbutton )