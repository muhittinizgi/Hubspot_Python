from time import sleep

from HubSpot.Configuration.config import Config
from HubSpot.Pages.login_page import LoginPage

class AccountPage(LoginPage):
    # Constructor with super()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ## Account Page locators
    _account_menu_id                =   "account-menu-container"
    _user_email_class               =   "user-info-email"
    _navigation_menu_contacts_xpath ="//div[@class='desktop-nav-left-container']//a[@id='nav-primary-contacts-branch']"
    _contacts_link_xpath            =   "//nav[@id='navbar']//div//div//div//div//div//div//a[@id='nav-secondary-contacts']"

    # Account Page expectations
    expected_accountpage_title      = "Account Setup | HubSpot"
    expected_accountpage_url        = "https://app.hubspot.com/getting-started/"

    # Actions
    def verify_title(self):
        self.verifyTitle(self.expected_accountpage_title)

    def verify_url(self):
        self.verifyURL(self.expected_accountpage_url)

    def verify_user(self):
        self.elementClick(self._account_menu_id,locatorType="id")
        self.highLight(self._user_email_class,"class",2)
        user=self.getText(self._user_email_class,locatorType="class")
        print("-----> User email : " + user)
        sleep(2)
        return user.find(Config.email)

    def go_to_contacts_page(self):
        self.elementClick(self._navigation_menu_contacts_xpath,"xpath")
        self.elementClick(self._contacts_link_xpath,"xpath")
        sleep(2)