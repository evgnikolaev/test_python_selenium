from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get(url)

'''
Explicit Waits - явное ожидание. Задаем expected_conditions:
    title_is
    title_contains
    presence_of_element_located
    visibility_of_element_located
    visibility_of
    presence_of_all_elements_located
    text_to_be_present_in_element
    text_to_be_present_in_element_value
    frame_to_be_available_and_switch_to_it
    invisibility_of_element_located
    element_to_be_clickable
    staleness_of
    element_to_be_selected
    element_located_to_be_selected
    element_selection_state_to_be
    element_located_selection_state_to_be
    alert_is_present


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
'''

# Ждем пока текст станет = $100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )


button1 = browser.find_element(By.ID, "book")
button1.click()

x_element = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys( calc(x_element) )


button2 = browser.find_element(By.ID, "solve")
button2.click()


time.sleep(10)

