import pytest

from pages.login_page import LoginPage
from pages.order_history_page import OrderHistory
from pages.profile_page import ProfilePage


class TestPersonalAccount:
    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_click_personal_account_btn(self, driver_setup, setup_home_page):
        driver = setup_home_page
        click_btn = LoginPage(driver)
        assert click_btn.check_click_account()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_login(self, driver_setup, setup_home_page):
        driver = setup_home_page
        login = LoginPage(driver)
        assert login.login_in_system()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_history_link(self, driver_setup, setup_home_page):
        driver = setup_home_page
        history = OrderHistory(driver)
        assert history.check_history_link()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_logout(self, driver_setup, setup_home_page):
        driver = setup_home_page
        logout = ProfilePage(driver)
        assert logout.check_logout()




