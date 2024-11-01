from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get(url)

'''

Implicit и Explicit Waits
при асинхронной работе скриптов или задержек от сервера


Implicit wait - неявное ожидание (Не надо явно указывать каждый раз, когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды.)
WebDriver каждые 0.5 секунды проверяет, появился ли элемент

browser.implicitly_wait(5)

'''

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text


time.sleep(10)

