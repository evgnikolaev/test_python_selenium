'''



                PyTest:

                    pip install pytest==7.1.2            установка PyTest
                    pip freeze > requirements.txt        фиксируем пакеты в requirements.txt
                    pip install -r requirements.txt      установить все пакеты из requirements.txt


                    pytest file.py    - запуск
                    pytest -v (verbose, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения:

                    pytest  -s  2_webdriver/L3_4_2__fixture.py        // -s, чтобы увидеть текст, который выводится командой print().

                    pytest -s -v -m smoke 2_webdriver/L3_5_1__mark.py                   -   запуск тестов с нужной маркировкой                          ( -m smoke )
                    pytest -s -v -m "not smoke" 2_webdriver/L3_5_1__mark.py             -   запуск тестов не имеющие заданную маркировку (инверсия)     (-m "not smoke")
                    pytest -s -v -m "smoke or regression" 2_webdriver/L3_5_1__mark.py   -   Запустим smoke и regression-тесты                           (-m "smoke or regression")
                    pytest -s -v -m "smoke and win10" 2_webdriver/L3_5_1__mark.py       -   Выбор тестов, имеющих несколько маркировок                  (-m "smoke and win10")

                    pytest -s -v --browser_name=firefox test_cmd.py                     -   запуск в браузере firefox
                    pytest -s -v --browser_name=chrome test_parser.py                   -   запуск в браузере chrome



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



         -------------------------------------------


                        1) Юнит-тест

                                    import unittest


                                    class TestAbs(unittest.TestCase):
                                        def test_abs1(self):
                                            self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

                                        def test_abs2(self):
                                            self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


                                    if __name__ == "__main__":
                                        unittest.main()



                        2) Pytest

                                    def test_abs1():
                                        assert abs(-42) == 42, "Should be absolute value of a number"

                                    def test_abs2():
                                        assert abs(-42) == -42, "Should be absolute value of a number"





         -------------------------------------------


            Фикстуры            -  L3_4_2__fixture.py - файл

            Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.
            Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами

            pytest  -s  2_webdriver/L3_4_2__fixture.py        // -s, чтобы увидеть текст, который выводится командой print().


             - префиксы setup_*, teardown_* отвечают за порядок исполнения фикстур: до чего-то, после чего-то.
             - постфиксы *_class, *_method и другие отвечают за уровень применения фикстур: ко всему классу, к каждому методу в классе и тд.

                Исходя их логики выше:

                    setup_class - выполняется один раз перед запуском всех тестовых методов в классе
                    teardown_class  - выполянется один раз после
                    setup_method  - выполняется перед запуском каждого тестового метода в классе
                    teardown_method - выполняется каждый раз после

                Про декоратор:
                @classmethod декоратор, использованный для удобства чтения кода. Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу.





         -------------------------------------------




                Фикстуры, возвращающие значение       - L3_4_3__fixture.py - файл


                        @pytest.fixture(scope="function")
                        def browser():
                            # “setup” - вначале теста
                            print("\n......01")
                            driver = webdriver.Chrome()
                            yield driver

                            # “teardown” - вконце теста
                            print("\n......05")
                            driver.quit()



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




         -------------------------------------------




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





        -------------------------------------------




                Параметризация тестов

                @pytest.mark.parametrize('language', ["ru", "en-gb"])       - запустить один и тот же тест с разными входными параметрами




         -------------------------------------------




                Conftest.py — конфигурация тестов (одна фикстура на несколько файлов, чтобы в каждом файле не описывать)    - файл    L3_6_1__conftest.py

                    ОЧЕНЬ ВАЖНО!

                                tests/
                                ├── conftest.py
                                ├── subfolder
                                │   └── conftest.py
                                │   └── test_abs.py

                        Следует избегать вложенности conftest.py , если запускаем из папки test например!

                        В таком случае применяются ОБА файла conftest.py, что может вести к непредсказуемым ошибкам и конфликтам.
                        Таким образом можно переопределять разные фикстуры, но мы в рамках курса рекомендуем придерживаться одного файла на проект/задачу и держать их горизонтально, как-нибудь так:

                                selenium_course_solutions/
                                ├── section3
                                │   └── conftest.py
                                │   └── test_languages.py
                                ├── section4
                                │   └── conftest.py
                                │   └── test_main_page.py

                                правильно!




         -------------------------------------------





                Conftest.py и передача параметров в командной строке

                    В файле  conftest.py добавляем:


                                        import pytest
                                        from selenium import webdriver

                                        def pytest_addoption(parser):
                                            parser.addoption('--browser_name', action='store', default="chrome",
                                                             help="Choose browser: chrome or firefox")


                                        @pytest.fixture(scope="function")
                                        def browser_conftest(request):
                                            browser_name = request.config.getoption("browser_name")
                                            browser = None
                                            if browser_name == "chrome":
                                                print("\nstart chrome browser for test..")
                                                browser = webdriver.Chrome()
                                            elif browser_name == "firefox":
                                                print("\nstart firefox browser for test..")
                                                browser = webdriver.Firefox()
                                            else:
                                                raise pytest.UsageError("--browser_name should be chrome or firefox")
                                            yield browser
                                            print("\nquit browser..")
                                            browser.quit()




                    Это делается с помощью встроенной функции pytest_addoption и фикстуры request:
                    browser_name = request.config.getoption("browser_name")



                    pytest -s -v  .\2_webdriver\L3_6_5__conftest_request.py
                    Если запустить без параметра, будет ошибка.
                    Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:

                                        parser.addoption('--browser_name', action='store', default="chrome",
                                                         help="Choose browser: chrome or firefox")

                                        pytest_addoption - функция должна быть прописана в conftest.py, иначе обибки

                    pytest -s -v --browser_name=chrome .\2_webdriver\L3_6_5__conftest_request.py

















'''