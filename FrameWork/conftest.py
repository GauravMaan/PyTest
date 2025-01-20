# conftest.py

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Set up WebDriver
    driver = webdriver.Chrome()  # You can also use Firefox or another browser
    driver.maximize_window()  # Optional: Maximize the window

    # Yield driver to the test function
    yield driver

    # Teardown after test is done
    driver.quit()