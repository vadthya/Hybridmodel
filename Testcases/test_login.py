import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_001_Login:
    baseurl = "https://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin"

    logger = LogGen.loggen()




    def test_homepagetitle(self,setup):
        self.logger.info("********************* test_homepagetitle ***************** ")
        self.logger.info("********************* Verifying test_homepagetitle ***************** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("********************* Passed successfully ***************** ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.logger.error("********************* Failed test_homepagetitle ***************** ")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.logger.info("********************* test_login ***************** ")
        self.logger.info("********************* verifying test_login ***************** ")

        self.driver = setup

        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.remeberMe()
        self.lp.ClickLogin()

        title2 = self.driver.title



        if title2 == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********************* passed successfully  ***************** ")
            self.driver.close()


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("********************* Failed test_login ***************** ")
            self.driver.close()
            assert False










