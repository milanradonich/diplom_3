from locators.forgot_password_locators import ForgotPasswordLocators
from pages.login_page import LoginPage


class ForgotPasswordPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email):
        self.input_symbols(ForgotPasswordLocators.EMAIL_LABEL, email)

    def click_recovery(self):
        self.click_element(ForgotPasswordLocators.RECOVERY_BUTTON)

    def enter_email_and_click_recovery(self):
        self.input_email('milan_radonich13@yandex.ru')
        self.click_recovery()




