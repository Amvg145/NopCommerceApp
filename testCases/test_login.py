import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    screenshot_path = ReadConfig.getScreenshotPath()
    loggers = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.loggers.info("******************** Test_001_Login ***************************")
        self.loggers.info("******************** Verifying Home Page **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.loggers.info("************* test_homePageTitle test case is Passed **************")
        else:
            self.driver.save_screenshot(self.screenshot_path + "test_homePageTitle.png")
            self.driver.close()
            self.loggers.error("************* test_homePageTitle test case is Failed **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.loggers.info("******************** Test_001_Login ***************************")
        self.loggers.info("******************** Verifying Login Page **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        Act_title = self.driver.title
        if Act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.loggers.info("************* test_login test case is Passed **************")
        else:
            self.driver.save_screenshot(self.screenshot_path + "test_login.png")
            self.driver.close()
            self.loggers.error("************* test_login test case is Failed **************")
            assert False

        self.loggers.info("*-------------------------------****--------------------------------*")
