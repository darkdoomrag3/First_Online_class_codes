import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import configReader,dataProvider
import logging
from Utilities.logUTI import Logger

log = Logger(__name__, logging.INFO)


class Test_CareWale(BaseTest):


    def test_gotoNewCar(self):
        log.logger.info("******Inside New Car Test*********")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)


    @pytest.mark.parametrize("carBrand,carTitle",
                             dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is : ", carBrand)
        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

    @pytest.mark.parametrize("carBrand,carTitle",
                             dataProvider.get_data("NewCarsTest"))
    def test_printCarNamesandPrices(self, carBrand, carTitle):
        log.logger.info("******Inside Car Names and Prices Test*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is : ", carBrand)
        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
