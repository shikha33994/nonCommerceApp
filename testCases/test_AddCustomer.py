import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string, random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********Test_003_AddCustomer Started*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********Login Successfull*********")
        self.logger.info("********Starting Add Customer Test*****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("*********Providing Customer Info**********")
        self.logger.info("******Providing Customer Info*******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Shikha")
        self.addcust.setLastName("Shrivastava")
        self.addcust.setDob("2/13/1985")
        self.addcust.setCompanyName("ABC")
        self.addcust.setAdminContent("Testing ...")
        self.addcust.clickOnSave()

        self.logger.info("*********Saving Customer Info*********")

        self.logger.info("******Add Customer Validation started******")
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg :
            assert True
            self.logger.info("Add customer test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddCustomer_scr.png")
            self.logger.error("********Add customer test failed********")
            assert False

        self.driver.close()
        self.logger.info("**********Ending Home Page Title Test*********")


def random_generator(size = 8, chars = string.ascii_lowercase+string.digits):
    print(''.join(random.choice(chars) for x in range(size)))
    return ''.join(random.choice(chars) for x in range(size))