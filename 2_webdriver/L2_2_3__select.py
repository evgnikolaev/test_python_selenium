from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


  
url = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(url)


'''

# Селекты
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

'''

x1 = browser.find_element(By.ID, "num1").text
x2 = browser.find_element(By.ID, "num2").text
y = int(x1) + int(x2)


browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "[value='" + str(y) + "']").click()

browser.find_element(By.CSS_SELECTOR, "button.btn").click()


time.sleep(10)

