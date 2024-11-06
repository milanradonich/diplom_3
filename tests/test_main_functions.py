import pytest

import database
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunction:
    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_constructor_transition(self, driver_setup, setup_home_page):
        driver = setup_home_page
        click_btn = MainPage(driver)
        current_url = click_btn.check_constructor_transition()
        expected_url = database.BASE_URL
        assert current_url == expected_url

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_click_feed(self, driver_setup, setup_home_page):
        driver = setup_home_page
        click_btn = FeedPage(driver)
        current_url = click_btn.check_click_feed()
        expected_url = FeedPage.FeedLocators.FEED_PAGE
        assert current_url == expected_url

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_open_ingredient_modal(self, driver_setup, setup_home_page):
        driver = setup_home_page
        click_ingredient = MainPage(driver)
        assert click_ingredient.check_open_ingredient_modal()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_close_ingredient_modal(self, driver_setup, setup_home_page):
        driver = setup_home_page
        close_ingredient_modal = MainPage(driver)
        assert close_ingredient_modal.check_close_ingredient_modal()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_ingredient_counter_increases(self, driver_setup, setup_home_page):
        driver = setup_home_page
        add_ingredient = MainPage(driver)
        assert add_ingredient.ingredient_counter_increases()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_create_order_auth_user(self, driver_setup, setup_home_page):
        driver = setup_home_page
        create_order = LoginPage(driver)
        assert create_order.create_order_auth_user()


