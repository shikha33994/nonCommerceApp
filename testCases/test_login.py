import pytest
from selenium import webdriver
import logging
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
	baseURL = ReadConfig.getApplicationURL()
	username = ReadConfig.getUseremail()
	password = ReadConfig.getPassword()
	logger = LogGen.loggen()

	@pytest.mark.regression
	def test_homePageTitle(self, setup):
		self.logger.info("****************Test_001_Login started***************************")
		self.logger.info("****************Verifying Home Page Title***************************")
		self.driver = setup
		self.driver.get(self.baseURL)
		act_title = self.driver.title
		if act_title == "Your store. Login":
			self.logger.info("****************Home Page Title Test case passed***************************")
			assert True
		else:
			self.driver.save_screenshot("C:\\Users\\Master\\PycharmProjects\\nonCommerceApp\\Screenshots\\"+"test_homePageTitle.png")
			self.logger.error("****************Home Page Title Test Case Failed***************************")
			assert False
		self.driver.close()

	@pytest.mark.sanity
	@pytest.mark.regression
	def test_Login(self, setup):
		self.logger.info("****************Verifying Login Test***************************")

		self.driver = setup
		self.driver.get(self.baseURL)
		self.lp = LoginPage(self.driver)
		self.lp.setUserName(self.username)
		self.lp.setPassword(self.password)
		self.lp.clickLogin()
		act_title = self.driver.title
		if act_title == "Dashboard / nopCommerce administration":
			self.logger.info("****************Login Test case passed***************************")
			assert True
		else:
			self.driver.save_screenshot("C:\\Users\\Master\\PycharmProjects\\nonCommerceApp\\Screenshots\\"+"test_Login.png")
			self.logger.error("****************Login Test case failed***************************")
			assert False
		self.driver.close()