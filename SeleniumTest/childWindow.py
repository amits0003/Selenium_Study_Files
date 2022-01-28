from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element_by_link_text("Click Here").click()


#Switch to new window
#pass the window ID

childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)

newWindowText = driver.find_element_by_tag_name("h3").text

assert 'New Window' == newWindowText
mainWindow = driver.window_handles[0]

driver.switch_to.window(mainWindow)


mainWindowText = driver.find_element_by_tag_name('h3').text

assert 'Opening a new window' == mainWindowText
