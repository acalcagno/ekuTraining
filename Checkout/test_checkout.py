import pytest
from Checkout import Checkout

@pytest.fixture()
def co():
    co = Checkout()
    co.addItemPrice("cheese", 2)
    co.addItemPrice("chocolate", 3)
    return co


def test_total_for_multiple_items(co):
    co.addItem("cheese")

    total = co.getTotal()

    assert total == 2
    

def test_total_for_different_items(co):
    co.addItem("cheese")
    co.addItem("chocolate")

    total = co.getTotal()

    assert total == 5


def test_can_add_discount(co):
    co.addDiscount("cheese", 3, 2)


def test_can_apply_discount(co):
    co.addDiscount("cheese", 3, 2)
    co.addItem("cheese")
    co.addItem("cheese")
    co.addItem("cheese")

    total = co.getTotal()

    assert total == 2


def test_exception_with_item_without_price(co):
    with pytest.raises(Exception):
        co.addItem("sand")
