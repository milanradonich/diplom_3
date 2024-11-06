
import allure
from selenium.webdriver.common.by import By

from database import MyAcc
from pages.main_page import MainPage


class LoginPage(MainPage):
    class LoginLocators:
        LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
        RECOVER_PASSWORD_LINK = By.XPATH, "//a[text()='Восстановить пароль']"
        BTN_LOGIN = By.XPATH, '//button[text()="Войти"]'                                # кнопка войти при авторизации
        INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'  # поле ввода пароля
        EMAIL_INPUT = By.XPATH, "//input[@type='text' and @name='name']"                # поле ввода почты
        PASSWORD_INPUT = By.XPATH, '//input[@type="password" and @name="Пароль"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_recovery_pass(self):
        self.click_element(self.LoginLocators.RECOVER_PASSWORD_LINK)

    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    @allure.description("Тест проверяет, что по клику на «Личный кабинет» попадем на страницу ЛК")
    def check_click_account(self):
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Получение актуального URL"):
            current_url = self.get_current_url()
        with allure.step("Получение ожидаемого URL"):
            expected_url = LoginPage.LoginLocators.LOGIN_PAGE
        with allure.step("Сравнение ОР и ФР URL"):
            return current_url == expected_url

    @allure.title("Процедура входа в систему")
    def login_in_system(self):
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Ввод email"):
            self.input_symbols(self.LoginLocators.EMAIL_INPUT, MyAcc.EMAIL)
        with allure.step("Ввод пароля"):
            self.input_symbols(self.LoginLocators.PASSWORD_INPUT, MyAcc.PASSWORD)
        with allure.step("Клик по кнопке войти"):
            self.click_element(self.LoginLocators.BTN_LOGIN)
        with allure.step("Получение локатора кнопки Оформить заказ"):
            return self.present_in_element(self.MainLocators.BTN_ORDER)

    @allure.title("Проверка,что залогиненный пользователь может оформить заказ")
    @allure.description("Тест проверяет, успешное оформление заказа залогининым юзером")
    def create_order_auth_user(self):
        with allure.step("Процедура входа в систему"):
            self.login_in_system()
        with allure.step("Добавление товара в корзину"):
            self.ingredient_counter_increases()
        with allure.step("Клик по кнопке оформить заказ"):
            self.click_element(self.MainLocators.BTN_ORDER)
        with allure.step("Проверяем, что появилось окно заказа"):
            if self.find_element(self.MainLocators.ORDER_MODAL):
                return True
