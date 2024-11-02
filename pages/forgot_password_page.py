from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class ForgotPasswordPage(LoginPage):
    class ForgotPasswordLocators:
        FORGOT_PASS_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'
        RECOVERY_BUTTON = By.XPATH, "//button[text()='Восстановить']"  # кнопка восстановить
        EMAIL_LABEL = By.XPATH, "//input[@type='text' and @name='name']"  # форма email

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email):
        self.input_symbols(self.ForgotPasswordLocators.EMAIL_LABEL, email)

    def click_recovery(self):
        self.click_element(self.ForgotPasswordLocators.RECOVERY_BUTTON)

    def enter_email_and_click_recovery(self):
        self.input_email('milan_radonich13@yandex.ru')
        self.click_recovery()


