from src.phone import Phone
import pytest

@pytest.fixture
def phones():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_init(phones):
    assert phones.name == "iPhone 14"
    assert phones.price == 120_000
    assert phones.quantity == 5
    assert phones.number_of_sim == 2

def test_str_repr(phones):
    assert str(phones) == 'iPhone 14'
    assert repr(phones) == "Phone('iPhone 14', 120000, 5, 2)"
