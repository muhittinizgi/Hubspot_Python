from unittest import TestLoader, TestSuite, TextTestRunner
from HubSpot.Tests.contacts_page_test import ContactsPageTest
from HubSpot.Tests.home_page_test import HomePageTest
from HubSpot.Tests.login_page_test import LoginPageTest
from HubSpot.Tests.account_page_test import AccountPageTest
from HubSpot.Tests.book_meeting_page_test import BookMeetingPageTest
import testtools as testtools

if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(HomePageTest),
        loader.loadTestsFromTestCase(LoginPageTest),
        loader.loadTestsFromTestCase(AccountPageTest),
        loader.loadTestsFromTestCase(BookMeetingPageTest),
        loader.loadTestsFromTestCase(ContactsPageTest)
    ))

    #run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    #run test parallel using concurrent_suite
    # concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult())