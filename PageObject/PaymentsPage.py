from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class PaymentsPage(BasePage):

    basePage = BasePage()
    redeemLink = (By.LINK_TEXT,"Redeem a coupon code instead")
    redeemCouponModal = (By.ID,"myModal")
    couponTextbox = (By.ID,"coupon")
    submitButton = (By.LINK_TEXT,"Submit")

    messageText = (By.XPATH,"//*[@id='myModal']//div[contains(@class,'alert')]")

    def isRedeemLinkPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.redeemLink)

    def clickRedeemLink(self,driver):
        self.basePage.waitAndClick(driver,self.redeemLink)

    def isRedeemCouponModalPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.redeemCouponModal)

    def isCouponTextboxPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.couponTextbox)

    def isSubmitButtonpresent(self,driver):
        return self.basePage.isElementPresent(driver,self.submitButton)

    def enterCouponCode(self,driver,couponcode):
        self.basePage.waitAndType(driver,couponcode,self.couponTextbox)

    def clickSubmitButton(self,driver):
        self.basePage.waitAndClick(driver,self.submitButton)

    def wasCouponProcessed(self,driver):
        return self.basePage.isElementPresent(driver,self.messageText)

    def getMessageText(self,driver):
        return self.basePage.getElementText(self.basePage.getElement(driver,self.messageText))