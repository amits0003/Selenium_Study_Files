from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")


def test_form():
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@name='name']").send_keys('Amit')
    driver.find_element_by_xpath("//input[@name='email']").send_keys('veddaily@gmail.com')
    driver.find_element_by_xpath("//input[@type='password']").send_keys("AmitKumar")
    driver.find_element_by_xpath("//input[@id='inlineRadio1']").click()
    driver.find_element_by_xpath("//input[@name='bday']").send_keys("15-02-1994")
    driver.find_element_by_xpath("//input[@type='submit']").click()

    alert_text = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
    assert alert_text == "×\nSuccess! The Form has been submitted successfully!."


    dropdwon  = Select()
    driver.quit()


if __name__ == "__main__":
    test_form()
