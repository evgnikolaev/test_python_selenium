from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# step 8
def test_input_text(expected_result, actual_result):
  assert expected_result == actual_result , f"expected {expected_result}, got {actual_result}"

test_input_text(11, 11)





# step 9
def test_substring(full_string, substring):
  assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)

test_substring('fulltext', 'some_value')
test_substring('some_text', 'some')




'''
assert - проверяет истинность утверждений.  
    assert True  - не приводит к выводу дополнительных сообщений
    assert False - вызовет исключение AssertionError

assert abs(-42) == 42                                                       
assert abs(-42) == -42                                                      исключение AssertionError                     
assert abs(-42) == -42, "Should be absolute value of a number"              исключеение с текстом - AssertionError: Should be absolute value of a number



Форматирование строк:
    print("Wrong text, got " + actual_result + ", something wrong")                                 Конкатенация строк
    print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))      Функция str.format  для строки

    actual_result = "abrakadabra"
    print(f"Wrong text, got {actual_result}, something wrong")




Вхождение подстроки:
    s = 'My Name is Julia'

    ключевое слово in (вернет true/false)
      if 'Name' in s:
          print('Substring found')


    функция find ( вернет индекс первого вхождения подстроки в строку и -1, если подстрока не найдена. )
      index = s.find('Name')
      if index != -1:
          print(f'Substring found at index {index}')





print(globals)  - служебные переменные  
__name__ хранит имя модуля  
                      "__main__" - скрипт запущен смостоятельно (по сути это точка входа в приложение),  
                      "имя модуля" - когда был импорт модуля в другой модуль

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")

'''


