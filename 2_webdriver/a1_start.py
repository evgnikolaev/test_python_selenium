'''


https://stepik.org/lesson/25969/step/2?unit=196192


    python --version                    версия питон
    mkdir environments	                Создаем папку в которой будем работать
    python -m venv selenium_env	        создание окружения в созданной папке (делается одноразово)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    cd environments			                Созданная папка, в ней работаем
    selenium_env\Scripts\activate.bat       Запуск окружения
    deactivate			                    выйти из окружения
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    python                          Запуск питона в запущенном окружении
    print("Hello, Selenium!")       Команда питона
    exit()                          Выйти из питона в запущенном окружении




Для работы в pycharm  ставим :
1) selenium в pycharm
2) chromedriver - в поиске в гугле, и скачиваем драйвер под свою версию браузера:
https://developer.chrome.com/docs/chromedriver/downloads?hl=ru




https://stepik.org/lesson/25969/step/6?unit=196192

    pip install selenium==4.*            установка библиотеки селениума в окружение
    pip list                             установленные библиотеки
    pip install pytest==7.1.2            установка PyTest
    pip freeze > requirements.txt        фиксируем пакеты в requirements.txt
    pip install -r requirements.txt      установить все пакеты из requirements.txt



    Запуск скрипта на питоне
        python C:\Users\e.nikolaev\selenium_course\lesson_1_6__step_2__find_element.py


    Запуск скрипта на PyTest
        pytest -v (verbose, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения:

        pytest C:\Users\e.nikolaev\selenium_course\lesson_1_6__step_10__unic_selector_asert.py
        pytest -v C:\Users\e.nikolaev\selenium_course\lesson_3_3__step_9__pytest.py
        pytest -v C:\Users\e.nikolaev\selenium_course\lesson_3_4__step_2__fixture.py





























'''