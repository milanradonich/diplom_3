import pytest

from pages.login_page import LoginPage
from pages.order_history_page import OrderHistory
from pages.profile_page import ProfilePage


class TestPersonalAccount:
    def test_check_click_personal_account_btn(self, setup_home_page):
        driver = setup_home_page
        click_btn = LoginPage(driver)
        assert click_btn.check_click_account()

    def test_login(self, setup_home_page):
        driver = setup_home_page
        login = LoginPage(driver)
        assert login.login_in_system()

    def test_check_history_link(self, setup_home_page):
        driver = setup_home_page
        history = OrderHistory(driver)
        assert history.check_history_link()

    def test_logout(self, setup_home_page):
        driver = setup_home_page
        logout = ProfilePage(driver)
        assert logout.check_logout()




