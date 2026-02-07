import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from data import Urls

@pytest.fixture
def driver():
    # Отключаем лишние логи в терминале
    os.environ['WDM_LOG_LEVEL'] = '0'
    
    try:
        # Пытаемся установить/обновить драйвер
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(executable_path=driver_path)
        driver = webdriver.Firefox(service=service)
    except Exception:
        # Если GitHub заблокировал IP — пытаемся запустить просто Firefox 
        # (сработает, если драйвер уже есть в системе или кэше)
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(Urls.BASE_URL)
    
    yield driver
    
    driver.quit()