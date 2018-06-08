from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class MainDashboardPage(BasePage):

    basePage = BasePage()
    accountLink = (By.LINK_TEXT,"Account")

    def isAccountLinkPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.accountLink)

    def clickAccountLink(self,driver):
        self.basePage.waitAndClick(driver,self.accountLink)

