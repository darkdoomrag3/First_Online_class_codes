from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pytest
import allure
from allure_commons.types import AttachmentType
from Utilities import configReader

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def chrome_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(configReader.readConfig("basic info","testurl"))
    yield
    driver.quit()

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)



@pytest.fixture(params=["firefox", "chrome"], scope="function")
def get_browser(request):


    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver= driver
    # driver.set_window_size(390, 844)
    driver.maximize_window()
    driver.get(configReader.readConfig("basic info","testurl"))

    driver.implicitly_wait(10)
    yield driver
    driver.quit()




# # don't forget to set up pycharm pytest config python interpreter and pytest.ini env
# @pytest.fixture(scope="function", params=["chrome", "firefox"])
# def get_browser(request):
#     global driver
#     if request.param == "chrome":
#         driver = webdriver.Remote(
#             command_executor='http://localhost:4444/wd/hub',
#             options=webdriver.ChromeOptions()
#         )
#     if request.param == "firefox":
#         driver = webdriver.Remote(
#             command_executor='http://localhost:4444/wd/hub',
#             options=webdriver.FirefoxOptions()
#         )
#     driver.maximize_window()
#     driver.get("https://google.com")
#     driver.quit()
