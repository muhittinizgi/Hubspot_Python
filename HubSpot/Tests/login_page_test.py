from ddt import unpack, data, ddt, file_data

from HubSpot.Utils.get_csv_data import get_csv_data
from HubSpot.Base.base_driver import Driver
from HubSpot.Configuration.config import Config
from HubSpot.Pages.home_page import Home
from HubSpot.Pages.login_page import LoginPage

# THE SAME TESTS ARE DONE WITH USAGE
#   1)CONFIG,
#   2)*.CSV ,
#   3)*.JSON  ,
#   4)ARRAY
@ddt
class LoginPageTest(Driver):

    def test_login_page_1(self):
        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.screenShot("homepage")
        home.go_to_login_page()
        # LogIn Page_________________________
        login = LoginPage(driver)
        login.screenShot("loginpage")
        login.test_url_title()
        login.verify_signup_text()
        login.do_login(Config.email, Config.password)
        # Verify if logged in account_________________________
        login.test_accountpage_title()
        login.test_accountpage_url()

    @data(*get_csv_data(Config.test_user_data_csv))
    @unpack
    def test_login_page2(self,email,password):

        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.screenShot("homepage")
        home.go_to_login_page()
        # LogIn Page_________________________
        login = LoginPage(driver)
        login.screenShot("loginpage")
        login.test_url_title()
        login.verify_signup_text()
        login.do_login(username=email, password=password)
        # Verify if logged in account_________________________
        login.test_accountpage_title()
        login.test_accountpage_url()

    @file_data(Config.test_user_data_json)
    @unpack
    def test_login_page_3(self,email,password):

        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.screenShot("homepage")
        home.go_to_login_page()
        # LogIn Page_________________________
        login = LoginPage(driver)
        login.screenShot("loginpage")
        login.test_url_title()
        login.verify_signup_text()
        login.do_login(username=email, password=password)
        # Verify if logged in account_________________________
        login.test_accountpage_title()
        login.test_accountpage_url()

    @data(["muhittin@gmail.com","muhittin@19"],["Nurettin@gmail.com","Nettin@1945"])
    @unpack
    def test_login_page_4(self, email, password):
        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.screenShot("homepage")
        home.go_to_login_page()
        # LogIn Page_________________________
        login = LoginPage(driver)
        login.screenShot("loginpage")
        login.test_url_title()
        login.verify_signup_text()
        login.do_login(username=email, password=password)
        # Verify if logged in account_________________________
        login.test_accountpage_title()
        login.test_accountpage_url()