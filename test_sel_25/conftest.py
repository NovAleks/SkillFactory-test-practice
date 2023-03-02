from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome()
   chrome_options = Options()
   driver = webdriver.Chrome(executable_path="C:/WebDriver/chromedriver.exe/", options=chrome_options)

   pytest.driver.set_window_size(1000, 1000)
   # Переход на страницу авторизации пользователя
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield


   pytest.driver.quit()