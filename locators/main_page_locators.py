from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка куки "да все привыкли"
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Шаблоны для вопросов и ответов (вместо {} будем подставлять номер 0-7)
    QUESTION_LOCATOR_TEMPLATE = (By.ID, "accordion__heading-{}")
    ANSWER_LOCATOR_TEMPLATE = (By.ID, "accordion__panel-{}")

    # Кнопки "Заказать" (верхняя и нижняя)
    ORDER_BUTTON_TOP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")