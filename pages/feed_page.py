import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


class FeedPage(MainPage):
    class FeedLocators:
        ORDERS_LINK = By.XPATH, "//a[normalize-space()='Лента Заказов']"
        FEED_PAGE = 'https://stellarburgers.nomoreparties.site/feed'
        ORDER_CARDS = By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li/a"
        MODAL_CLOSE = By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button'
        MODAL_WINDOW = By.CSS_SELECTOR, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]"

    def __init__(self, driver):
        super().__init__(driver)

    def check_click_feed(self):
        self.click_element(self.FeedLocators.ORDERS_LINK)
        return self.get_current_url()

    def click_on_order_card(self):
        self.check_click_feed()
        time.sleep(2)
        self.click_element(self.FeedLocators.ORDER_CARDS)
        time.sleep(2)

    def close_order_card(self):
        self.click_on_order_card()
        self.click_element(self.FeedLocators.MODAL_CLOSE)
        try:
            self.visible_element(self.FeedLocators.MODAL_CLOSE)
            return True
        except NoSuchElementException:
            return False

