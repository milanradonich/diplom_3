import database
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistory
from pages.profile_page import ProfilePage


class TestPersonalAccount:
    def test_check_click_personal_account_btn(self, setup_home_page):
        driver = setup_home_page
        click_btn = MainPage(driver)
        click_btn.click_account()
        current_url = click_btn.get_current_url()
        expected_url = LoginPage.LoginLocators.LOGIN_PAGE
        assert current_url == expected_url

    def test_login(self, setup_home_page):
        driver = setup_home_page
        login = LoginPage(driver)
        assert login.login_in_system()

    def test_go_to_history_page(self, setup_home_page):
        driver = setup_home_page
        history = OrderHistory(driver)
        assert history.go_to_history_page()

    def test_logout(self, setup_home_page):
        driver = setup_home_page
        logout = ProfilePage(driver)
        current_url = logout.check_logout()
        assert current_url == LoginPage.LoginLocators.LOGIN_PAGE



