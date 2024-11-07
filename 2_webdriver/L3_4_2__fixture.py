from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n..........01")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("..........02")
        self.browser.quit()


    def test_guest_should_see_login_link(self):
        print("..........03")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("..........04")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")



class TestMainPage2():

    def setup_method(self):
        print("..........101")
        self.browser = webdriver.Chrome()


    def teardown_method(self):
        print("..........102")
        self.browser.quit()


    def test_guest_should_see_login_link(self):
        print("..........103")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("..........104")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")




'''

Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.
Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами

pytest  -s  2_webdriver/L3_4_2__fixture.py        // -s, чтобы увидеть текст, который выводится командой print().



 - префиксы setup_*, teardown_* отвечают за порядок исполнения фикстур: до чего-то, после чего-то.
 - постфиксы *_class, *_method и другие отвечают за уровень применения фикстур: ко всему классу, к каждому методу в классе и тд.

    Исходя их логики выше:
    
        setup_class - выполняется один раз перед запуском всех тестовых методов в классе
        teardown_class  - выполянется один раз после
        setup_method  - выполняется перед запуском каждого тестового метода в классе
        teardown_method - выполняется каждый раз после

    Про декоратор:
    @classmethod декоратор, использованный для удобства чтения кода. Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу.








'''


