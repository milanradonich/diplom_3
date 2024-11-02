from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HeaderPage:
    class HeaderLocators:
        ACCOUNT = By.XPATH, "//a[@href='/account']"  # личный кабинет

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def wait_visible_header(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def find_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator, timeout: int = 10):
        self.find_element(locator, timeout).click()

    def click_account(self):
        self.click_element(self.HeaderLocators.ACCOUNT)

    def present_in_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_visible_url(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(locator))

