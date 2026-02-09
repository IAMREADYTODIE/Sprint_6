import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнение формы 'Для кого самокат'")
    def fill_client_form(self, user_data):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, user_data["name"])
        self.set_text_to_element(OrderPageLocators.SURNAME_FIELD, user_data["surname"])
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, user_data["address"])
        
        # Выбор метро
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.set_text_to_element(OrderPageLocators.METRO_FIELD, user_data["metro"])
        # Сборка локатора из строки-шаблона
        station_xpath = OrderPageLocators.METRO_OPTION_TEMPLATE.format(user_data["metro"])
        self.click_element((By.XPATH, station_xpath))
        
        self.set_text_to_element(OrderPageLocators.PHONE_FIELD, user_data["phone"])
        self.click_element(OrderPageLocators.ORDER_NEXT_BUTTON)

    @allure.step("Заполнение формы 'Про аренду'")
    def fill_rent_form(self, user_data):
        # Выбор даты
        self.set_text_to_element(OrderPageLocators.ORDER_DATE, user_data["date"])
        self.find_element_with_wait(OrderPageLocators.ORDER_DATE).send_keys(Keys.ENTER)
        
        # Выбор срока
        self.click_element(OrderPageLocators.ORDER_RENTAL_PERIOD)
        period_xpath = OrderPageLocators.ORDER_RENTAL_OPTION_TEMPLATE.format(user_data["period"])
        self.click_element((By.XPATH, period_xpath))
        
        # Выбор цвета
        color_loc = OrderPageLocators.ORDER_COLOR_BLACK if user_data["color"] == "black" else OrderPageLocators.ORDER_COLOR_GREY
        self.click_element(color_loc)
            
        self.set_text_to_element(OrderPageLocators.ORDER_COMMENT, user_data["comment"])
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)

    @allure.step("Полный цикл оформления заказа")
    def make_order(self, user_data):
        """Метод объединяет заполнение обеих форм и клик 'Заказать'."""
        self.fill_client_form(user_data)
        self.fill_rent_form(user_data)
        self.click_element(OrderPageLocators.ORDER_CONFIRM_YES)

    @allure.step("Проверка видимости окна успешного заказа")
    def is_order_success_visible(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS_MODAL).is_displayed()
    