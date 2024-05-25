import time

import pytest

from pageObject.LoginPage import LoginPage
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_SearchCustomersByName:
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    loggers = LogGen.loggen()
    screenshot_path = ReadConfig.getScreenshotPath()

    @pytest.mark.regression
    def test_searchcustomerbyName(self, setup):
        self.loggers.info("***** Test_005_SearchCustomersByName *****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.loggers.info("*********** Login Successfully ************")

        self.loggers.info("************ Starting Search Customer by Name ************")
        self.addcustmr = AddCustomer(self.driver)
        self.addcustmr.clickCustomersMenu()
        self.addcustmr.clickOnCustomersMenuItem()

        self.loggers.info("*********** Searching Customer By Name **************")
        self.searchCustmr = SearchCustomer(self.driver)
        self.searchCustmr.setFname("Victoria")
        self.searchCustmr.setLname("Terces")
        self.searchCustmr.clickOnSearchBtn()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(5)
        status = self.searchCustmr.searchCustomerByName("Victoria Terces")
        assert True == status
        self.driver.close()
        self.loggers.info("*************** TC_searchByName Finished **************")
        self.loggers.info("*-------------------------------****--------------------------------*")
