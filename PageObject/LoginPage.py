class LoginPage:
    textbox_username_id = "Email"
    testbox_password_id = "Password"
    textbox_remeberme_id = "RememberMe"
    Loginclick_xpath = "//button[text()='Log in']"
    logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element_by_id(self.testbox_password_id).clear()
        self.driver.find_element_by_id(self.testbox_password_id).send_keys(password)


    def remeberMe(self):
        self.driver.find_element_by_id(self.textbox_remeberme_id).click()





    def ClickLogin(self):
        self.driver.find_element_by_xpath(self.Loginclick_xpath).click()


    def ClickLogout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()
