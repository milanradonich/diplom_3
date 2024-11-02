from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    RECOVERY_BUTTON = By.XPATH, "//button[text()='Восстановить']"  #кнопка восстановить
    EMAIL_LABEL = By.XPATH, "//input[@type='text' and @name='name']" # форма email

