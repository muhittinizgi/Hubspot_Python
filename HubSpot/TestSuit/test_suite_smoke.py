from unittest import TestLoader, TestSuite, TextTestRunner
from HubSpot.Tests.home_page_test import HomePageTest
from HubSpot.Tests.login_page_test import LoginPageTest
from HubSpot.Tests.account_page_test import AccountPageTest
from HubSpot.Tests.book_meeting_page_test import BookMeetingPageTest
from HubSpot.Tests.contacts_page_test import ContactsPageTest

# Get all test from the test class
tc1 =  TestLoader().loadTestsFromTestCase(HomePageTest)
tc2 =  TestLoader().loadTestsFromTestCase(LoginPageTest)
tc3 =  TestLoader().loadTestsFromTestCase(AccountPageTest)
tc4 =  TestLoader().loadTestsFromTestCase(BookMeetingPageTest)
tc5 =  TestLoader().loadTestsFromTestCase(ContactsPageTest)

# Create test suite
smokeTest = TestSuite([tc1,tc2,tc3])
TextTestRunner(verbosity=2).run(smokeTest)
