import time

import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage


class ProfilePage(MainPage):
    class ProfileLocators:
        PROFILE_PAGE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
        BTN_LOGOUT = By.XPATH, '//button[text()="Выход"]'
        HISTORY_LINK = By.XPATH, '//a[@href="/account/order-history"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    @allure.title("Проверка перехода в раздел «История заказов»")
    @allure.description("Тест проверяет переход в раздел «История заказов» в ЛК")
    def check_history_link(self):
        with allure.step("Процедура логина в систему"):
            self.login_page.login_in_system()
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке История заказов"):
            self.click_element(self.ProfileLocators.HISTORY_LINK)

    def click_history_link(self):
        self.click_account()
        self.click_element(self.ProfileLocators.HISTORY_LINK)

    def click_logout(self):
        self.click_element(self.ProfileLocators.BTN_LOGOUT)

    @allure.title("Проверка выхода из аккаунта")
    @allure.description("Тест проверяет успешный выход из аккаунта")
    def check_logout(self):
        with allure.step("Процедура логина в систему"):
            self.login_page.login_in_system()
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке выход"):
            self.click_logout()
        with allure.step("Получение актуального URL"):
            current_url = self.wait_visible_url(LoginPage.LoginLocators.LOGIN_PAGE)
        with allure.step("Сравнение ОР и ФР URL"):
            return current_url == LoginPage.LoginLocators.LOGIN_PAGE



