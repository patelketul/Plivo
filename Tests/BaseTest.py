from selenium import webdriver

class BaseTest():

    def startDriver(self,browser):

        if browser == "chrome":
            return webdriver.Chrome(executable_path="../conf/chromedriver")

        if browser == "firefox":
            return webdriver.Firefox(executable_path="../conf/geckodriver")

