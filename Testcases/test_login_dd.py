import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseurl = "https://admin-demo.nopcommerce.com"
    path = ".//Test Data//testData.xlsx"
    logger = LogGen.loggen()




    def test_dd(self,setup):

        self.logger.info("****** Test_002_DDT_Login *******")
        self.logger.info("****** verifying test_dd  *******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("maximum number of rows are : ", self.rows)
        self.col = XLUtils.getColumnCount(self.path, "Sheet1")
        print("Number of columns are : ", self.col)

        list_status= []

        for r in range(2, self.rows+1):
            self.user = XLUtils.ReadData(self.path, "Sheet1", r, 1)
            self.passwd = XLUtils.ReadData(self.path,"Sheet1", r ,2)
            self.status = XLUtils.ReadData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.passwd)
            self.lp.ClickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                self.logger.info("*** Test passed** ")
                if self.status == "pass":
                    self.lp.ClickLogout()
                    list_status.append(self.status)
                elif self.status== "Fail":
                    self.logger.info("**** Test Failed *******")
                    self.lp.ClickLogout()
                    list_status.append(self.status)
            elif act_title!= exp_title:
                if self.status== "pass":
                    self.logger.info("*** failed ****")
                    list_status.append(self.status)
                elif self.status == "fail":
                    self.logger.info("*** passed ****")
                    list_status.append(self.status)
        if "Fail" not in list_status:
            self.logger.info("*****  test_dd passed *** ")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****  test_dd Failed *** ")
            self.driver.close()
            assert False
        self.logger.info("End of the test case")











































