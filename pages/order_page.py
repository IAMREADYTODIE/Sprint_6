import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполняем данные пользователя")
    def fill_user_data(self, user_data):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, user_data["name"])
        self.set_text_to_element(OrderPageLocators.SURNAME_FIELD, user_data["surname"])
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, user_data["address"])
        
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.set_text_to_element(OrderPageLocators.METRO_FIELD, user_data["metro"])
        method, locator = OrderPageLocators.METRO_OPTION_TEMPLATE
        self.click_element((method, locator.format(user_data["metro"])))
        
        self.set_text_to_element(OrderPageLocators.PHONE_FIELD, user_data["phone"])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем детали аренды")
    def fill_rent_details(self, user_data):
        self.set_text_to_element(OrderPageLocators.DATE_FIELD, user_data["date"])
        self.find_element_with_wait(OrderPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
        
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        method, locator = OrderPageLocators.RENTAL_OPTION_TEMPLATE
        self.click_element((method, locator.format(user_data["period"])))
        
        color_loc = OrderPageLocators.COLOR_BLACK if user_data["color"] == "black" else OrderPageLocators.COLOR_GREY
        self.click_element(color_loc)
            
        self.set_text_to_element(OrderPageLocators.COMMENT_FIELD, user_data["comment"])
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверяем всплывающее окно об успехе")
    def check_order_success(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS_MODAL).is_displayed()

    @allure.step("Полный процесс оформления заказа")
    def make_order(self, user_data):
        """Метод объединяет все шаги заполнения заказа"""
        self.fill_user_data(user_data)
        self.fill_rent_details(user_data)
        self.confirm_order()