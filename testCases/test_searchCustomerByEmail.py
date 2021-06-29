import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomer import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string, random

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********Test_004_SearchCustomerByEmail Started*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********Login Successfull*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("**********Searching Customer by Email ID*********")
        searchcust = SearchCustomer(self.driver)

        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)

        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert status
        self.logger.info("*********TC_004_searchCustomerByEmail Finished************")
        self.driver.close()
