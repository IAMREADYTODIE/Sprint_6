import pytest
import allure
from pages.main_page import MainPage
from data import Urls, TestData

class TestMainPage:

    @allure.title("Проверка FAQ")
    @allure.description("Проверяем соответствие текста ответов выбранным вопросам")
    @pytest.mark.parametrize("index, expected_answer", TestData.FAQ_ANSWERS)
    def test_faq_questions(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(index)
        # Проверка текста ответа
        assert main_page.get_answer_text(index) == expected_answer

    @allure.title("Проверка логотипа 'Самокат'")
    @allure.description("Проверка возврата на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        # 1. Уходим на страницу заказа
        main_page.click_order_button_top()
        # 2. Жмем на лого Самоката
        main_page.click_scooter_logo()
        # 3. Проверяем URL через метод Page Object
        assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Проверка логотипа 'Яндекс'")
    @allure.description("Проверка перехода на страницу Дзена в новой вкладке при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        
        # Переключение на новую вкладку через метод страницы
        main_page.switch_to_new_tab()
        # Ожидание и проверка URL
        assert main_page.wait_for_url_contains("dzen.ru")
