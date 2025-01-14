import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser option: chrome or safari")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = setup(browser)
    yield driver
    driver.quit()

def setup(browser):
    if browser == "Safari":
        driver = webdriver.Safari()
    elif browser == "Chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser: {browser}. Choose 'Chrome' or 'Safari'.")

    return driver