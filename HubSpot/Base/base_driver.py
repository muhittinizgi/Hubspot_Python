from HubSpot.Configuration.config import Config
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver(unittest.TestCase):
    #setUP contains the browser setup attributes
    @classmethod
    def setUp(cls):
        chrome_options = Options()
        # chrome_options.add_argument("user-data-dir=selenium")
        # self.driver = webdriver.Chrome(chrome_options)
        cls.driver = webdriver.Chrome(Config.chrome_path,0,chrome_options)
        print(str(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S - ")) + "LOG - " + "Browser is initialized ---------- ")
        cls.driver.implicitly_wait(6)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(Config.wait_time)
        cls.driver.get(Config.html)

    #tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDown(cls):
     if (cls.driver!=None):
        print(str(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S - ")) + "LOG - " + "Browser is closed ---------- ")
        cls.driver.close()
        cls.driver.quit()