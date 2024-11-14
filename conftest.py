import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser_conftest():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()