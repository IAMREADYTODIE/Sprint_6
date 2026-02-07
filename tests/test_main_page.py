import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from data import Urls, TestData

class TestMainPage:

    @allure.title("Проверка раздела 'Вопросы о важном'")
    @allure.description("Проверяем соответствие текста ответов выбранным вопросам")
    @pytest.mark.parametrize("index, expected_answer", TestData.FAQ_ANSWERS)
    def test_faq_questions(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(index)
        answer_text = main_page.get_answer_text(index)
        assert answer_text == expected_answer

    @allure.title("Проверка логотипа 'Самокат'")
    @allure.description("Проверка возврата на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        assert driver.current_url == Urls.BASE_URL

    @allure.title("Проверка логотипа 'Яндекс'")
    @allure.description("Проверка перехода на страницу Дзена в новой вкладке при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()

        # Ожидаем открытие второй вкладки
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        
        # Переключаемся на новую вкладку
        all_handles = driver.window_handles
        driver.switch_to.window(all_handles[1])

        # Ждем, пока в URL появится домен дзена
        assert main_page.wait_for_url_contains("dzen.ru")