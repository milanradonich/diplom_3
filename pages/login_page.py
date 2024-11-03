import time

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

    def login_in_system(self):
        self.click_account()
        self.input_symbols(self.LoginLocators.EMAIL_INPUT, MyAcc.EMAIL)
        self.input_symbols(self.LoginLocators.PASSWORD_INPUT, MyAcc.PASSWORD)
        self.click_element(self.LoginLocators.BTN_LOGIN)
        return self.present_in_element(self.MainLocators.BTN_ORDER)
