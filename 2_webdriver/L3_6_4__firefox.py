



from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()
driver.get("https://stepik.org/lesson/25969/step/8")
driver.quit()


'''

запуск тестов с firefox:
    https://stepik.org/lesson/237240/step/6?unit=209628
    https://selenium-python.com/install-geckodriver


    pytest -s -v --browser_name=firefox test_cmd.py            --browser_name - в каком браузере запустить тест
    
'''









