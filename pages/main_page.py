import time

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    class MainLocators:
        ACCOUNT = By.XPATH, "//a[@href='/account']"
        BTN_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'
        CONSTRUCTOR_LINK = By.XPATH, "//a[normalize-space()='Конструктор']"
        INGREDIENT = By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']"
        COUNTER = By.XPATH, ("//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, "
                             "'counter_counter__num__3nue1')]")
        BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"
        ORDER_MODAL = By.XPATH, "//p[text()='идентификатор заказа']"
        DETAILS_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")
        MODAL_INGREDIENT_CLOSE = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]"
        CLOSE_ORDER_MODAL = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_page_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_value(self, locator):
        value = self.driver.find_element(*locator)
        return value.text

    def find_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, timeout: int = 10):
        self.find_element(locator, timeout).click()

    def input_symbols(self, locator, text, timeout: int = 10):
        self.find_element(locator, timeout).send_keys(text)

    def click_account(self):
        self.click_element(self.MainLocators.ACCOUNT)

    def present_in_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_visible_url(self, locator, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(locator))
        return self.driver.current_url

    def visible_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.title("Проверка перехода по клику на «Конструктор»")
    @allure.description("Тест проверяет корректный переход в раздел «Конструктор» ")
    def check_constructor_transition(self):
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке конструктор"):
            self.click_element(self.MainLocators.CONSTRUCTOR_LINK)
        return self.get_current_url()

    @allure.title("Проверка счетчика ингредиента")
    @allure.description("Тест проверяет, что при добавлении ингредиента в заказ, увеличивается каунтер данного "
                        "ингредиента")
    def ingredient_counter_increases(self):
        with allure.step("Поиск ингредиента"):
            ingredient = self.find_element(self.MainLocators.INGREDIENT)
        with allure.step("Поиск корзины"):
            order_area = self.find_element(self.MainLocators.BASKET)
        with allure.step("Поиск счетчика ингредиента"):
            counter = self.find_element(self.MainLocators.COUNTER)
        with allure.step("Получение текущего значения счетчика ингредиента"):
            initial_count = int(counter.text)
        with allure.step("Инициализация ActionChains"):
            actions = ActionChains(self.driver)
        with allure.step("Перетаскивание элемента"):
            actions.drag_and_drop(ingredient, order_area).perform()
        with allure.step("Ожидание изменения значения счетчика"):
            WebDriverWait(self.driver, 10).until(
                lambda driver: int(self.find_element(self.MainLocators.COUNTER).text) == initial_count + 2
            )
        with allure.step("Получение нового значения счетчика ингредиента"):
            time.sleep(2)
            updated_count = int(self.find_element(self.MainLocators.COUNTER).text)
        with allure.step("Проверка нового значения счетчика ингредиента и старого"):
            if updated_count == initial_count + 2:
                return True
            else:
                return False

    @allure.title("Проверка открытия модального окна ингредиента")
    @allure.description("Тест проверяет, если кликнуть на ингредиент, появится всплывающее окно с деталями ")
    def check_open_ingredient_modal(self):
        with allure.step("Клик по ингредиенту"):
            self.click_element(self.MainLocators.INGREDIENT)
        with allure.step("поиск открывшегося модального окна"):
            if self.find_element(self.MainLocators.DETAILS_INGREDIENT):
                return True

    @allure.title("Проверка закрытия на крестик модального окна ингредиента")
    @allure.description("Тест проверяет, если кликнуть на крестик модального окна, оно закроется")
    def check_close_ingredient_modal(self):
        with allure.step("Клик по ингредиенту"):
            self.check_open_ingredient_modal()
        with allure.step("Клик по крестику модального окна"):
            self.click_element(self.MainLocators.MODAL_INGREDIENT_CLOSE)
        with allure.step("Проверка закрытия модального окна"):
            try:
                self.visible_element(self.MainLocators.MODAL_INGREDIENT_CLOSE)
                return True
            except NoSuchElementException:
                return False

