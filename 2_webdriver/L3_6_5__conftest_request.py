
'''

Conftest.py и передача параметров в командной строке

    В файле  conftest.py добавляем:


                        import pytest
                        from selenium import webdriver

                        def pytest_addoption(parser):
                            parser.addoption('--browser_name', action='store', default="chrome",
                                             help="Choose browser: chrome or firefox")


                        @pytest.fixture(scope="function")
                        def browser_conftest(request):
                            browser_name = request.config.getoption("browser_name")
                            browser = None
                            if browser_name == "chrome":
                                print("\nstart chrome browser for test..")
                                browser = webdriver.Chrome()
                            elif browser_name == "firefox":
                                print("\nstart firefox browser for test..")
                                browser = webdriver.Firefox()
                            else:
                                raise pytest.UsageError("--browser_name should be chrome or firefox")
                            yield browser
                            print("\nquit browser..")
                            browser.quit()



-------------------------------------------------------------
    Это делается с помощью встроенной функции pytest_addoption и фикстуры request:
    browser_name = request.config.getoption("browser_name")



    pytest -s -v  .\2_webdriver\L3_6_5__conftest_request.py
    Если запустить без параметра, будет ошибка.
    Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:

                        parser.addoption('--browser_name', action='store', default="chrome",
                                         help="Choose browser: chrome or firefox")

                        pytest_addoption - функция должна быть прописана в conftest.py, иначе обибки

    pytest -s -v --browser_name=chrome .\2_webdriver\L3_6_5__conftest_request.py

'''

def test_guest_should_see_login_link(browser_conftest):
    print("\n..........07")
    link = "http://selenium1py.pythonanywhere.com/"
    browser_conftest.get(link)


