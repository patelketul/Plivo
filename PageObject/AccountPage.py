from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class AccountPage(BasePage):

    basePage = BasePage()
    paymentsLink = (By.LINK_TEXT,"Payments")

    def isPaymentsLinkPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.paymentsLink)

    def clickPaymentsLink(self,driver):
        self.basePage.waitAndClick(driver,self.paymentsLink)

