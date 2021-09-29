from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def test_end_2_end_checkout():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe"
                              ,options=chrome_options)

    #implicit wait
    driver.implicitly_wait(30)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.maximize_window()

    shopbutton = driver.find_element_by_css_selector("a[href*='shop']")

    driver.execute_script("arguments[0].click();" , shopbutton)

    products = driver.find_elements_by_xpath("//div[@class='card h-100']")

    #//div[@class='card h-100']/div/h4/a

    for product in products :
        productName = product.find_element_by_xpath("div/h4/a").text

        if productName == "Blackberry" :
            product.find_element_by_xpath("div/button").click()

    driver.find_element_by_css_selector("a[class*='btn btn-primary']").click()

    driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

    #explicit wait
    driver.find_element_by_id("country").send_keys("India")

    wait = WebDriverWait(driver, 60)

    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

    driver.find_element_by_link_text("India").click()

    driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

    driver.find_element_by_xpath("//input[@type='submit']").click()

    successTest = driver.find_element_by_class_name("alert-success").text
    print(driver.find_element_by_class_name("alert-success").text)

    assert successTest == '×\nSuccess! Thank you! Your order will be delivered in next few weeks :-).'

    driver.quit()

if __name__ =="__main__":
    test_end_2_end_checkout()

