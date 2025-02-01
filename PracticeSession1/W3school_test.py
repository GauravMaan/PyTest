from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_clickable():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_button")

    # Wait for the iframe to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "iframeResult"))
    )
    driver.switch_to.frame("iframeResult")

    try:
        # Wait for the button to be clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Click Me!"]'))
        )
        assert button.is_enabled(), "Button is not clickable"
        print("Button is clickable.")
    finally:
        driver.quit()