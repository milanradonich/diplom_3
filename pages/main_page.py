import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from database import BASE_URL


class MainPage:
    class MainLocators:
        ACCOUNT = By.XPATH, "//a[@href='/account']"
        BTN_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'
        CONSTRUCTOR_LINK = By.XPATH, "//a[normalize-space()='Конструктор']"
        INGREDIENT = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"
        COUNTER = By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d']"
        BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    def find_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator, timeout: int = 10):
        self.find_element(locator, timeout).click()

    def input_symbols(self, locator, text, timeout: int = 10):
        self.find_element(locator, timeout).send_keys(text)

    def click_account(self):
        self.click_element(self.MainLocators.ACCOUNT)

    def present_in_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_visible_url(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(locator))

    def visible_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def check_constructor_transition(self):
        self.click_account()
        time.sleep(2)
        self.click_element(self.MainLocators.CONSTRUCTOR_LINK)
        time.sleep(2)
        return self.get_current_url()

    def ingredient_counter_increases(self):
        ingredient = self.find_element(self.MainLocators.INGREDIENT)
        counter = ingredient.find_element(self.MainLocators.COUNTER)
        initial_count = int(counter.text)
        order_area = self.find_element(self.MainLocators.BASKET)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, order_area).perform()
        WebDriverWait(self.driver, 10).until(
            lambda driver: int(ingredient.find_element(self.MainLocators.COUNTER).text) == initial_count + 2
        )
        updated_count = int(ingredient.find_element(self.MainLocators.COUNTER).text)
        assert updated_count == initial_count + 2

