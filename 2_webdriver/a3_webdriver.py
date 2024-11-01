'''


https://habr.com/ru/companies/otus/articles/596071/


        Поиск в консоли браузера:
                $$('css-селектор')
                $x('Xpath-селектор')

            //
            /
            [@atribute ..]
            (//input[@class="OouJcb"])[2]
             .
             ..

             ancestor::
             ancestor-of-self::
             following-sibling::
             preceding-sibling::
             parent::


             Функции Xpath:
                last() - последний из коллекции
                text() - по тексту, содержимому
                contains() - содержит ли
                start-with() - начинается ли
                    h1[contains(text(),'How people')]




        -------------------------------------------




            driver:
                ChromeDriver / FirefoxDriver / EdgeDriver




            driver.get();
            driver.title
            driver.current_url
---              driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
            driver.quit();


---            driver.manage().window()
---                .maximize();
---               .setSize(new Dimension(640, 320));


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




---            WebElement a
---                 .getText()
---                  .click()


---         WebElement btn
---                .getText()
---                 .click()
---                  .submit()
---                      .isEnabled()
---                     .isDisplayed()


---          WebElement input
                   .get_attribute("value")
---                  .clear()
                 .send_keys()
---                  input.send_keys(Keys.chord(Keys.SHIFT, "test Keys"));
---                          Keys.ENTER
---                           Keys.chord(Keys.CONTROL, "a")


              WebElement input[@type='file']
                       .send_keys("C:\\test.png")

                        Работа с файлами
                            import os

                            print(os.path.abspath(__file__))                               вернет абсолютный путь -    C:\Users\e.nikolaev\selenium_course\lesson_2_2__step_8__file.py
                            print(os.path.abspath(os.path.dirname(__file__)))              вернет директорию  -        C:\Users\e.nikolaev\selenium_course


                            current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
                            file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
                            element.send_keys(file_path)                                # добавляем файл инпуту




---            WebElement checkbox, radio
---                   .click()
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



---            .assertTrue(1 + 1 == 2) - проверка на true
---            .assertFalse(1 + 1 == 10)- проверка на false

---            .assertNull() - проверка на Null
---            .assertNotNull() - проверка на Null

---            .assertEquals(10, 5 + 5) - проверка на сравнение
---            .assertNotEquals(10, 5 + 5) - проверка на сравнение


---            .assertTrue("Метод провалился",1 + 1 == 12) - Можно 1-м параметром передавать сообщение при провале теста
---            Тесты могут выполняться в любом порядке, они должны быть независимые.



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







unittest, PyTest


---             JUnit:
---                @BeforeClass - в самом начале один раз перед всеми методами
---                @AfterClass - в самом конце один раз после всех методов
---               @Before - перед каждым тестовым методом
---                @After - после каждоого тестового метода
---                @Ignore - не выполнять тестовый метод










'''