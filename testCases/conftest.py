#testCases/conftest.py

import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
	if browser == 'chrome':
		driver = webdriver.Chrome()
		print("Launching Chrome Browser......")
		return driver
	elif browser == 'firefox':
		driver = webdriver.Firefox()
		print("Launching Firefox Browser......")
		return driver
	else:
		driver = webdriver.Edge(executable_path="C:\\Shikha\\msedgedriver")
		print("Launching Edge Browser.....")
		return driver


def pytest_addoption(parser):				# This will get the value from CLI
	parser.addoption("--browser")

@pytest.fixture()
def browser(request):						# This will return the browser value to setup method
	return request.config.getoption("--browser")


###############Pytest HTML Report################

#it is hook for adding environment info to HTML Report
def pytest_configure(config):
	config._metadata['Project Name'] = 'nop Commerce'
	config._metadata['Module Name'] = 'Customers'
	config._metadata['Tester'] = 'Shikha'


#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
	metadata.pop("JAVA_HOME", None)
	metadata.pop("Plugins", None)