import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")

        #  with pytest.raises()  проверить, что тест вызывает ожидаемое исключение  (ИСПОЛЬЗУЕТСЯ РЕДКО)
        #  В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException, которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.
        with pytest.raises(NoSuchElementException):                         
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):

              #  Тест пройдет. (no_such_button.btn - такого элемента нет)
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()




'''
pytest 2_webdriver/L3_2_13__unit_test.py




PyTest:

    pip install pytest==7.1.2            установка PyTest
    pip freeze > requirements.txt        фиксируем пакеты в requirements.txt
    pip install -r requirements.txt      установить все пакеты из requirements.txt
    
    pytest file.py    - запуск 


Преимущества:
1) PyTest полностью обратно совместим с фреймворками unittest 
2) Подробный отчёт с поддержкой цветовых схем из коробки.
3) PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest (no boilerplate).
4) Для проверок используется стандартный assert из Python.
5) Возможность создания динамических фикстур (специальных функций, которые настраивают тестовые окружения и готовят тестовые данные).
6) Дополнительные возможности по настройке фикстур.
7) Параметризация тестов — для одного теста можно задать разные параметры (тест запустится несколько раз с разными тестовыми данными).
8) Наличие маркировок (marks), которые позволяют маркировать тесты для их выборочного запуска.
9) Возможность передавать дополнительные параметры через командную строку для настройки тестовых окружений.
10) Большое количество плагинов, которые расширяют возможности PyTest и позволяют решать узкоспециализированные проблемы, что может сэкономить много времени.

Недостатки:
1) PyTest требуется устанавливать дополнительно, так как он не входит в стандартный пакет библиотек Python, в отличие от unittest. 
2) Использование PyTest требует более глубокого понимания языка Python, чтобы разобраться, как применять фикстуры, параметризацию и другие возможности PyTest.







PyTest: правила запуска тестов 

    Когда мы выполняем команду  pytest file.py , тест-раннер собирает все тесты для запуска по определенным правилам:
     - если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории
     - как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например: 
    
            # найти все тесты в директории scripts/selenium_scripts
            pytest scripts/selenium_scripts
            
            # найти и выполнить все тесты в файле 
            pytest test_user_interface.py
            
            # найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить 
            pytest scripts/drafts.py::test_register_new_user_parametrized
            
    
     - дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории
     - во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)
     - внутри всех этих файлов находит тестовые функции по следующему правилу:
            - все тесты, название которых начинается с test, которые находятся вне классов
            - все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)


    Пример:
        def test_abs1():
            assert abs(-42) == 42, "Should be absolute value of a number"
        
        def test_abs2():
            assert abs(-42) == -42, "Should be absolute value of a number"
            
            
        pytest test_abs.py - запуск
'''


