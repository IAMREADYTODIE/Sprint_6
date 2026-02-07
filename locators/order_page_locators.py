from selenium.webdriver.common.by import By

class OrderPageLocators:
    # --- Этап 1: "Для кого самокат" ---
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # Локатор для выбора конкретной станции из списка (подставляем название станции)
    METRO_OPTION_TEMPLATE = (By.XPATH, ".//div[@class='select-search__select']//div[text()='{}']")
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # --- Этап 2: "Про аренду" ---
    DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    # Локатор для выбора срока (подставляем текст: "сутки", "двое суток" и т.д.)
    RENTAL_OPTION_TEMPLATE = (By.XPATH, ".//div[@class='Dropdown-option' and text()='{}']")
    
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FINAL = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # --- Окна подтверждения ---
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")