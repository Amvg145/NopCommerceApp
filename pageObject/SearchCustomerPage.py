from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchCustomer:
    txt_email_ID = "SearchEmail"
    txt_Fname_ID = "SearchFirstName"
    txt_Lname_ID = "SearchLastName"
    btn_search_ID = "search-customers"

    tbl_searchResult_xpath = "//table[@id='customers-grid']"
    tbl_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tbl_colms_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_ID).clear()
        self.driver.find_element(By.ID, self.txt_email_ID).send_keys(email)

    def setFname(self, Fname):
        self.driver.find_element(By.ID, self.txt_Fname_ID).clear()
        self.driver.find_element(By.ID, self.txt_Fname_ID).send_keys(Fname)

    def setLname(self, Lname):
        self.driver.find_element(By.ID, self.txt_Lname_ID).clear()
        self.driver.find_element(By.ID, self.txt_Lname_ID).send_keys(Lname)

    def clickOnSearchBtn(self):
        self.driver.find_element(By.ID, self.btn_search_ID).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_rows_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.tbl_searchResult_xpath)
            emailId = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)']/td[2]").text
            if emailId == email:
                flag = True
                break

        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.tbl_searchResult_xpath)
            wait = WebDriverWait(self.driver,10)
            wu = wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)']/td[3]"))).text
            # CName = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)']/td[3]").text
            if wu == name:
                flag = True
                break
        return flag

