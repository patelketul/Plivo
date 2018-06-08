from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class LoginPage(BasePage):

    basePage = BasePage()
    emailTextbox = (By.ID,"id_username")
    passwordTextbox = (By.ID, "id_password")
    loginButton = (By.ID,"login-sub")

    def isEmailTextboxPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.emailTextbox)

    def isPassworkTextboxPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.passwordTextbox)

    def isLoginButtonPresent(self,driver):
        return self.basePage.isElementPresent(driver,self.loginButton)

    def typeUsername(self,driver,username):
        self.basePage.waitAndType(driver,username,self.emailTextbox)

    def typePassword(self,driver,password):
        self.basePage.waitAndType(driver,password,self.passwordTextbox)

    def clickLoginButton(self,driver):
        self.basePage.waitAndClick(driver,self.loginButton)

    def loginToPlivo(self,driver,username,password):
        self.basePage.waitAndType(driver,username,self.emailTextbox)
        self.basePage.waitAndType(driver,password,self.passwordTextbox)
        self.basePage.waitAndClick(driver,self.loginButton)


