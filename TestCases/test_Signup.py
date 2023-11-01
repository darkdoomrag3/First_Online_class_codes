import pytest

from Pages.registrationPage import RegistrationPage
from TestCases.BaseTest import BaseTest
from TestCases.conftest import get_browser
from Utilities.dataProvider import get_data


# @pytest.fixture()
# def log_on_failure(request, chrome_browser):
#     driver = chrome_browser
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="report", attachment_type=AttachmentType.PNG)
#



class Test_SignUp(BaseTest):



    @pytest.mark.parametrize("username,password", get_data())
    def test_doSignup(self, username, password):

        regPage = RegistrationPage(self.driver)
        regPage.fillForm(username, password)
