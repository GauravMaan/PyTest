# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# @pytest.fixture(params=["safari", "chrome"])
# def driver(request):
#     if request.param == "safari":
#         driver = webdriver.Safari()
#     elif request.param == "chrome":
#         driver = webdriver.Chrome()
#
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#
#
# @pytest.mark.parametrize("username, password, expected_message", [
#     ("valid_user1", "valid_pass1", "Welcome"),
#     ("valid_user2", "valid_pass2", "Welcome"),
#     ("invalid_user", "invalid_pass", "Authentication failed")
# ])
# @pytest.mark.usefixtures("driver")
# class TestAuthentication:
#     def test_authentication(self, driver, username, password, expected_message):
#         driver.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
#
#         # Use the page form elements to enter credentials and submit
#         email_field = driver.find_element(By.ID, "email")
#         password_field = driver.find_element(By.ID, "passwd")
#         login_button = driver.find_element(By.ID, "SubmitLogin")
#
#         email_field.clear()
#         email_field.send_keys(username)
#         password_field.clear()
#         password_field.send_keys(password)
#         login_button.click()
#
#         time.sleep(2)
#         page_source = driver.page_source
#         assert expected_message in page_source, f"Test Failed for {username}. Expected: {expected_message}"
#
#
# if __name__ == "__main__":
#     pytest.main(["-n", "2"])

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.mark.parametrize("email, password, expected_result", [
    ("valid_user@example.com", "valid_password", "My account"),
    ("invalid_user@example.com", "invalid_password", "Authentication failed"),
    ("", "password", "An email address required"),
    ("user@example.com", "", "Password is required")
])
def test_login(driver, email, password, expected_result):
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")


    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys(email)


    password_field = driver.find_element(By.ID, "passwd")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, "SubmitLogin")
    login_button.click()

    time.sleep(2)
    if expected_result == "My account":
        assert "controller=my-account" in driver.current_url, "Login failed with valid credentials"
    else:
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        assert expected_result in error_message, f"Expected error '{expected_result}' not found"


if __name__ == "__main__":
    pytest.main(["-v", "test_file.py"])
