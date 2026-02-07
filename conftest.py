import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from data import Urls

@pytest.fixture
def driver():
    # Отключаем лишние логи драйвера
    os.environ['WDM_LOG_LEVEL'] = '0'
    
    # Настройки для стабильности в Firefox
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    try:
        # Установка через менеджер
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(executable_path=driver_path)
        driver = webdriver.Firefox(service=service, options=options)
    except Exception:
        # Если бан по IP от GitHub — берем драйвер из системы
        driver = webdriver.Firefox(options=options)

    # Заходим на главную
    driver.get(Urls.BASE_URL)
    
    yield driver
    
    # Закрываем браузер после теста
    driver.quit()
    