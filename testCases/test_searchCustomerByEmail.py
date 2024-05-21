import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.LoginPage import LoginPage
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_004_SearchCustomersByEmail:
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    loggers = LogGen.loggen()
    screenshot_path = ReadConfig.getScreenshotPath()

    @pytest.mark.regression
    def test_searchcustomerbyemail(self, setup):
        self.loggers.info("***** Test_004_SearchCustomersByEmail *****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.loggers.info("*********** Login Successfully ************")

        self.loggers.info("************ Starting Search Customer by Email ************")
        self.addcustmr = AddCustomer(self.driver)
        self.addcustmr.clickCustomersMenu()
        self.addcustmr.clickOnCustomersMenuItem()

        self.loggers.info("*********** Searching Customer By Email **************")
        self.searchCustmr = SearchCustomer(self.driver)
        self.searchCustmr.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCustmr.clickOnSearchBtn()
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(5)
        status = self.searchCustmr.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.driver.close()
        self.loggers.info("*************** TC_searchByEmail Finished **************")
        self.loggers.info("*-------------------------------****--------------------------------*")
