from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Поля первой формы
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_OPTION_TEMPLATE = ".//div[@class='select-search__select']//div[text()='{}']"
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    ORDER_NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # Поля второй формы
    ORDER_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    ORDER_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    ORDER_RENTAL_OPTION_TEMPLATE = ".//div[@class='Dropdown-option' and text()='{}']"
    ORDER_COLOR_BLACK = (By.ID, "black")
    ORDER_COLOR_GREY = (By.ID, "grey")
    ORDER_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    
    # Кнопки финала
    ORDER_BUTTON_FINAL = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    ORDER_CONFIRM_YES = (By.XPATH, ".//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")
    