from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

def test_func():
    driver.get("http://www.techtutorial.in/selenium-with-python-interview-questions-and-answers/")

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@type='submit']").click()

    word =  driver.find_element_by_xpath("//span[text()='The field is required.']").text

    assert word == 'The field is required.'



def test_func2():
    driver.get("http://automationpractice.com/")

    driver.find_element_by_xpath()