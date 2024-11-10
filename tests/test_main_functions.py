import pytest

import database
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.base_page import BasePage


class TestMainFunction:
    def test_check_constructor_transition(self, setup_home_page):
        driver = setup_home_page
        click_btn = BasePage(driver)
        current_url = click_btn.check_constructor_transition()
        expected_url = database.BASE_URL
        assert current_url == expected_url

    def test_check_click_feed(self, setup_home_page):
        driver = setup_home_page
        click_btn = FeedPage(driver)
        current_url = click_btn.check_click_feed()
        expected_url = FeedPage.FeedLocators.FEED_PAGE
        assert current_url == expected_url

    def test_check_open_ingredient_modal(self, setup_home_page):
        driver = setup_home_page
        click_ingredient = BasePage(driver)
        assert click_ingredient.check_open_ingredient_modal()

    def test_check_close_ingredient_modal(self, setup_home_page):
        driver = setup_home_page
        close_ingredient_modal = BasePage(driver)
        assert close_ingredient_modal.check_close_ingredient_modal()

    def test_ingredient_counter_increases(self, setup_home_page):
        driver = setup_home_page
        add_ingredient = BasePage(driver)
        assert add_ingredient.ingredient_counter_increases()

    def test_create_order_auth_user(self, setup_home_page):
        driver = setup_home_page
        create_order = LoginPage(driver)
        assert create_order.create_order_auth_user()


