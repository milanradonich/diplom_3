
import allure
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.profile_page import ProfilePage


class OrderHistory(BasePage):
    class OrderHistoryLocators:
        ORDER_HISTORY_URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
        BTN_LOGOUT = By.XPATH, '//button[text()="Выход"]'
        HISTORY_LINK = By.XPATH, '//a[@href="/account/order-history"]'
        LAST_ORDER = By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[last()]"
        ORDER_NUMBER = By.XPATH, "//p[@class='text text_type_digits-default']"

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_page = ProfilePage(driver)
        self.login_page = LoginPage(driver)

    @allure.title("Проверка перехода в раздел «История заказов»")
    @allure.description("Тест проверяет переход в раздел «История заказов» в ЛК")
    def check_history_link(self):
        with allure.step("Процедура логина в систему"):
            self.login_page.login_in_system()
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке История заказов"):
            self.click_element(self.profile_page.ProfileLocators.HISTORY_LINK)
        with allure.step("Получение актуального URL"):
            current_url = self.get_current_url()
        with allure.step("Получение ожидаемого URL"):
            expected_url = self.OrderHistoryLocators.ORDER_HISTORY_URL
        with allure.step("Сравнение ОР и ФР URL"):
            return current_url == expected_url

    def check_history_order(self):
        self.scroll_page_to_element(self.OrderHistoryLocators.LAST_ORDER)
        return self.get_value(self.OrderHistoryLocators.ORDER_NUMBER)


