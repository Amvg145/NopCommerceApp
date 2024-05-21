import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    lnk_Customer_menu_xpath = "//a[@href='#']//p[contains(.,'Customers')]"
    lnk_Customer_menuItem_xpath = "//a[@href='/Admin/Customer/List'][contains(.,'Customers')]"
    AddNewUser_btn_xpath = "//a[@class='btn btn-primary']"
    txt_Email_xpath = "//input[@id='Email']"
    txt_Password_xpath = "//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    Gender_male_rdBtn_Id = "Gender_Male"
    Gender_Female_rdBtn_Id = "Gender_Female"
    txt_DOB_xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_xpath = "//input[@id='Company']"
    txt_Customer_Roles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul"
    lstItem_Administrator_xpath = "//li[contains(text(),'Administrators')]"
    lstItem_Registered_xpath = "li[contains(text(),'Registered')]"
    lstItem_Guest_xpath = "//li[contains(text(),'Guest')]"
    lstItem_Vendor_xpath = "//option[contains(text(),'Vendors')]"
    CustomerRole_remove_btn_xpath = "//li[@title='Registered']/span[@class='select2-selection__choice__remove']"
    drD_Vendor_xpath = "//*[@id='VendorId']"
    txt_adminComment_xpath = "//textarea[@id='AdminComment']"
    save_btn_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_Customer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_Customer_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.AddNewUser_btn_xpath).click()

    def setEmail(self, Email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(Email)

    def setPassword(self, Password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(Password)

    def setFirstName(self, FirstName):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(FirstName)

    def setLastName(self, Lastname):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(Lastname)

    def setGender(self, gender='Male'):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.Gender_male_rdBtn_Id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.Gender_Female_rdBtn_Id).click()
        else:
            self.driver.find_element(By.ID, self.Gender_male_rdBtn_Id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setComapanyName(self, Comname):
        self.driver.find_element(By.XPATH, self.txt_CompanyName_xpath).send_keys(Comname)

    def setCustomerRoles(self, role='Registered'):
        self.custRole = self.driver.find_element(By.XPATH, self.txt_Customer_Roles_xpath)
        self.custRole.click()

        wait = WebDriverWait(self.driver, 10)

        if role == 'Registered':
            self.custRole.click()

        elif role == 'Guests':
            self.listItem = wait.until(EC.element_to_be_clickable((By.XPATH, self.lstItem_Guest_xpath)))
            self.listItem.click()
            self.driver.find_element(By.XPATH, self.CustomerRole_remove_btn_xpath).click()

        elif role == 'Administrators':
            self.listItem = wait.until(EC.element_to_be_clickable((By.XPATH, self.lstItem_Administrator_xpath)))
            self.listItem.click()
            self.custRole.click()

        elif role == 'Vendors':
            self.listItem = wait.until(EC.element_to_be_clickable((By.XPATH, self.lstItem_Vendor_xpath)))
            self.listItem.click()
            self.custRole.click()

        else:
            self.driver.find_element(By.XPATH, self.lstItem_Registered_xpath).click()

    def setManagerVendor(self, value):
        drd = Select(self.driver.find_element(By.XPATH, self.drD_Vendor_xpath))
        drd.select_by_visible_text(value)

    def clickSaveBtn(self):
        self.driver.find_element(By.XPATH, self.save_btn_xpath).click()


