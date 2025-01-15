import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.feature('Search Feature')
@allure.story('Search for T-shirt on the Automation Practice website')
def test_search_tshirt():
    with allure.step('Launch Safari browser'):
        driver = webdriver.Chrome()

    try:
        with allure.step('Navigate to the website'):
            driver.get("http://www.automationpractice.pl/index.php")
        with allure.step('Find the search box and input "T-shirt"'):
            search_box = driver.find_element(By.ID, "search_query_top")
            search_box.send_keys("T-shirt")
        with allure.step('Submit the search query'):
            search_box.send_keys(Keys.RETURN)
        with allure.step('Wait for search results to load'):
            time.sleep(2)

    finally:
        with allure.step('Close the browser'):
            driver.quit()