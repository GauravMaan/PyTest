import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_action():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify successful login by checking the presence of inventory page
    assert "inventory" in driver.current_url
    driver.quit()