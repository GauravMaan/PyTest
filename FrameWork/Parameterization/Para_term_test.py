import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    time.sleep(3)
    search_box.send_keys("pytest" + Keys.RETURN)