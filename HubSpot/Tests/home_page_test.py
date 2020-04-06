import unittest
from time import sleep
from HubSpot.Base.base_driver import Driver
from HubSpot.Pages.home_page import Home

class HomePageTest(Driver):
    def test_home_page(self):

        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.screenShot("homepage")
        home.test_url_title()
        home.cookies_warning_allow()
        home.test_if_all_elements_displayed()
        sleep(2)

# if __name__ == '__main__':
#     unittest.main()