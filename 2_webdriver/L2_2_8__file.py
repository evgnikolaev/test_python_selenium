from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

  
url = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(url)


# Работа с файлами
# import os 

# print(os.path.abspath(__file__))                               вернет абсолютный путь -    C:\Users\e.nikolaev\selenium_course\lesson_2_2__step_8__file.py
# print(os.path.abspath(os.path.dirname(__file__)))              вернет директорию  -        C:\Users\e.nikolaev\selenium_course


# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path)                                # добавляем файл инпуту


browser.find_element(By.NAME, "firstname").send_keys("name")
browser.find_element(By.NAME, "lastname").send_keys("lastname")
browser.find_element(By.NAME, "email").send_keys("qw@qw.ru")


current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file_2_2__step_8.txt')
browser.find_element(By.NAME, "file").send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()


time.sleep(10)

