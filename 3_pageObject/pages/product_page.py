from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        # sleep(530)

    def should_product_added_to_basket(self):
        self.name_matches_message()
        self.price_matches_message()

    def name_matches_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name.text == product_name_in_message.text, "Не добавился в корзину, Названия не совпадают"

    def price_matches_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert product_price.text == product_price_in_message.text, f'Не добавился в корзину, Цены не совпадают [{product_price.text}] и [{product_price_in_message.text}]'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Not dissapired"
