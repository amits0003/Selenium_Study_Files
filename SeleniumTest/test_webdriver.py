from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://www.google.com")
print(driver.title)
driver.get("https://www.twitter.com")
print(driver.current_url)
driver.close()