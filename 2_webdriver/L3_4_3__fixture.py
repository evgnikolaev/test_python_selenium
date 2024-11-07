import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    # “setup” - вначале теста
    print("\n......01")
    driver = webdriver.Chrome()
    yield driver

    # “teardown” - вконце теста
    print("\n......05")
    driver.quit()





# autouse=True  -   фикстура запустится для каждого теста даже без явного вызова
@pytest.fixture(autouse=True)
def prepare_data():
    print("\n......02")




class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        print("\n......03")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\n......04")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


'''

    Фикстуры, возвращающие значение
    
    1) Создадим фикстуру browser,
    2) @pytest.fixture - укажем, что он является фикстурой с помощью декоратора @pytest.fixture
    3) Всё, что идёт до оператора yield является “setup”, а всё, что после — “teardown” (yield, к слову, может ничего и не возвращать, а просто будет разделителем, отделяющим “setup” от “teardown”).
    4) Для фикстур можно задавать область покрытия фикстур scope="class" . Допустимые значения: 
    
            session   - один раз для всех тестов, запущенных в данной сессии
            module    - один раз для модуля
            
            class     - выполняется один раз перед запуском всех тестовых методов в классе
            function  - выполняется перед запуском каждого тестового метода в классе
            
            
    5) Для фикстур можно задавать автоиспользование фикстур
            autouse=True  - фикстура запустится для каждого теста даже без явного вызова
            Без явной необходимости автоиспользованием фикстур лучше не пользоваться. 
            
            
    6) После этого мы можем вызывать фикстуру в тестах, передав ее как параметр.




                ЧТобы лучше понять фикстуры:
                    Декораторы в питон - это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.
                                def decorator_function(func):
                                    def wrapper():
                                        print('Функция-обёртка!')
                                        print('Оборачиваемая функция: {}'.format(func))
                                        print('Выполняем обёрнутую функцию...')
                                        func()
                                        print('Выходим из обёртки')
                                    return wrapper
                                
                                @decorator_function
                                def hello_world():
                                    print('Hello world!')
                                
                                hello_world()
                    
                    
'''


