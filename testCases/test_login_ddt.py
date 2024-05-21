import time

import pytest

from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = r".//TestData//testingdata.xlsx"
    screenshot_path = ReadConfig.getScreenshotPath()
    loggers = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.loggers.info("******************** Test_002_DDT_Login ************************")
        self.loggers.info("**************** Verifying Login Page *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows: ", self.rows)
        list_status = []

        for row in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', row, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            Act_title = self.driver.title
            Expected_title = "Dashboard / nopCommerce administration"
            if Act_title == Expected_title:
                if self.exp == 'Pass':
                    self.loggers.info("***** Passed *****")
                    self.lp.clickLogout()
                    list_status.append('Pass')
                elif self.exp == 'Fail':
                    self.loggers.info("***** Failed *****")
                    self.lp.clickLogout()
                    list_status.append('Fail')
            elif Act_title != Expected_title:
                if self.exp == 'Pass':
                    self.loggers.info("***** Failed *****")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.loggers.info("***** Passed *****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.loggers.info("****** Login DDT testdata Passed... *******")
            self.driver.close()
            assert True
        else:
            self.loggers.info("****** Login DDT testdata Failed... *******")
            self.driver.close()
            assert False

        self.loggers.info("***** End of Login Page DDT test *****")
        self.loggers.info("***** Completed Test_002_DDT_Login ")

        self.loggers.info("*-------------------------------****--------------------------------*")
