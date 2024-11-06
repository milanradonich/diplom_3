import allure
from selenium.webdriver.common.by import By
from pages.forgot_password_page import ForgotPasswordPage


class ResetPasswordPage(ForgotPasswordPage):
    class ResetPasswordLocators:
        RESET_PASS_PAGE = 'https://stellarburgers.nomoreparties.site/reset-password'
        NEW_PASSWORD_INPUT = By.XPATH, "//input[@type='password' and @name='Введите новый пароль']"
        NEW_PASSWORD_INPUT_TEXT = By.XPATH, "//input[@type='text' and @name='Введите новый пароль']"
        PASSWORD_FOCUSED = By.XPATH, "//label[contains(@class, 'input__placeholder-focused')]"
        ICON_SVG = By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg'][width='24'][height='24'][fill='#F2F2F3']"
        ACTIVE_INPUT_DIV = By.CSS_SELECTOR, "div.input.input_type_password.input_status_active"

    def __init__(self, driver):
        super().__init__(driver)

    def input_new_password(self):
        self.input_symbols(self.ResetPasswordLocators.NEW_PASSWORD_INPUT, '1234')

    def click_to_svg(self):
        self.click_element(self.ResetPasswordLocators.ICON_SVG)

    def input_active(self):
        return self.present_in_element(self.ResetPasswordLocators.NEW_PASSWORD_INPUT_TEXT)

    @allure.title("Проверка ввода почты и клик по кнопке «Восстановить»")
    @allure.description("Тест проверяет, что после ввода почты и клику по кнопке «Восстановить» перейдем на страницу "
                        "сброса пароля")
    def check_click_recovery_btn(self):
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке восстановить пароль"):
            self.click_recovery_pass()
        with allure.step("Ввод почты и пароля с нажатием на восстановить"):
            self.enter_email_and_click_recovery()
        with allure.step("Ожидание страницы после восстановления пароля"):
            self.wait_visible_url(self.ResetPasswordLocators.RESET_PASS_PAGE)
        with allure.step("Проверка актуальной страницы и ожидаемой"):
            assert self.driver.current_url == self.ResetPasswordLocators.RESET_PASS_PAGE

    @allure.title("Проверка клика по кнопке показать/скрыть пароль")
    @allure.description(
        "Тест проверяет, что клик на показать/скрыть пароль делает поле активным")
    def click_icon_show_password(self):
        with allure.step("Клик по кнопке личный кабинет"):
            self.click_account()
        with allure.step("Клик по кнопке восстановить пароль"):
            self.click_recovery_pass()
        with allure.step("Ввод почты и пароля с нажатием на восстановить"):
            self.enter_email_and_click_recovery()
        with allure.step("Ввод нового пароля"):
            self.input_new_password()
        with allure.step("Клик по иконке показать/скрыть пароль"):
            self.click_to_svg()
        return self.input_active()
