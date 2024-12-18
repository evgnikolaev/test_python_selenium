from time import process_time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser_conftest):
    browser_conftest.get(link)
    browser_conftest.find_element(By.CSS_SELECTOR, "#login_link")
    print("...........from conftest.py..........")


'''

   Conftest.py — конфигурация тестов (одна фикстура на несколько файлов, чтобы в каждом файле не описывать)

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


'''


