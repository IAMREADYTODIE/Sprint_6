import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента: {locator}")
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста в элемент {locator}")
    def set_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Прокрутка до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание появления текста в URL")
    def wait_for_url_contains(self, url_part):
        return WebDriverWait(self.driver, 15).until(EC.url_contains(url_part))

    @allure.step("Ждем открытия новой вкладки и переключаемся")
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
