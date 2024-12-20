from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), 'Корзина не пуста при клике посмотреть в корзине, товары не добавлялись'

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), 'Нет сообщения "Корзиина пуста" при клике посмотреть в корзине, товары не добавлялись'
