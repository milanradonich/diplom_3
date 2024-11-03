from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class ForgotPasswordPage(LoginPage):
    class ForgotPasswordLocators:
        FORGOT_PASS_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'
        RECOVERY_BUTTON = By.XPATH, "//button[text()='Восстановить']"  # кнопка восстановить
        EMAIL_INPUT = By.XPATH, "//input[@type='text' and @name='name']"  # форма email

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email):
        self.input_symbols(self.ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_recovery(self):
        self.click_element(self.ForgotPasswordLocators.RECOVERY_BUTTON)

    def enter_email_and_click_recovery(self):
        self.input_email('milan_radonich13@yandex.ru')
        self.click_recovery()

    def transition_to_forgot_password_page(self):
        self.click_account()
        self.click_recovery_pass()
        self.navigate(self.ForgotPasswordLocators.FORGOT_PASS_PAGE)
        current_url = self.driver.current_url
        return current_url == self.ForgotPasswordLocators.FORGOT_PASS_PAGE


