from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_url_to_be(self, url):
        return WebDriverWait(self.driver, 15).until(
            EC.url_to_be(url)
        )

    def wait_for_url_contains(self, url_part):
        """Ожидание появления части текста в URL (для динамических ссылок)."""
        return WebDriverWait(self.driver, 15).until(
            EC.url_contains(url_part)
        )