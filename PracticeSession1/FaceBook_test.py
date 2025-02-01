import pytest
from selenium import webdriver

def test_page_title():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()