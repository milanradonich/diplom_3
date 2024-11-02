from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    def test_password_recovery_by_click_recover_password(self, setup_home_page):
        driver = setup_home_page
        forgot_pass = ResetPasswordPage(driver)
        assert forgot_pass.click_icon_show_password()
