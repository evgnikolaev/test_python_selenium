import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_exception1():
    try:
        browser = webdriver.Chrome()
        # browser.get("http://selenium1py.pythonanywhere.com/")
        browser.get("https://selenium1py.pythonanywhere.com/ru/accounts/login/")

        link = browser.find_element(By.XPATH, '//button[@name="login_submit"]')

        inputEmail = browser.find_element(By.XPATH, '//*[@name="login-username"]')

        inputEmail.send_keys('adasdasdasdasd')
        time.sleep(3)
        inputEmail.send_keys(Keys.CONTROL,'a')
        time.sleep(3)
        inputEmail.clear()
        time.sleep(3)

        # time.sleep(10)

    finally:
        browser.quit()


'''



'''


