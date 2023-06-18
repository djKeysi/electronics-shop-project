"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest

@pytest.fixture
def items():
    return Item("Смартфон", 10000, 20)
@pytest.fixture
def items2():
    return Item.all[0]

def test_calculate_total_price(items):
    assert items.calculate_total_price() == 200000

def test_apply_discount(items):
    item1=Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.price*item1.pay_rate*0.8 == 8000.0
    assert item2.price*item2.pay_rate== 20000


def test_init(items):
    assert items.price == 10000
    assert items.quantity == 20
    assert items.name == "Смартфон"
    #assert item1.all == ['src.item.Item object at 0x7f91b2826ad0']

def test_string_to_number(items):
    assert items.string_to_number('5') == 5
    assert items.string_to_number('5.0') == 5
    assert items.string_to_number('5.5') == 5
    assert items.string_to_number('55.5') == 5

def test_instantiate_from_csv(items2):
    pass
    #assert items2.all[0] == "<src.item.Item object at 0x7f01221aa910>"
    #assert len(Item.all) == 0

def test_getters(items):
    assert items.name == "Смартфон"

def test_setters(items):
    items.name = "Телефон"
    assert items.name == "Телефон"
    items.name = "Смартфон"
    assert items.name == "Смартфон"
    items.name = "Сотовый"
    assert items.name == "Сотовый"

