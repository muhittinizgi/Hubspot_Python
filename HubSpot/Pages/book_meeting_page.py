from time import sleep
from HubSpot.Pages.home_page import Home

class BookMeeting(Home):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ## Book Meeting Page locators
    _welcome_text_tag       = "h3"
    _firstname_name         = "firstname"
    _lastname_name          = "lastname"
    _email_name             = "email"
    _phone_name             = "phone"
    _company_name           = "company"
    _website_name           = "website"
    _employees_count_name   = "employees__c"
    _country_name           = "country_dropdown"
    _marketting_name        = "marketing_company_auto__c"
    _textbox_name           = "what_are_you_looking_to_accomplish_with_hubspot_"
    _nextBtn_xpath          = "//input[contains(@class,'hs-button primary')]"

    # Book Meeting Page expectations
    expected_page_title     = "Contact Sales | HubSpot's Marketing and Sales Software"
    expected_page_url       = "https://offers.hubspot.com/contact-sales"

    # Actions
    def verify_title(self):
        self.verifyTitle(self.expected_page_title)

    def verify_url(self):
        self.verifyURL(self.expected_page_url)

    def verify_welcome_text(self):
        self.elementPresentCheck(self._welcome_text_tag,"tag")

    def get_welcome_text(self):
        self.highLight(self._welcome_text_tag,2)
        welcome_text=self.getText(self._welcome_text_tag,"tag")
        print(welcome_text)


    def fill_book_meeting_form(self,firstname,lastname,email,phone,company,
                               website,employees_count,country,marketting,text):
        self.sendKeys(firstname,self._firstname_name,"name")
        self.sendKeys(lastname, self._lastname_name, "name")
        self.sendKeys(email, self._email_name, "name")
        self.sendKeys(phone, self._phone_name, "name")
        self.sendKeys(company, self._company_name, "name")
        self.sendKeys(website, self._website_name, "name")
        self.selectDropDownByValue(employees_count,self._employees_count_name,"name")
        self.selectDropDownByVisibleText(country,self._country_name,"name")
        self.selectDropDownByOptionClick(marketting, self._marketting_name, "name")
        self.sendKeysByActions(text,self._textbox_name,"name")

    def submit_request_to_book_meeting(self):
        self.highLight(self._nextBtn_xpath,"xpath",2)
        # self.elementClick(self._nextBtn_xpath,"xpath")
        sleep(2)
