from time import sleep
from selenium.webdriver import ActionChains
from HubSpot.Utils.element_util import ElementUtil

class Home(ElementUtil):

    # Constructor with super()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Home page locators
    _logo_xpath                 = "//img[@id='hsg-nav__logo-desktop']"
    _navigation_links_xpath     = "//ul[contains(@class,'hsg-nav__group--primary')]/li/div/a"
    # _about_link__xpath          = "//ul[contains(@class,'hsg-nav__group--primary')]/li[5]/div/a"
    _log_in_btn_xpath           = "//a[@class='cta--secondary cta--small' and contains(text(),'Log in')]"
    _cookie_allow_btn_id        = "hs-eu-confirmation-button"
    _book_meeting_link_xpath    = "//li[@class='hsg-nav__group-item']//a[@class='hsg-nav__link']"

    # Home Page expectations
    expected_homepage_title     = "HubSpot | Inbound Marketing, Sales, and Service Software"
    expected_homepage_url       = "https://www.hubspot.com/"

    # Login Page expectations
    expected_loginpage_title    = "HubSpot Login"
    expected_loginpage_url      = "https://app.hubspot.com/login"

    # Actions
    def verify_title(self):
        self.verifyTitle(self.expected_homepage_title)

    def verify_url(self):
        self.verifyURL(self.expected_homepage_url)

    def if_cookies_warnig_displayed(self):
        self.isElementDisplayed(self._cookie_allow_btn_id,locatorType="id")
        self.highLight(self._logo_xpath,"xpath",2)

    def if_logo_displayed(self):
        self.isElementDisplayed(self._logo_xpath,locatorType="xpath")

    def if_log_in_btn_displayed(self):
        self.isElementDisplayed(self._log_in_btn_xpath,locatorType="xpath")

    def if_navigation_links_displayed(self):
        navigation_menu_items = self.getElementList(self._navigation_links_xpath,"xpath")
        for item in navigation_menu_items:
            self.highLight(None,None,2,item)  #Use elemet as parameter instead locator  !!!
            ActionChains(self.driver).move_to_element(item).perform()

    def cookies_warning_allow(self):
        self.elementClick(self._cookie_allow_btn_id,locatorType="id")

    def go_to_login_page(self):
        self.elementClick(self._log_in_btn_xpath, locatorType="xpath")
        sleep(5)

    def go_to_book_meeting_page(self):
        self.elementClick(self._book_meeting_link_xpath, locatorType="xpath")

    def test_url_title(self):
        self.verify_title()
        self.verify_url()

    def test_if_all_elements_displayed(self):
        self.if_logo_displayed()
        self.if_navigation_links_displayed()
        self.if_log_in_btn_displayed()

    def test_loginpage_title(self):
        self.verifyTitle(self.expected_loginpage_title)

