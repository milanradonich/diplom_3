from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage


class LoginPage(HeaderPage):
    class LoginLocators:
        RECOVER_PASSWORD_LINK = By.XPATH, "//a[text()='Восстановить пароль']"

    def __init__(self, driver):
        super().__init__(driver)

    def input_symbols(self, locator, text, timeout: int = 10):
        self.find_element(locator, timeout).send_keys(text)

    def click_recovery_pass(self):
        self.click_element(self.LoginLocators.RECOVER_PASSWORD_LINK)

