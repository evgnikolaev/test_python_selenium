from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(url)

'''

alert
alert = browser.switch_to.alert
alert.accept()                      - нажать на кнопку ОК
alert_text = alert.text             - получить alert-текст


confirm
confirm = browser.switch_to.alert
confirm.accept()                    - нажать на кнопку ОК
confirm.dismiss()                   - нажать на кнопку Отмена


prompt
prompt = browser.switch_to.alert
prompt.send_keys("My answer")       - Заполнить поле prompt
prompt.accept()                     - нажать на кнопку ОК


'''

browser.find_element(By.CSS_SELECTOR, "button.btn").click()
confirm = browser.switch_to.alert
confirm.accept()


x_element = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys( calc(x_element) )

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(10)

