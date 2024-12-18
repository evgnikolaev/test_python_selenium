import pytest

import time

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


#  тесты для авторизованного пользователя

class TestUserAddToBasketFromProductPage():

    # регистрируем, логиним пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser_conftest):
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser_conftest, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakemail$org"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser_conftest):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser_conftest, link)
        page.open()
        page.add_product_to_basket()
        page.should_product_added_to_basket()

    def test_user_cant_see_success_message(self, browser_conftest):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser_conftest, link)
        page.open()
        page.should_not_be_success_message()


#  тесты под неавторизованного пользователя

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser_conftest, link):
    # link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser_conftest, link)
    page.open()
    page.add_product_to_basket()
    page.should_product_added_to_basket()


def test_guest_cant_see_success_message(browser_conftest):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser_conftest, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser_conftest):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser_conftest, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser_conftest):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser_conftest, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser_conftest):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser_conftest, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser_conftest):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser_conftest, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser_conftest, browser_conftest.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser_conftest):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser_conftest, link)
    page.open()
    # page.add_product_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser_conftest, browser_conftest.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
