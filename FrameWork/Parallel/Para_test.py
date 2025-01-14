import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase:
    def test_chrome(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.google.com/")
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("selenium")
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            assert "selenium" in driver.title, "Title does not contain 'selenium'"
        finally:
            driver.quit()

    def test_safari(self):
        driver = webdriver.Safari()
        try:
            driver.get("https://www.google.com/")
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("selenium")
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            assert "selenium" in driver.title, "Title does not contain 'selenium'"
        finally:
            driver.quit()