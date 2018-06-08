from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

class BasePage():

    #wait for element to render on screen
    #Phantomjs has some issues with visibility_of_element_located. Added try-except statement to handle the issue
    def waitForElement(self, driver,locator,wait=30):
        try:
            return WebDriverWait(driver, wait).until(EC.visibility_of_element_located(locator))
        except:
            return WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator))


    def waitForAllElements(self,driver,locator,wait=30):
        try:
            return WebDriverWait(driver,wait).until(EC.visibility_of_all_elements_located(locator))
        except:
            return WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located(locator))

    #Get element
    def getElement(self, driver,locator,wait=30):
        try:
            return WebDriverWait(driver, wait).until(EC.visibility_of_element_located(locator))
        except:
            return WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator))


    def waitForElementToBeClickable(self,driver,locator,wait=30):
        WebDriverWait(driver,wait).until(EC.element_to_be_clickable(locator))

    def waitForElementToBeInvisible(self, driver, locator, wait=30):
        WebDriverWait(driver, wait).until(EC.invisibility_of_element_located(locator))

    #Wait for element to render and click
    def waitAndClick(self,driver,locator):
        self.waitForElement(driver,locator)
        self.waitForElementToBeClickable(driver,locator)
        self.getElement(driver,locator).click()

    #Wait for element to render and type text
    def waitAndType(self,driver,text,locator):
        self.waitForElement(driver,locator)
        self.waitForElementToBeClickable(driver,locator)
        self.getElement(driver,locator).send_keys(text)

    #Check if element is present on the page or not.
    # If present return true or return false
    def isElementPresent(self,driver,locator,wait=30):
        try:
            self.waitForElement(driver,locator,wait)
            self.getElement(driver,locator).is_displayed()
            return True
        except:
            return False

    #Check if element is displayed or not
    def isElementDisplayed(self,element):
        return element.is_displayed()

    #Return text from element
    def getElementText(self,element):
        return element.get_attribute('textContent')#element.text





