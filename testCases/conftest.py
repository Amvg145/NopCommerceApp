import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--v=1")


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.maximize_window()
        print("Launching Chrome Browser___")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("Launching Firefox Browser___")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Chrome Browser___")
    return driver


def pytest_addoption(parser): # this will get value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): # this will return browser value to setup method
    return request.config.getoption("--browser")


################# PyTest HTML Reports ####################
def pyets_configure(config):
    config._metadata['Project Name'] = 'NopCommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester Name'] = 'Veerana Gouda'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

