from pages.header_page import HeaderPage
from locators.login_locators import LoginLocators


class LoginPage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_symbols(self, locator, text, timeout: int = 10):
        self.find_element(locator, timeout).send_keys(text)

    def click_recovery_pass(self):
        self.click_element(LoginLocators.RECOVER_PASSWORD_LINK)
