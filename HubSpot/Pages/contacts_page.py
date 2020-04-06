from time import sleep
from HubSpot.Pages.account_page import AccountPage

class ContactsPage(AccountPage):
    # Constructor with super()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Contacts Page locators
    _account_menu_id            = "account-menu-container"
    _user_email_class           = "user-info-email"
    # Saved Contacts List
    _contacts_name_list_xpath   = "//table//tbody/tr/td[2]/div/a"
    _number_of_contacts_xpath   = "//div[@class='m-top-2']/small/*[1]"
    # Create contact btn
    _create_contact_btn_xpath   = "//span[contains(text(),'Create contact')]"
    # Form Fields
    _email_xpath            = "//input[@name='textInput']"
    _first_name_xpath       = "//input[@class='form-control private-form__control' and @data-field='firstname']"
    _last_name_xpath        = "//input[@class='form-control private-form__control' and @data-field='lastname']"
    _job_title_xpath        = "//input[@class='form-control private-form__control' and @data-field='jobtitle']"
    _phone_xpath            = "//input[@class='form-control private-form__control' and @data-field='phone']"
    _lead_status_xpath      = "//div[@data-selenium-test='property-input-hs_lead_status']"
    _lead_status_list_xpath = "//div[starts-with(@id,'react-select') and @class='Select-option']"  # 7 options
    # submit btn
    _submit_contact_form_xpath  = "//div[@class='private-layer']//li[1]"
    # back to contacts page
    _back_to_contacts_link_xpath= "//div[@class='display-flex']/div/div/nav"

    # Account Page expectations
    expected_contactspage_title = "Contacts"
    expected_contactspage_url   = "https://app.hubspot.com/contacts/"

    # Actions
    def verify_title(self):
        self.verifyTitle(self.expected_contactspage_title)

    def verify_url(self):
        self.verifyURL(self.expected_contactspage_url)

    def open_new_contacts_form(self):
        self.highLight(self._create_contact_btn_xpath, "xpath", 2)
        self.elementClick(self._create_contact_btn_xpath, "xpath")

    def fill_contacts_form(self, email, fname, lname, jobtitle, phone, status):
        self.sendKeys(email, self._email_xpath, "xpath")
        self.sendKeys(fname, self._first_name_xpath, "xpath")
        self.sendKeys(lname, self._last_name_xpath, "xpath")
        self.sendKeys(jobtitle, self._job_title_xpath, "xpath")
        self.sendKeys(phone, self._phone_xpath, "xpath")
        self.select_lead_status(status)

    def click_and_submit_form(self):
        self.highLight(self._submit_contact_form_xpath, "xpath", 2)
        self.elementClick(self._submit_contact_form_xpath, "xpath")
        sleep(5)

    def back_to_contacts(self):
        self.highLight(self._back_to_contacts_link_xpath, "xpath", 2)
        self.elementClick(self._back_to_contacts_link_xpath, "xpath")
        sleep(10)

    def test_contacts_list(self):
        contact_names = self.getElementList(self._contacts_name_list_xpath, "xpath")
        contacts_count = len(contact_names)  # count the list of contacts
        # get number of contacts from the 'All Contacts' summary
        number_of_contacts = int(self.getText(self._number_of_contacts_xpath, "xpath").split()[0])
        # Compare the numbers (!!!! BASIC comparison if contacts<25 !!!!)
        print(self.logTime() + "NOTE - " + "Number of Contacts are compared: ")
        print(">>> Summary contacts count given : " + str(number_of_contacts))
        print(">>> Contacts listed : " + str(contacts_count))
        return contacts_count == number_of_contacts

    def select_lead_status(self, status):
        """Select a status from list
        ['New','Open','In progress','Open deal','Unqualified','Attempted to contact','Connected','Bad timing']"""
        self.elementClick(self._lead_status_xpath, "xpath")
        status_list = self.getElementList(self._lead_status_list_xpath, "xpath")
        try:
            for option in status_list:
                if option.text == status:
                    option.click()
                    break
            print(
                self.logTime() + "LOG - " + "Selected text '" + status + "' on element ")
        except:
            print(
                self.logTime() + "EXCEPTION - " + "Cannot select text '" + status + "' on element ")
