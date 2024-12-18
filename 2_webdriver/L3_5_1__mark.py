import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\n.......01")
    browser = webdriver.Chrome()
    yield browser
    print("\n.......02")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        print("\n.......03")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")


    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\n.......04")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")



    @pytest.mark.smoke
    @pytest.mark.win10
    def test_for_win10(self, browser):
        print("\n.......05")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")



    @pytest.mark.smoke
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print("\n.......06")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")


'''

    Маркировка тестов - для разделения тестов ( например smoke и regression)
    
    @pytest.mark.mark_name  - декоратор для маркировки (mark_name - любая строка)
    @pytest.mark.skip       - Пропуск тестов (стандартная метка)
    @pytest.mark.xfail      - помечать тест как ожидаемо падающий (стандартная метка)
    
    @pytest.mark.xfail(reason="fixing this bug right now") -  reason - добавляем сообщение в консоли
                                                              запускаем с параметром -rx :       pytest -rx -v test_fixture10a.py
    @pytest.mark.xfail(strict=True)  - вместо статуса xpass - будет статус упавший failed
    
    
    
    
    Также метки нужно регистрировать в pytest.ini с содержимым:
                        [pytest]
                        markers =
                            smoke: marker for smoke tests
                            regression: marker for regression tests
    
    
    
    pytest -s -v -m smoke .\2_webdriver\L3_5_1__mark.py                   -   запуск тестов с нужной маркировкой                          ( -m smoke )
    pytest -s -v -m "not smoke" .\2_webdriver\L3_5_1__mark.py             -   запуск тестов не имеющие заданную маркировку (инверсия)     (-m "not smoke")
    pytest -s -v -m "smoke or regression" .\2_webdriver\L3_5_1__mark.py   -   Запустим smoke и regression-тесты                           (-m "smoke or regression")
    pytest -s -v -m "smoke and win10" .\2_webdriver\L3_5_1__mark.py       -   Выбор тестов, имеющих несколько маркировок                  (-m "smoke and win10")
                 
                    
                    
'''


