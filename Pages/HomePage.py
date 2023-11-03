from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage

from Utilities import configReader


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newCar_XPATH")
        self.click("findNewCars_XPATH")

        return NewCarsPage(self.driver)
    def goToCompareCars(self):
        pass

    def goToUsedCars(self):
        pass
