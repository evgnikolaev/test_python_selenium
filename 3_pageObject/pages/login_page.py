from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == 'https://selenium1py.pythonanywhere.com/ru/accounts/login/', "current_url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        input_password2.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        input_password2.click()
