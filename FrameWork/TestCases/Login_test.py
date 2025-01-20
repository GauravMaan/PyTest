# FrameWork/TestCases/Login_test.py
import time

import pytest

from FrameWork.pages.Login_page import LoginPage


class TestLogin:
    def test_login(self, driver):  # 'driver' fixture will be automatically passed
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        # Create an object of LoginPage
        login_page = LoginPage(driver)

        # Perform actions using methods from LoginPage
        login_page.login("Admin", "admin123")
        time.sleep(3)
        # Add assertions to validate login
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard", "Login failed!"