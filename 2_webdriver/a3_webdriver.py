'''


https://habr.com/ru/companies/otus/articles/596071/



            Поиск в консоли браузера:
                $$('css-селектор')
                $x('Xpath-селектор')



            Xpath - xml-путь


            /html/body/div/  -  абсолютный - полный путь по дереву ( / - корень)
            //body//a   - относительный - можем перескакивать, пропускать элементы в дереве
            Можно комбинировать  -  //div/div//a



             Атрибуты  [@ ..]
             //input[@id="OouJcb"]

             Несколько атрибутов (более уточняющий)
             //input[@id="OouJcb" and @class="OouJcb"]//ul/li


             *любой элемент
             //*[@id="OouJcb"]
             //input[@id="OouJcb" and @class="OouJcb"]//ul/*

             //input[1] - 1-ый инпут
             (//input[@class="OouJcb"])[2] - 2-ый инпут, оборачиваем в скобки у сложной конструкции


             . - текущий узел
             .. - узел на уровень выше
             //table/.//tr - ищем tr в рамках таблицы





             Оси:
             ancestor:: -  найди предков
             ancestor-of-self:: - найди себя и предков
             //input[@class="vector-search-box-input"]/ancestor::form  (предки формы у инпута)

             following-sibling::  - соседи
             preceding-sibling::  - соседи выше элемента
             //input[@class="vector-search-box-input"]/following-sibling::* - (все соседи инпута)

             parent::  - найди 1-го родителя
             //input[@class="vector-search-box-input"]/parent::div






             Функции Xpath:
             last() - последний из коллекции
             //*[@id="simpleSearch"]/input[last()]

             text() - по тексту, содержимому
             //a[text()="Apple Records"]

             contains() - содержит ли
             //li[contains(@class,'mw-list-item')]
             //h1[contains(text(),'How people')]

             start-with() - начинается ли
             //input[startt-with(@title,''Go to)]





        -------------------------------------------




            driver:
                ChromeDriver / FirefoxDriver / EdgeDriver




            driver
                .get();
                .title
                .current_url
                .implicitly_wait(5)
                .quit();

                .set_window_size(1920, 300)


            driver.
                .back();
                .forward();
                .refresh();


            driver.find_element
                By.LINK_TEXT
                By.PARTIAL_LINK_TEXT
                By.NAME
                By.CLASS_NAME
                By.ID
                By.CSS_SELECTOR
                By.XPATH




            // Проверка на существование элемента
            if (len(browser.find_elements(By.TAG_NAME, "input")) > 0):
                print("Нашли элемент")




        -------------------------------------------




            WebElement a
                .text
                .click()


            WebElement btn
                .text()
                .click()
                .submit()
                    .is_enabled()
                    .is_displayed()



            WebElement input
                .get_attribute("value")
                .clear()
                .send_keys()
                    .send_keys(Keys.ENTER);
                    .send_keys(Keys.CONTROL,'a')



              WebElement input[@type='file']
                       .send_keys("C:\\test.png")

                        Работа с файлами
                            import os

                            print(os.path.abspath(__file__))                               вернет абсолютный путь -    C:\Users\e.nikolaev\selenium_course\lesson_2_2__step_8__file.py
                            print(os.path.abspath(os.path.dirname(__file__)))              вернет директорию  -        C:\Users\e.nikolaev\selenium_course


                            current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
                            file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
                            element.send_keys(file_path)                                # добавляем файл инпуту




            WebElement checkbox, radio
                    .click()
---                        .isSelected()


            WebElement select

                    # 1 способ, (кликаем select, кликаем опцию)
                            browser.find_element(By.TAG_NAME, "select").click()
                            browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
                            browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

                    # 2 способ, (подключаем библиотеку Select из библиотеки WebDriver)
                            from selenium.webdriver.support.ui import Select
                            select = Select(browser.find_element(By.TAG_NAME, "select"))
                            select.select_by_value("1")
                            select.select_by_visible_text("text")  #  по видимому тексту
                            select.select_by_index(index)          # по его индексу или порядковому номеру



         -------------------------------------------




---            List<WebElement> checkboxes = driver.findElements();
---           checkboxes.get(2).click();
---           checkboxes.size()

---           for(WebElement el: checkboxes){
---               el.click();
---            }






         -------------------------------------------

            Implicit и Explicit Waits
            при асинхронной работе скриптов или задержек от сервера


            1) Implicit wait - неявное ожидание (Не надо явно указывать каждый раз, когда мы выполняем поиск элементов find_element, оно автоматически будет применяться при вызове каждой последующей команды.)
            WebDriver каждые 0.5 секунды проверяет, появился ли элемент

            browser.implicitly_wait(5)  - неявное ожидания выполнения асинхронного запроса



            2) Explicit Waits - явное ожидание. Задаем expected_conditions:
            https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

                    title_is                                    - Ожидание проверки заголовка страницы
                    title_contains
                    presence_of_element_located
                    visibility_of_element_located
                    visibility_of
                    presence_of_all_elements_located
                    text_to_be_present_in_element              - Ожидание проверки наличия данного текста в указанном элементе
                    text_to_be_present_in_element_value
                    frame_to_be_available_and_switch_to_it
                    invisibility_of_element_located
                    element_to_be_clickable                     - пока кнопка не станет кликабельной
                    staleness_of
                    element_to_be_selected
                    element_located_to_be_selected
                    element_selection_state_to_be
                    element_located_selection_state_to_be
                    alert_is_present


            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions


            # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
            button = WebDriverWait(browser, 5).until(
                    expected_conditions.element_to_be_clickable((By.ID, "verify"))
                )

            # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
            button = WebDriverWait(browser, 5).until_not(
                    expected_conditions.element_to_be_clickable((By.ID, "verify"))
    )





         -------------------------------------------



---           Actions actions = new Actions(driver);

---            actions
---                .moveToElement(element)         - навести на элемент
---                .dragAndDrop(element, link)     - перенести один элемент на другой
---                .doubleClick(element)           - двойной клик
---                .contextClick(element)          - клик правой кнопкой мыши
---                .build().perform()              - собрать и выполнить

---               .clickAndHold()                 - кликнуть и не отпускать клавишу
---               .release()                      - отпустить клавишу мыши

---                actions.clickAndHold(element).moveToElement(link).release().build().perform();




         -------------------------------------------



               //js
                    driver
                        .execute_script("document.title='Script executing';alert('Robots at work');")

                        # Варинаты js-скролла страницы до кнопки:
                        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
                        browser.execute_script("button = document.getElementsByTagName('button')[0];button.scrollIntoView(true);")



               //alert
                    alert = browser.switch_to.alert
                    alert.accept()                      - нажать на кнопку ОК
                    alert_text = alert.text             - получить alert-текст


                    confirm = browser.switch_to.alert
                    confirm.accept()                    - нажать на кнопку ОК
                    confirm.dismiss()                   - нажать на кнопку Отмена


                    prompt = browser.switch_to.alert
                    prompt.send_keys("My answer")       - Заполнить поле prompt
                    prompt.accept()                     - нажать на кнопку ОК




            //вкладки, окна
                    При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
                    Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти:

                        1) browser.switch_to.window(window_name)

                          new_window = browser.window_handles[1]          - имя второй вкладки
                          first_window = browser.window_handles[0]        - имя текущей вкладки



                        2) handler = driver.current_window_handle  - имя текущей вкладки

                          for handle in driver.window_handles:
                              driver.switch_to.window(handle)   - переключись на последнюю вкладку



         -------------------------------------------



---            Date dateNow = new Date();
---            SimpleDateFormat format = new SimpleDateFormat("hh-mm-ss");
---            String fileName = format.format(dateNow) + ".jpg";

---            // скриншоты
---            File screen = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
---            FileUtils.copyFile(screen, new File("C:\\Users\\e.nikolaev\\Downloads\\" + fileName));   - pom.xml ставим пакет






         -------------------------------------------

            Assert:

                assert - проверяет истинность утверждений.
                    assert True  - не приводит к выводу дополнительных сообщений
                    assert False - вызовет исключение AssertionError

                assert abs(-42) == 42
                assert abs(-42) == -42                                                      исключение AssertionError
                assert abs(-42) == -42, "Should be absolute value of a number"              исключеение с текстом - AssertionError: Should be absolute value of a number




         -------------------------------------------


            Юнит-тесты:

                                    import unittest


                                    class TestAbs(unittest.TestCase):
                                        def test_abs1(self):
                                            self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

                                        def test_abs2(self):
                                            self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


                                    if __name__ == "__main__":
                                        unittest.main()


            Для этого нам понадобится выполнить следующие шаги:
                1. Импортировать unittest в файл: import unittest
                2. Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
                3. Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
                4. Изменить assert на self.assertEqual(), assertNotEqual, assertTrue, assertFalse
                5. Заменить строку запуска программы на unittest.main()




         -------------------------------------------



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










'''