import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    
    @allure.step("Принимаем куки")
    def accept_cookies(self):
        """Метод закрывает плашку с куками, если она появилась."""
        try:
            # Ждем кнопку куки чуть меньше (5 сек), чтобы не тратить время всего теста
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            # Если кнопка не появилась — просто игнорируем и идем дальше
            pass

    @allure.step("Кликаем на вопрос номер {num}")
    def click_question(self, num):
        """Метод находит вопрос по индексу и кликает на него."""
        method, locator = MainPageLocators.QUESTION_LOCATOR_TEMPLATE
        formatted_locator = (method, locator.format(num))
        self.scroll_to_element(formatted_locator)
        self.click_element(formatted_locator)

    @allure.step("Получаем текст ответа номер {num}")
    def get_answer_text(self, num):
        """Метод возвращает текст открывшегося ответа по индексу."""
        method, locator = MainPageLocators.ANSWER_LOCATOR_TEMPLATE
        formatted_locator = (method, locator.format(num))
        return self.get_text_from_element(formatted_locator)

    @allure.step("Кликаем на кнопку 'Заказать' в шапке")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликаем на кнопку 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликаем на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)