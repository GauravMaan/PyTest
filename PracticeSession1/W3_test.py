import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission_error():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")
    driver.switch_to.frame("iframeResult")

    # Submitting form without entering any data
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Check if browser validation error appears (HTML5 validation message)
    name_field = driver.find_element(By.NAME, "fname")
    assert name_field.get_attribute("required") is not None
    driver.quit()