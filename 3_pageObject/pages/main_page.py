from .base_page import BasePage


class MainPage(BasePage):
    ''' Вынесли в BasePage
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        alert = self.browser.switch_to.alert
        alert.accept()
     '''

    # Как вы уже знаете, метод __init__ вызывается при создании объекта.
    # Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
