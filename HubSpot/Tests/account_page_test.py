from HubSpot.Base.base_driver import Driver
from HubSpot.Configuration.config import Config
from HubSpot.Pages.home_page import Home
from HubSpot.Pages.login_page import LoginPage
from HubSpot.Pages.account_page import AccountPage

class AccountPageTest(Driver):
    def test_Account_Page(self):

        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.screenShot("homepage")
        home.go_to_login_page()
        # LogIn Page_________________________
        login = LoginPage(driver)
        login.screenShot("loginpage")
        login.do_login(Config.email, Config.password)
        # Account Page_________________________
        account=AccountPage(driver)
        account.test_accountpage_title()
        account.test_accountpage_url()
        account.verify_user()
        account.screenShot("accountpage")
