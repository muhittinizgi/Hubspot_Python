import datetime
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

class ElementUtil():
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, filename):
        fileName = str(datetime.datetime.now().strftime("%m-%d-%y_%H-%M-%S-"))+filename + ".png"
        screenshotDirectory = "../ScreenShots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            print(self.logTime() + "LOG - " + "Screenshot save to directory: " + destinationFile)
        except:
            print(self.logTime() + "EXCEPTION - " + "### Exception Occurred when taking screenshot")

    def getTitle(self):
        return self.driver.title

    def getURL(self):
        return self.driver.current_url

    def getByType(self, loctorType):
        loctorType = loctorType.lower()
        if (loctorType == "id"):
            return By.ID
        elif (loctorType == "xpath"):
            return By.XPATH
        elif (loctorType == "name"):
            return By.NAME
        elif (loctorType == "class"):
            return By.CLASS_NAME
        elif (loctorType == "css"):
            return By.CSS_SELECTOR
        elif (loctorType == "link"):
            return By.LINK_TEXT
        elif (loctorType == "plink"):
            return By.PARTIAL_LINK_TEXT
        else:
            print(self.logTime() + "LOG - " + "Locator Type " + loctorType + "not correct / supported!")
        return False

    def getElementList(self, locator, locatorType="id"):
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        elements = self.driver.find_elements(byType, locator)
        # for x in range(len(elements)):
        #     print(elements[x].text)
        for element in elements:
            print(element.text)
        if len(elements) > 0:
            print(self.logTime() + "LOG - " + "Element list Found with locator: " + locator +
                  " and locatorType: " + locatorType)
        else:
            print(self.logTime() + "EXCEPTION - " + "Element list NOT Found with locator: " + locator +
                  " and locatorType: " + locatorType)
        return elements

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            # print(self.logTime() + "LOG - " + "Element found")
        except:
            pass
            # print(self.logTime() + "EXCEPTION - " + "Element not found")
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            print(self.logTime() + "LOG - " + "Clicked on element with locator: " + locator +
                  " locatorType: " + locatorType)
        except:
            print(self.logTime() + "EXCEPTION - " + "Cannot click on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(self.logTime() + "LOG - " + "Sent data '"+data+"' on element with locator: " + locator +
                  " locatorType: " + locatorType)
        except:
            print(self.logTime() + "LOG - " + "Cannot send data '"+data+"' on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def clearField(self, locator="", locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.clear()
        print(self.logTime() + "LOG - " + "Clear field with locator: " + locator +
              " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                print(self.logTime() + "LOG - " + "Getting text on element with locator: " + locator +
                      " locatorType: " + locatorType + " :: " + info)
                text = text.strip()
        except:
            print(self.logTime() + "ERROR - " + "Failed to get text on element with locator: " + locator +
                  " locatorType: " + locatorType + " :: " + info)
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                print(self.logTime() + "LOG - " + "Element present with locator: " + locator +
                      " locatorType: " + locatorType)
                return True
            else:
                print(self.logTime() + "LOG - " + "Element not present with locator: " + locator +
                      " locatorType: " + locatorType)
                return False
        except:
            print(self.logTime() + "ERROR - " + "Element not found with locator: " + locator +
                  " locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                print(self.logTime() + "LOG - " + "Element is displayed with locator: " + locator +
                      " locatorType: " + locatorType)
            else:
                print(self.logTime() + "LOG - " + "Element NOT displayed with locator: " + locator +
                      " locatorType: " + locatorType)
            return isDisplayed
        except:
            print(self.logTime() + "ERROR - " + "Element not found with locator: " + locator +
                  " locatorType: " + locatorType)
            return False

    def sendKeysWithEnter(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data, Keys.ENTER)

            print(self.logTime() + "LOG - " + "Send data '"+data+"' on element " + locator + "locator type: " + locatorType)
        except:
            print(self.logTime() + "EXCEPTION - " + "Cannot send data '"+data+"' on element " + locator + "locator type: " + locatorType)

    def elementPresentCheck(self, locator, locatorType="id"):
        try:
            elementlist = self.driver.find_elements(locatorType, locator)
            if (len(elementlist) > 0):
                print(self.logTime() + "LOG - " + "Element found with locator: " + locator +
                      " locatorType: " + locatorType)
                return True
            else:
                print(self.logTime() + "LOG - " + "Element not found with locator: " + locator +
                      " locatorType: " + locatorType)
                return False
        except:
            print(self.logTime() + "EXCEPTION - " + "Element not found with locator: " + locator +
                  " locatorType: " + locatorType)
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFreq=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print(self.logTime() + "LOG - " + "Waiting for maximum :: " + str(timeout) + ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver,
                                 timeout,
                                 poll_frequency=pollFreq,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException
                                                     ]
                                 )
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print(self.logTime() + "LOG - " + "Element '" + locator + "' appered on the web page ")
        except:
            print(self.logTime() + "EXCEPTION - " + "Element '" + locator + "' NOT appeared on the web page")
        return element

    def take_Screenshot(self, driver):
        # fileName = str(round(time.time() * 1000)) + ".png"
        fileName = "snapShot.png"
        dir = "../screenshots/"
        driver.save_screenshot(dir + fileName)

    def mouseHover(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            print(self.logTime() + "LOG - " + "Mouse hover on element " + locator + "locator type: " + locatorType)
        except:
            print(self.logTime() + "ERROR - " + "Cannot Mouse hover  on element " + locator + "locator type: " + locatorType)

    def scrollToElement(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            print(self.logTime() + "LOG - " + " Scroll to element " + locator + "locator type: " + locatorType)
        except:
            print(self.logTime() + "ERROR - " + "Cannot scroll to element " + locator + "locator type: " + locatorType)

    def verifyTitle(self, titleTxt):
        if titleTxt in self.getTitle():
            print(self.logTime() + "LOG - " + "Page Title Verification PASSED: " + titleTxt)
            return True
        else:
            print(self.logTime() + "LOG - " + "Page Title Verification FAILED: " + titleTxt)
            return False

    def verifyURL(self, URLTxt):
        if URLTxt in self.getURL():
            print(self.logTime() + "LOG - " + "Page URL Verification PASSED: " + URLTxt)
            return True
        else:
            print(self.logTime() + "LOG - " + "Page URL Verification FAILED: " + URLTxt)
            return False

    def webScroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -800);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 800);")

    def switchToFrame(self, id="", name="", index=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                print(self.logTime() + "LOG - " + "Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                print(self.logTime() + "LOG - " + "Element :: '" + info + "' is enabled")
            else:
                print(self.logTime() + "LOG - " + "Element :: '" + info + "' is not enabled")
        except:
            print(self.logTime() + "ERROR - " + "Element :: '" + info + "' state could not be found")
        return enabled

    def logTime(self):
        return str(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S - "))

    def highLight(self, locator, locatorType, second, element=None):
        # Highlights a Selenium webdriver element
        if locator:
            element = self.getElement(locator, locatorType=locatorType)
        driver = self.driver
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)
        orignal_style = element.get_attribute('style')
        apply_style("border: 2px solid red")
        if (element.get_attribute("style") != None):
            time.sleep(second)
        apply_style(orignal_style)

    def sendKeysByActions(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            ActionChains(self.driver).send_keys_to_element(element, data).perform()
            print(self.logTime() + "LOG - " + "Sent data '"+data+"' on element with locator: " + locator +
                  " locatorType: " + locatorType)
        except:
            print(self.logTime() + "LOG - " + "Cannot send data '"+data+"' on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def elementClickByActions(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            ActionChains(self.driver).click(element).perform()
            print(self.logTime() + "LOG - " + "Clicked on element with locator: " + locator +
                  " locatorType: " + locatorType)
        except:
            print(self.logTime() + "EXCEPTION - " + "Cannot click on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def elementRightClickByActions(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            ActionChains(self.driver).context_click(element).perform()
            print(self.logTime() + "LOG - " + "Right_Clicked on element with locator: " + locator +
                  " locatorType: " + locatorType)
        except:
            print(self.logTime() + "EXCEPTION - " + "Cannot right_click on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def selectDropDownByValue(self, value, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            select = Select(element)
            select.select_by_value(value)
            print(self.logTime() + "LOG - " + "Selected value '"+value+"' on element " + locator +
                  "locator type: " + locatorType)
        except:
            print(self.logTime() + "EXCEPTION - " + "Cannot select value '"+value+"' on element " +
                  locator + "locator type: " + locatorType)

    def selectDropDownByVisibleText(self, text, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            Select(element).select_by_visible_text(text)
            print(
                self.logTime() + "LOG - " + "Selected text '" + text + "' on element " + locator +
                "locator type: " + locatorType)
        except:
            print(
                self.logTime() + "EXCEPTION - " + "Cannot select text '" + text + "' on element " +
                locator + "locator type: " + locatorType)

    def selectDropDownByOptionClick(self, text, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            for option in element.find_elements_by_tag_name('option'):
                if option.text == text:
                    option.click()
                    break
            print(
                self.logTime() + "LOG - " + "Selected text '" + text + "' on element " + locator +
                "locator type: " + locatorType)
        except:
            print(
                self.logTime() + "EXCEPTION - " + "Cannot select text '" + text + "' on element " + locator +
                "locator type: " + locatorType)