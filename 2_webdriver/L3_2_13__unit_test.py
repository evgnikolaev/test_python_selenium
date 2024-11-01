from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


    
class TestAbs(unittest.TestCase):


    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        first_name = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        first_name.send_keys("Имя")

        last_name = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        last_name.send_keys("Фамилия")

        email = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        email.send_keys("Емайл")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "!!!!FAIL 11111 !!!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()








    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        first_name = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        first_name.send_keys("Имя")

        last_name = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        last_name.send_keys("Фамилия")

        email = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        email.send_keys("Емайл")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "!!!!FAIL 11111 !!!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


        

        
if __name__ == "__main__":
    unittest.main()




'''

unittest

Для этого нам понадобится выполнить следующие шаги:
    1. Импортировать unittest в файл: import unittest
    2. Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
    3. Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
    4. Изменить assert на self.assertEqual(), assertNotEqual, assertTrue, assertFalse
    5. Заменить строку запуска программы на unittest.main()

'''


