# extract all the checkboxes in a single list so that it can be iterated in a for loop


import time
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.maximize_window()


# //input[@type='']

def test_iteration():
    checkboxes_list = driver.find_elements_by_xpath("//input[@type='checkbox']")

    print(len(checkboxes_list))

    # Assert the number of checkbox
    # for checkbox in checkboxes_list:
    #     checkbox.click()
    #     assert checkbox.is_selected()

    # only select the only one option in checkbox

    for checkbox in checkboxes_list:
        print(checkbox.get_attribute('value'))
        if checkbox.get_attribute('value') == 'option2':
            checkbox.click()
            assert checkbox.is_selected()

    driver.quit()


if __name__ == "__main__":
    test_iteration()
