from faulthandler import is_enabled

import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestAuth:
    text_answer = ''

    @pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    # @pytest.mark.parametrize('num', ["236898"])
    def test_auth(self, browser, num):
        link = f"https://stepik.org/lesson/{num}/step/1"
        browser.implicitly_wait(10)
        browser.get(link)

        #  1) авторизовались
        popup_btn = browser.find_element(By.XPATH, "//a[contains(@class,'navbar__auth_login')]")
        popup_btn.click()

        login = browser.find_element(By.ID, "id_login_email")
        login.send_keys("ХХХ")

        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys("ХХХ")

        form_btn = browser.find_element(By.XPATH, "//*[@id='login_form']//button")
        form_btn.click()


        #  2) ввод ответа (если есть кнопка "Решить заново", то сперва нажимаем ее)
        try:
            again_btn = WebDriverWait(browser, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'again-btn')][text()='Решить снова']"))
            )
            if again_btn:
                again_btn.click()
        except Exception:
            print('\n--Нет кнопки "Решить заново"')

        time.sleep(1)
        textarea = browser.find_element(By.XPATH, "//textarea[contains(@class,'ember-text-area')]")
        answer = math.log(int(time.time()))
        textarea.clear()
        textarea.send_keys(answer)
        submit = browser.find_element(By.XPATH, "//button[contains(@class,'submit-submission')]")
        submit.click()

        hint = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )

        self.text_answer += hint.text
        print('\n---', self.text_answer)
        assert hint.text == 'Correct!', f"\n.............expected {hint.text}, got {hint.text}"
