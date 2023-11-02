from Pages.BasePage import BasePage
from Utilities import configReader


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def goToNewCars(self):
        self.moveTo("NewCars_XPATH")
        self.click("FindNewCars_XPATH")
        pass
    def goToCompareCars(self):
        pass

    def goToUsedCars(self):
        pass

