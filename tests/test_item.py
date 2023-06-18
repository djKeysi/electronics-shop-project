"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest

@pytest.fixture
def items():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    item1=Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item1=Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.price*item1.pay_rate*0.8 == 8000.0
    assert item2.price*item2.pay_rate== 20000

def test_init():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.name == "Смартфон"
    #assert item1.all == ['src.item.Item object at 0x7f91b2826ad0']

def test_string_to_number(items):
    assert items.string_to_number('5') == 5
    assert items.string_to_number('5.0') == 5
    assert items.string_to_number('5.5') == 5

def test_instantiate_from_csv(items):
    assert items.all == []

def test_getters(items):
    assert items.name == "Смартфон"

def test_setters(items):
    items.name = "Телефон"
    assert items.name == "Телефон"
