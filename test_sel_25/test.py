import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_pets():
    # Ввод email
    pytest.driver.find_element_by_id('email').send_keys('Xandr3302@mail.ru')
    # Ввод пароля
    pytest.driver.find_element_by_id('pass').send_keys('@Mail123@321')

    # Неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Нажатие кнопки входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверка того, что находимся на нужно странице
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    # Поиск на странице всей информации о питомце (фото, имя, вид, возраст):
    images = pytest.driver.find_elements_by_xpath('//img[@class="card-img-top"]')
    names = pytest.driver.find_elements_by_xpath('//h5[@class="card-title"]')
    descriptions = pytest.driver.find_elements_by_xpath('//p[@class="card-text"]')

    # Проверка того, что данный по питомцам не содержат пустых строк
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_show_my_pets():
    # авторизация и открытие главной страницы сайта
    pytest.driver.find_element_by_id('email').send_keys('Xandr3302@mail.ru')
    pytest.driver.find_element_by_id('pass').send_keys('@Mail123@321')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Явного ожидания:
    wait = WebDriverWait(pytest.driver, 10)

    assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "PetFriends"))

    # Открываем страницу /my_pets.
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()

    # Ожидаем в течение 10с, что на странице есть тег h2 с текстом "All" -именем пользователя
    assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), "All"))

    # Ищем в теле таблицы все строки с полными данными питомцев (имя, порода, возраст, "х" удаления питомца):
    css_locator = 'tbody>tr'
    data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)

    # Ожидание, что данные всех питомцев, найденных локатором css_locator = 'tbody>tr', видны на странице:
    for i in range(len(data_my_pets)):
        assert wait.until(EC.visibility_of(data_my_pets[i]))

    # Поиск в теле таблицы всех фото питомцев. Ожидание, что все загруженные фото видны на странице:
    image_my_pets = pytest.driver.find_elements_by_css_selector('img[style="max-width: 100px; max-height: 100px;"]')
    for i in range(len(image_my_pets)):
        if image_my_pets[i].get_attribute('src') != '':
            assert wait.until(EC.visibility_of(image_my_pets[i]))

    # Поиск имен и ожидание:
    name_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
    for i in range(len(name_my_pets)):
        assert wait.until(EC.visibility_of(name_my_pets[i]))

    # Поиск породы и ожидание:
    type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
    for i in range(len(type_my_pets)):
        assert wait.until(EC.visibility_of(type_my_pets[i]))

    # Возраст:
    age_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')
    for i in range(len(age_my_pets)):
        assert wait.until(EC.visibility_of(age_my_pets[i]))

    # Количество питомцев пользователя:
    all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
    statistics_pets = all_statistics[1].split(" ")
    all_my_pets = int(statistics_pets[-1])

    assert len(data_my_pets) == all_my_pets

    # Проверяем, что хотя бы у половины питомцев есть фото:
    m = 0
    for i in range(len(image_my_pets)):
        if image_my_pets[i].get_attribute('src') != '':
            m += 1
    assert m >= all_my_pets / 2

    # Имя питомца:
    for i in range(len(name_my_pets)):
        assert name_my_pets[i].text != ''

    # Порода или вид питомца:
    for i in range(len(type_my_pets)):
        assert type_my_pets[i].text != ''

    # Наличие возраста:
    for i in range(len(age_my_pets)):
        assert age_my_pets[i].text != ''

    # Разные имена питомцев:
    list_name_my_pets = []
    for i in range(len(name_my_pets)):
        list_name_my_pets.append(name_my_pets[i].text)
    set_name_my_pets = set(list_name_my_pets)  # преобразовываем список в множество
    assert len(list_name_my_pets) == len(
        set_name_my_pets)  # сравниваем длину списка и множества: без повторов должны совпасть