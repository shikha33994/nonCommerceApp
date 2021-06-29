import pytest
from selenium import webdriver
import logging
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtiles

class Test_002_ddd_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\Master\\PycharmProjects\\nonCommerceApp\\TestData\\Data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("**********Test_002_ddd_Login*********")
        self.logger.info("****************Verifying Login Test***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtiles.getRowCount(self.path, 'Sheet1')
        print("Number or Rows in a Excel:", self.rows)

        lst_status=[]       # Empty list variable
        for r in range(2, self.rows+1):
            time.sleep(3)
            self.user = ExcelUtiles.readData(self.path, 'Sheet1',r,1)
            self.password = ExcelUtiles.readData(self.path, 'Sheet1',r,2)
            self.exp = ExcelUtiles.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            time.sleep(5)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":                      # Test Case is Pass
                    self.logger.info("*********Passed*********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*********Failed*********")
                    #self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":  # Test Case is Fail
                    self.logger.info("*********Failed*********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*********Passed*********")
                    #self.lp.clickLogout()
                    lst_status.append("Pass")
                    time.sleep(2)

        if "Fail" not in lst_status:
            self.logger.info("****Login data Test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login Data Test Failed*****")
            self.driver.close()
            assert False

        self.logger.info("******End of Login Data Test******")
        self.logger.info("***Completed testCase_Login_ddd_002****")
       # self.driver.close()
