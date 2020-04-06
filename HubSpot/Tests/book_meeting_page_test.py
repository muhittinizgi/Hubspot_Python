import unittest

from ddt import data, unpack, ddt

from HubSpot.Base.base_driver import Driver
from HubSpot.Configuration.config import Config
from HubSpot.Pages.home_page import Home
from HubSpot.Pages.book_meeting_page import BookMeeting
from HubSpot.Utils.get_csv_data import get_csv_data

@ddt
class BookMeetingPageTest(Driver):
    @data(*get_csv_data(Config.book_meeting_user_data_csv))
    @unpack
    def test_book_meeting_page(self, firstname, lastname, email, phone, company,website, employees_count, country, marketting, text):

        driver = self.driver
        # Home Page_________________________
        home = Home(driver)
        home.cookies_warning_allow()
        home.screenShot("homepage")
        home.go_to_book_meeting_page()
        # Booking Page_________________________
        book_meeting = BookMeeting(driver)
        book_meeting.verify_title()
        book_meeting.verify_url()
        book_meeting.fill_book_meeting_form(firstname, lastname, email, phone, company,website, employees_count, country, marketting, text)
        # book_meeting.fill_book_meeting_form(
        #     "Metin",
        #     "Ozel",
        #     "metinoz@gmail.com",
        #     "2012023456",
        #     "Software LLC",
        #     "https://google.com",
        #     "11 to 25",
        #     "Turkey",
        #     "Yes",
        #     "That is an ordinary message"
        # )
        book_meeting.submit_request_to_book_meeting()
        book_meeting.screenShot("bookmeetingpage")
