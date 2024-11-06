import pytest

from selenium import webdriver
from database import *


class WebdriverFactory:
    @staticmethod
    def getwebdriver(browsername):
        if browsername == "firefox":
            return webdriver.Firefox()
        elif browsername == "chrome":
            return webdriver.Chrome()


@pytest.fixture(scope="function")
def driver_setup(request):
    browser_name = request.param
    driver = WebdriverFactory.getwebdriver(browser_name)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def setup_home_page(driver_setup):
    driver = driver_setup
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
