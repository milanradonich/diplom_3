
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistory
from pages.profile_page import ProfilePage


class FeedPage(MainPage):
    class FeedLocators:
        ORDERS_LINK = By.XPATH, "//a[normalize-space()='Лента Заказов']"
        FEED_PAGE = 'https://stellarburgers.nomoreparties.site/feed'
        ORDER_CARDS = By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li/a"
        MODAL_CLOSE = By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button'
        MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]"
        COMPOSITION_LOCATOR = By.CSS_SELECTOR, "p.text.text_type_main-medium.mb-8"
        ORDER_NUMBER = By.XPATH, "//p[@class='text text_type_digits-default']"
        ORDER_COUNT_ALL_TIME = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
        ORDER_COUNT_TODAY_TIME = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
        CLOSE_ORDER_MODAL = By.XPATH, "//button[@type='button' and contains(@class, 'Modal_modal__close')]"
        ORDER_ID = By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]"
        ID_ORDER_IN_PROCESS = By.XPATH, ("//ul[contains(@class, 'OrderFeed_orderListReady__1YFem "
                                         "OrderFeed_orderList__cBvyi')]//li[contains(@class, "
                                         "'text text_type_digits-default')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)
        self.click_history = ProfilePage(driver)
        self.history_page = OrderHistory(driver)

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    @allure.description("Тест проверяет корректный переход в раздел «Лента заказов»")
    def check_click_feed(self):
        with allure.step("Клик по кнопке Лента заказов"):
            self.click_element(self.FeedLocators.ORDERS_LINK)
        return self.get_current_url()

    @allure.title("Поис номера заказа")
    def find_order_number(self, locator):
        with allure.step("Скролл до эелемента"):
            self.scroll_page_to_element(locator)
        with allure.step("Получение значения элемента и его возврат"):
            return self.get_value(locator)

    @allure.title("Проверка открытия заказа")
    @allure.description("Тест проверяет, если кликнуть на заказ, откроется всплывающее окно с деталями")
    def click_on_order_card(self):
        with allure.step("Клик по кнопке «Лента заказов»"):
            self.check_click_feed()
        with allure.step("Клик по заказу"):
            self.click_element(self.FeedLocators.ORDER_CARDS)
        with allure.step("Проверка открытия окна заказа"):
            try:
                if self.visible_element(self.FeedLocators.MODAL_WINDOW):
                    return True
            except NoSuchElementException:
                return False

    @allure.title("Проверка закрытия окна заказа")
    @allure.description("Тест проверяет, если кликнуть на крестик, закроется всплывающее окно с деталями")
    def close_order_card(self):
        with allure.step("Процедура открытия заказа"):
            self.click_on_order_card()
        with allure.step("Клик по на крестик для закрытия окна заказа"):
            self.click_element(self.FeedLocators.MODAL_CLOSE)
        with allure.step("Проверка закрытия окна заказа"):
            try:
                self.visible_element(self.FeedLocators.MODAL_CLOSE)
                return True
            except NoSuchElementException:
                return False

    @allure.title("Проверка отображения заказа на странице «Лента заказов»")
    @allure.description("Тест проверяет, что заказы пользователя из раздела «История заказов» отображаются на "
                        "странице «Лента заказов»")
    def user_order_show_in_feed(self):
        with allure.step("Процедура создания заказа авторизованным юзером"):
            self.login_page.create_order_auth_user()
        with allure.step("Клик на крестик для закрытия окна заказа"):
            self.click_element(self.MainLocators.CLOSE_ORDER_MODAL)
        with allure.step("Клик по кнопке Личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке история заказов"):
            self.click_history.click_history_link()
        with allure.step("Получение номера заказа"):
            order_num_history = self.history_page.check_history_order()
        with allure.step("Клик по кнопке Лента заказов"):
            self.check_click_feed()
        with allure.step("Получение номера заказа"):
            order_num_feed = self.find_order_number(self.FeedLocators.ORDER_NUMBER)
        with allure.step("Проверка номера заказов из разных разделов сайта"):
            return order_num_history == order_num_feed

    @allure.title("Проверка счётчика Выполнено за всё время")
    @allure.description("Тест проверяет, что при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def when_create_new_order_all_time_counter_increases(self):
        with allure.step("Клик по кнопке Лента заказов"):
            self.check_click_feed()
        with allure.step("Получение текущего значения счетчика"):
            old_count = int(self.get_value(self.FeedLocators.ORDER_COUNT_ALL_TIME))
        with allure.step("Процедура создания заказа авторизованным юзером"):
            self.login_page.create_order_auth_user()
        with allure.step("Клик по на крестик для закрытия окна заказа"):
            self.click_element(self.FeedLocators.CLOSE_ORDER_MODAL)
        with allure.step("Клик по кнопке Лента заказов"):
            self.check_click_feed()
        with allure.step("Получение текущего значения счетчика"):
            new_count = int(self.get_value(self.FeedLocators.ORDER_COUNT_ALL_TIME))
        with allure.step("Проверка, что счетчик увеличился после заказа"):
            if new_count == old_count + 1:
                return True

    @allure.title("Проверка счётчика Выполнено за сегодня")
    @allure.description("Тест проверяет, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def when_create_new_order_today_time_counter_increases(self):
        with allure.step("Клик по кнопке Лента заказов"):
            self.check_click_feed()
        with allure.step("Получение текущего значения счетчика"):
            old_count = int(self.get_value(self.FeedLocators.ORDER_COUNT_TODAY_TIME))
        with allure.step("Процедура создания заказа авторизованным юзером"):
            self.login_page.create_order_auth_user()
        with allure.step("Клик по на крестик для закрытия окна заказа"):
            self.click_element(self.FeedLocators.CLOSE_ORDER_MODAL)
        with allure.step("Клик по кнопке Лента заказов"):
            self.check_click_feed()
        with allure.step("Получение текущего значения счетчика"):
            new_count = int(self.get_value(self.FeedLocators.ORDER_COUNT_TODAY_TIME))
        with allure.step("Проверка, что счетчик увеличился после заказа"):
            if new_count == old_count + 1:
                return True

    @allure.title("Проверка отображения заказа в разделе В работе")
    @allure.description("Тест проверяет, что после оформления заказа его номер появляется в разделе В работе")
    def check_order_in_processing(self):
        with allure.step("Процедура создания заказа авторизованным юзером"):
            self.login_page.create_order_auth_user()
        with allure.step("Получение id заказа"):
            id_order = int(self.get_value(self.FeedLocators.ORDER_ID))
        with allure.step("Клик по на крестик для закрытия окна заказа"):
            self.click_element(self.FeedLocators.CLOSE_ORDER_MODAL)
        with allure.step("Клик по кнопке Лента заказов"):
            self.check_click_feed()
        with allure.step("Получение id заказа из раздела В работе"):
            id_order_process = int(self.get_value(self.FeedLocators.ID_ORDER_IN_PROCESS))
        with allure.step("Проверка id из заказа в разделе В работе"):
            if id_order == id_order_process:
                return True


