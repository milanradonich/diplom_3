from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_visible_header(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def find_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator, timeout: int = 10):
        self.find_element(locator, timeout).click()

    def click_account(self):
        self.click_element(HeaderLocators.ACCOUNT)

    def present_in_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))



