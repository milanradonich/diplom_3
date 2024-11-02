from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.header_page import HeaderPage
from locators.header_locators import HeaderLocators


class TestPasswordRecovery:
    def test_password_recovery_by_click_recover_password(self, setup_home_page):
        driver = setup_home_page
        forgot_pass = ResetPasswordPage(driver)
        assert forgot_pass.set_new_password() == True
