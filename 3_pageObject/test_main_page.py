import pytest

from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage():

    # тестовая фикстура для тестов в классе
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.data = 'подготовленные данные'
        print("Подготавливаем данные для тестов 1")
        yield
        print("Удаляем те данные, которые мы создали 2 ")

    def test_guest_can_go_to_login_page(self, browser_conftest):
        print("Выполняем тест 3." + self.data)
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser_conftest, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser_conftest, browser_conftest.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser_conftest):
        print("Выполняем тест 4")
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser_conftest, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser_conftest):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser_conftest, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser_conftest, browser_conftest.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
