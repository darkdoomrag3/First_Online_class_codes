from selenium.webdriver.common.by import By

from Utilities import configReader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_elements(By.XPATH,configReader.readConfig("locators", "carTitle_XPATH")).text

    def getCarNameAndPrices(self):
        carNames = self.driver.find_elements(By.XPATH,configReader.readConfig("locators", "carName_XPATH"))
        carPrices = self.driver.find_elements(By.XPATH,configReader.readConfig("locators", "carPrice_XPATH"))

        for i in range(1, len(carPrices)):
            print(carNames[i].text+"----Prices are-----"+carPrices[i].text)


