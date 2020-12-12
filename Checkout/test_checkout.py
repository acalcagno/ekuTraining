from Checkout import Checkout
import pytest


@pytest.fixture()
def checkout():
    return Checkout()


def test_calculates_total(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")

    assert checkout.calculateTotal() == 1


def test_calculates_total_with_two_items(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    checkout.addItem("a")

    assert checkout.calculateTotal() == 2

def test_calculates_total_with_two_different_items(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    checkout.addItem("a")
    checkout.addItem("b")

    assert checkout.calculateTotal() == 3

def test_can_add_discount(checkout):
    pass
