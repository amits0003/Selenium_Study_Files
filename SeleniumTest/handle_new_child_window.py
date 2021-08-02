from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

childWindow = driver.window_handles[1]  #get all the window opened in the browser

#("ParentID", "ChildId") # driver.window_handles == gets the list of Id of all the windows

# Switch to a new window
driver.switch_to.window(childWindow)

# Printing the Text from parent Window
print(driver.find_element_by_tag_name("h3").text)

driver.close()

# Printing the text from child window
driver.switch_to.window(driver.window_handles[0])

print(driver.find_element_by_tag_name("h3").text)

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

driver.quit()