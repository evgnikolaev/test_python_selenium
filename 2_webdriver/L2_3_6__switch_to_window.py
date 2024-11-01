from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(url)

'''

При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти:

browser.switch_to.window(window_name)

new_window = browser.window_handles[1]          - имя второй вкладки    
first_window = browser.window_handles[0]        - имя текущей вкладки

'''

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

new_window = browser.window_handles[1] 
browser.switch_to.window(new_window)


x_element = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys( calc(x_element) )

browser.find_element(By.CSS_SELECTOR, "button.btn").click()


time.sleep(10)

