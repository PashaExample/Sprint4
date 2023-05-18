import pytest
from selenium import webdriver

# запуск браузера
@pytest.fixture()
def driver():

    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver

    driver.quit()