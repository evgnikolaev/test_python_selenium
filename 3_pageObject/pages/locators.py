from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[text()='Посмотреть корзину']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register_form']//button")


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']//button")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//h1/following-sibling::p[1]")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']//*[contains(@class,'alert-safe')][1]//strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.XPATH, "//*[@id='messages']//*[contains(@class,'alert-safe')][3]//strong")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//*[@id='content_inner']//*[contains(text(),'Ваша корзина пуста')]")
