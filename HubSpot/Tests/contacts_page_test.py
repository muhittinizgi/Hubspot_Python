from ddt import ddt, data, unpack
from HubSpot.Base.base_driver import Driver
from HubSpot.Configuration.config import Config
from HubSpot.Pages.home_page import Home
from HubSpot.Pages.login_page import LoginPage
from HubSpot.Pages.account_page import AccountPage
from HubSpot.Pages.contacts_page import ContactsPage
from HubSpot.Utils.get_csv_data import get_csv_data


@ddt
class ContactsPageTest(Driver):

    def test_contacts_Page(self):

        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.go_to_login_page()
        # LogIn Page_________________________
        login = LoginPage(driver)
        login.do_login(Config.email, Config.password)
        # Account Page_________________________
        account=AccountPage(driver)
        account.go_to_contacts_page()
        # Contacts Page_________________________
        contacts=ContactsPage(driver)
        contacts.open_new_contacts_form()
        contacts.fill_contacts_form(
            "selimkaramehmet@hotmail.com",
            "Selim",
            "Kara",
            "Software Developer",
            "988 023 4567",
            "New"
        )
        contacts.click_and_submit_form()
        contacts.back_to_contacts()
        contacts.test_contacts_list()