import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
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

