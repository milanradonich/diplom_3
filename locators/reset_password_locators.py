from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    NEW_PASSWORD_INPUT = By.XPATH, "//input[@type='password' and @name='Введите новый пароль']"
    PASSWORD_FOCUSED = By.XPATH, "//label[contains(@class, 'input__placeholder-focused')]"
    ICON_SVG = By.XPATH, "//svg[@xmlns='http://www.w3.org/2000/svg' and @width='24' and @height='24' and @fill='#F2F2F3']"

