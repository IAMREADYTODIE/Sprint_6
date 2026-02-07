import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData

class TestOrderPage:

    @allure.title("Заказ самоката через кнопку в шапке")
    def test_order_flow_from_header(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_top()
        
        order_page = OrderPage(driver)
        # ВЕСЬ ЗАКАЗ В ОДНУ СТРОЧКУ :
        order_page.make_order(TestData.USER_1)
        
        assert order_page.is_order_success_visible()

    @allure.title("Заказ самоката через кнопку внизу страницы")
    def test_order_flow_from_bottom(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_bottom()
        
        order_page = OrderPage(driver)
        # ВЕСЬ ЗАКАЗ В ОДНУ СТРОЧКУ:
        order_page.make_order(TestData.USER_2)
        
        assert order_page.is_order_success_visible()
