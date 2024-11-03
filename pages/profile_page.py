import time

from selenium.webdriver.common.by import By
from database import BASE_URL
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

    def click_history_link(self):
        self.login_page.login_in_system()
        self.click_account()
        self.click_element(self.ProfileLocators.HISTORY_LINK)

    def click_logout(self):
        self.click_element(self.ProfileLocators.BTN_LOGOUT)

    def check_logout(self):
        self.login_page.login_in_system()
        self.click_account()
        time.sleep(2)
        self.click_logout()
        time.sleep(2)
        return self.get_current_url()



