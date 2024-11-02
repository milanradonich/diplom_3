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

    def input_active(self):
        try:
            self.present_in_element(ResetPasswordLocators.NEW_PASSWORD_INPUT_TEXT)
            return True
        except:
            return False

    def set_new_password(self):
        time.sleep(2)
        self.click_account()
        time.sleep(2)
        self.click_recovery_pass()
        time.sleep(2)
        self.enter_email_and_click_recovery()
        time.sleep(2)
        self.input_new_password()
        time.sleep(2)
        self.click_to_svg()
        time.sleep(2)
        return self.input_active()
