import pytest

from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    def test_password_recovery_by_click_recover_password(self, setup_home_page):
        driver = setup_home_page
        forgot_pass = ResetPasswordPage(driver)
        assert forgot_pass.click_icon_show_password()

    def test_transition_to_forgot_pass_page(self, setup_home_page):
        driver = setup_home_page
        page = ForgotPasswordPage(driver)
        assert page.transition_to_forgot_password_page()

    def test_check_click_recovery_btn(self, setup_home_page):
        driver = setup_home_page
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.check_click_recovery_btn()
        assert driver.current_url == reset_password_page.ResetPasswordLocators.RESET_PASS_PAGE

