import time
from selenium.webdriver.support.ui import Select

class AddCustomer:

    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkCustomer_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    chckboxTaxExempt_xpath = "//*[@id='IsTaxExempt']"
    lstNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstitemStoreName_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    lstitemTestStore2_xpath= "//*[@id='8d276986-3c30-4ab3-9d9b-cdf30dfd9800']"
    lstCustomerRole_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitemForumModrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstitemGuests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemRegistered_xpath = "//*[@id='7027ba38-c16e-4192-8432-637911038f9c']"
    lstitemVendors_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "//*[@id='Gender_Male']"
    rdFeMaleGender_id = "//*[@id='Gender_Female']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    txtDob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath = "//*[@id='Company']"
    txtAdminContent_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    btnSaveAndContinue_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[2]"
    drpmgrofVendor_xpath = "//*[@id='VendorId']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]/span").click()
            time.sleep(1)
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath).click()
        elif role == 'Registered':
            self.driver.find_element_by_xpath(self.lstitemRegistered_xpath).click()
        elif role == 'Vendors':
            self.driver.find_element_by_xpath(self.lstitemVendors_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.lstitemGuests_xpath).click()
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("argument[0].click();", self.listitem())

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrofVendor_xpath))
        drp.select_by_visible_text(value)


    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_xpath(self.rdFeMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

        
