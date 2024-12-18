
'''

Для PyTest написано большое количество плагинов
https://docs.pytest.org/en/latest/explanation/flaky.html#plugins

Полный список доступных плагинов доступен здесь
https://docs.pytest.org/en/latest/reference/plugin_list.html




плагин pytest-rerunfailures
будем перезапускать упавший тест (вдуг упал из-за неполадок интернета, или еще что-то), чтобы еще раз убедиться, что он действительно нашел баг, а не упал случайно.

    1) pip install pytest-rerunfailures   (Установим плагин)
    2) pytest -v --tb=line --reruns 1 --browser_name=chrome .\2_webdriver\L3_6_8__plugins.py   (Запустим)

            --reruns n    - где n — это количество перезапусков.
            --tb=line     - чтобы сократить лог с результатами теста.


'''
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser_conftest):
    browser_conftest.get(link)
    browser_conftest.find_element(By.CSS_SELECTOR, "#login_link")


# этот тест перезапустится автоматически еще раз
def test_guest_should_see_login_link_fail(browser_conftest):
    browser_conftest.get(link)
    browser_conftest.find_element(By.CSS_SELECTOR, "#magic_link")


