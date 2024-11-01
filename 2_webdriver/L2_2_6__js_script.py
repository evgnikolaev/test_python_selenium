from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

  
url = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(url)


'''

# JS скрипты
browser.execute_script("document.title='Script executing';alert('Robots at work');")

# Варинаты js-скролла страницы до кнопки:
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.execute_script("button = document.getElementsByTagName('button')[0];button.scrollIntoView(true);")

'''


button = browser.find_element(By.ID, "input_value")

x_element = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys( calc(x_element) )


browser.find_element(By.ID, "robotCheckbox").click()


browser.execute_script("inp = document.getElementById('robotsRule');inp.scrollIntoView(true);")
browser.find_element(By.ID, "robotsRule").click()



browser.execute_script("button = document.getElementsByTagName('button')[0];button.scrollIntoView(true);")
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(10)

