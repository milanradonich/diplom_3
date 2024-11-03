import database
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistory
from pages.profile_page import ProfilePage


class TestMainFunction:
    def test_check_constructor_transition(self, setup_home_page):
        driver = setup_home_page
        click_btn = MainPage(driver)
        current_url = click_btn.check_constructor_transition()
        expected_url = database.BASE_URL
        assert current_url == expected_url

    def test_check_click_feed(self, setup_home_page):
        driver = setup_home_page
        click_btn = FeedPage(driver)
        current_url = click_btn.check_click_feed()
        expected_url = FeedPage.FeedLocators.FEED_PAGE
        assert current_url == expected_url

    def test_click_on_order_card(self, setup_home_page):
        driver = setup_home_page
        click_card = FeedPage(driver)
        click_card.click_on_order_card()

    def test_close_order_card(self, setup_home_page):
        driver = setup_home_page
        close_card = FeedPage(driver)
        assert close_card.close_order_card()

    def test_ingredient_counter_increases(self, setup_home_page):
        driver = setup_home_page
        add_ingredient = MainPage(driver)
        add_ingredient.ingredient_counter_increases()