import time

from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def fillForm(self, username, password):
        self.click("Desktop_username_CSS")
        self.type("username_XPATH", username)
        self.click("afterPhone_button_XPATH")
        time.sleep(5)
        self.click("enterButton_CSS")
        self.type("password_ID", password)
        self.click("loginButton_XPATH")
