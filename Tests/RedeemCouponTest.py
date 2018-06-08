import json, unittest, sys,os
sys.path.append(str((os.path.abspath(__file__))).split("Plivo")[0]+"Plivo")
from PageObject.LoginPage import LoginPage
from PageObject.MainDashboardPage import MainDashboardPage
from PageObject.AccountPage import AccountPage
from PageObject.PaymentsPage import PaymentsPage
from BaseTest import BaseTest


class RedeemCouponTest(unittest.TestCase):

    loginPage = LoginPage()
    mainDashboardPage = MainDashboardPage()
    accountPage = AccountPage()
    paymentsPage = PaymentsPage()
    baseTest = BaseTest()
    config = json.loads(open('../conf/config.json').read())

    def __init__(self,testname,browser):
        super(RedeemCouponTest, self).__init__(testname)
        self.browser = browser

    def setUp(self):
        self.driver = self.baseTest.startDriver(self.browser)#webdriver.Chrome("../conf/chromedriver")
        self.driver.get(self.config["url"])

    def test_RedeemCoupon(self):
        self.assertTrue(self.loginPage.isEmailTextboxPresent(self.driver),"Email textbox is not present")
        self.assertTrue(self.loginPage.isPassworkTextboxPresent(self.driver),"Password textbox is not present")
        self.assertTrue(self.loginPage.isLoginButtonPresent(self.driver),"Login button is not present")

        self.loginPage.loginToPlivo(self.driver,self.config["username"],self.config["password"])

        self.assertTrue(self.mainDashboardPage.isAccountLinkPresent(self.driver),"Account link is not present")

        self.mainDashboardPage.clickAccountLink(self.driver)

        self.assertTrue(self.accountPage.isPaymentsLinkPresent(self.driver),"Paymants link is not present")

        self.accountPage.clickPaymentsLink(self.driver)

        self.assertTrue(self.paymentsPage.isRedeemLinkPresent(self.driver),"Redeem coupon code link is not present")

        self.paymentsPage.clickRedeemLink(self.driver)

        self.assertTrue(self.paymentsPage.isRedeemCouponModalPresent(self.driver),"Redeem coupon code modal is not present")
        self.assertTrue(self.paymentsPage.isCouponTextboxPresent(self.driver),"Coupon code textbox is not present")
        self.assertTrue(self.paymentsPage.isSubmitButtonpresent(self.driver),"Submit button is not present")

        self.paymentsPage.enterCouponCode(self.driver,self.config["couponcode"])
        self.paymentsPage.clickSubmitButton(self.driver)

        #Since we don't have valid coupon code, here we assume system always throw error message for invalid coupon code.
        #Test case is marked as fail if failure message is not displayed

        self.assertTrue(self.paymentsPage.wasCouponProcessed(self.driver),"Coupon was not processed. System did not show any message")
        self.assertTrue(self.paymentsPage.getMessageText(self.driver)==self.config["errorMessage"],"Coupon code was valid")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    args = sys.argv

    test_loader = unittest.TestLoader()
    test_names = test_loader.getTestCaseNames(RedeemCouponTest)

    suite = unittest.TestSuite()
    for test_name in test_names:
        suite.addTest(RedeemCouponTest(test_name,args[1]))

    result = unittest.TextTestRunner().run(suite)