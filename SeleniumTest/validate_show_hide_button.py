from selenium import webdriver

from selenium.webdriver import ActionChains


def test_show_hide_button():
    # Chrome Driver Location
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

    driver.find_element_by_id("show-textbox").click()

    assert driver.find_element_by_id("displayed-text").is_displayed()

    driver.find_element_by_id("hide-textbox").click()

    assert not driver.find_element_by_id("displayed-text").is_displayed()


if __name__ == "__main__":
    test_show_hide_button()
