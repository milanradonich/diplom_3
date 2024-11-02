import time

from locators.reset_password_locators import ResetPasswordLocators
from pages.forgot_password_page import ForgotPasswordPage


class ResetPasswordPage(ForgotPasswordPage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_new_password(self):
        self.input_symbols(ResetPasswordLocators.NEW_PASSWORD_INPUT, '1234')

    def click_to_svg(self):
        self.click_element(ResetPasswordLocators.ICON_SVG)

    def set_new_password(self):
        self.click_account()
        self.click_recovery_pass()
        self.enter_email_and_click_recovery()
        self.input_new_password()
        self.click_to_svg()

