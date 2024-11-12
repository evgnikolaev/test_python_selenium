import pytest



class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login___1(self):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket___2(self):
        assert True




class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page___3(self):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price___4(self):
        assert True




@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket___5(self):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price___6(self):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue___7():
    assert True


# pytest -v -m "smoke and not beta_users"  .\2_webdriver\L3_5_2__mark.py
# Результаты  1 и 4