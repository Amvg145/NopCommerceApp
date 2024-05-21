import pytest
from selenium.webdriver.common.by import By
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    loggers = LogGen.loggen()
    screenshot_path = ReadConfig.getScreenshotPath()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.loggers.info("***** Test_003_AddCustomers *****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.loggers.info("*********** Login Successfully ************")

        self.loggers.info("************ Started Add Customer Test ************")
        self.addcustmr = AddCustomer(self.driver)
        self.addcustmr.clickCustomersMenu()
        self.addcustmr.clickOnCustomersMenuItem()
        self.addcustmr.clickOnAddNew()
        self.loggers.info("********* Providing Customer Information ************")
        self.email = random_generator() + "@gmail.com"
        self.driver.implicitly_wait(3)
        self.addcustmr.setEmail(self.email)
        self.addcustmr.setPassword("test1234")
        self.addcustmr.setFirstName("AM")
        self.addcustmr.setLastName("VG")
        self.addcustmr.setGender()  # it will take default value
        self.addcustmr.setDOB("07-05-1998")  # DD-MM-YYY
        self.addcustmr.setComapanyName("Testing Pvt Ltd")
        self.addcustmr.setCustomerRoles()  # it will take default value 'Registered'
        self.addcustmr.setCustomerRoles("Vendors")
        self.addcustmr.setManagerVendor("Vendor 2")
        self.addcustmr.clickSaveBtn()
        self.driver.implicitly_wait(3)

        self.loggers.info("******** Saving Account information ********")
        self.loggers.info("******* Add Customer validation Started *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        self.success = 'The new customer has been added successfully.'
        self.warn = 'A customer with a vendor associated could not be in "Administrators" role.'
        if self.warn in self.msg and self.success in self.msg:
            self.driver.save_screenshot(self.screenshot_path + "test_addCustomer_PW.png")
            assert True == True
            self.loggers.info("****** Add Customer Test Passed *******")
        elif self.success in self.msg:
            self.driver.save_screenshot(self.screenshot_path + "test_addCustomer_P.png")
            assert True == True
            self.loggers.info("****** Add Customer Test Passed *******")
        else:
            self.driver.save_screenshot(self.screenshot_path + "test_addCustomer_F.png")
            self.loggers.info("******** Add Customer test Failed ********")
            assert True == False
        self.driver.close()
        self.loggers.info("********** Ending Home Page Title testing ***********")
        self.loggers.info("*-------------------------------****--------------------------------*")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
