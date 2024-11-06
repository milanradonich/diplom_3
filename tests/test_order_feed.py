import pytest

from pages.feed_page import FeedPage


class TestOrderFeed:
    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_click_on_order_card(self, driver_setup, setup_home_page):
        driver = setup_home_page
        click_card = FeedPage(driver)
        assert click_card.click_on_order_card()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_close_order_card(self, driver_setup, setup_home_page):
        driver = setup_home_page
        close_card = FeedPage(driver)
        assert close_card.close_order_card()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_user_order_show_in_feed(self, driver_setup, setup_home_page):
        driver = setup_home_page
        check_order = FeedPage(driver)
        assert check_order.user_order_show_in_feed()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_when_create_new_order_all_time_counter_increases(self, driver_setup, setup_home_page):
        driver = setup_home_page
        counter_increased = FeedPage(driver)
        assert counter_increased.when_create_new_order_all_time_counter_increases()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_when_create_new_order_today_time_counter_increases(self, driver_setup, setup_home_page):
        driver = setup_home_page
        counter_increased = FeedPage(driver)
        assert counter_increased.when_create_new_order_today_time_counter_increases()

    @pytest.mark.parametrize("driver_setup", ["chrome", "firefox"], indirect=True)
    def test_check_order_in_processing(self, driver_setup, setup_home_page):
        driver = setup_home_page
        id_order = FeedPage(driver)
        assert id_order.check_order_in_processing()

