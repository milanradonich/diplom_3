import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class OrderHistory(MainPage):
    class OrderHistoryLocators:
        ORDER_HISTORY_URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
        BTN_LOGOUT = By.XPATH, '//button[text()="Выход"]'
        HISTORY_LINK = By.XPATH, '//a[@href="/account/order-history"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_page = ProfilePage(driver)
        self.login_page = LoginPage(driver)

    def go_to_history_page(self):
        self.profile_page.click_history_link()




