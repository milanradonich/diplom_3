from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    NEW_PASSWORD_INPUT = By.XPATH, "//input[@type='password' and @name='Введите новый пароль']"
    NEW_PASSWORD_INPUT_TEXT = By.XPATH, "//input[@type='text' and @name='Введите новый пароль']"
    PASSWORD_FOCUSED = By.XPATH, "//label[contains(@class, 'input__placeholder-focused')]"
    ICON_SVG = By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg'][width='24'][height='24'][fill='#F2F2F3']"
    ACTIVE_INPUT_DIV = By.CSS_SELECTOR, "div.input.input_type_password.input_status_active"

