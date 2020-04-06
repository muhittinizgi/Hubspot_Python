from time import sleep
from HubSpot.Pages.home_page import Home

class LoginPage(Home):

    # Constructor with super()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Login page locators
    _username_id        = "username"
    _password_id        = "password"
    _login_btn_id       = "loginBtn"
    _signup_link_xpath  = "//a[@class='m-left-1']"
    _signup_text_xpath  = "//div[@class='signup-link']"

    # Login Page expectations
    expected_loginpage_title    = "HubSpot Login"
    expected_loginpage_url      = "https://app.hubspot.com/login"

    # Account Page expectations
    expected_accountpage_title  = "Account Setup | HubSpot"
    expected_accountpage_url    = "https://app.hubspot.com/getting-started/"


    # Actions
    def verify_title(self):
        self.verifyTitle(self.expected_loginpage_title)

    def verify_url(self):
        self.verifyURL(self.expected_loginpage_url)

    def if_signup_text_displayed(self):
        self.isElementDisplayed(self._signup_text_xpath, locatorType="xpath")

    def verify_signup_text(self):
        innerText=self.getText(self._signup_text_xpath,"xpath")
        print("-----> Sign Up text : " + innerText)
        return innerText.find("registration")

    def do_login(self,username,password):
        self.highLight(self._username_id, "id", 2)
        self.sendKeys(username,self._username_id,"id")
        self.highLight(self._password_id, "id",2)
        self.sendKeys(password,self._password_id,"id")
        self.elementClick(self._login_btn_id,"id")
        sleep(2)

    def click_signup_link(self):
        self.elementClick(self._signup_link_xpath,"xpath")

    def test_url_title(self):
        self.verify_title()
        self.verify_url()

    def test_accountpage_title(self):
        self.verifyTitle(self.expected_accountpage_title)

    def test_accountpage_url(self):
        self.verifyURL(self.expected_accountpage_url)