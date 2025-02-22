"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item,InstantiateCSVError
from src.phone import Phone
import pytest

@pytest.fixture
def items():
    return Item("Смартфон", 10000, 20)
@pytest.fixture
def instantiateCSVerror():
    return InstantiateCSVError("Message")
@pytest.fixture
def phones():
    return Phone("iPhone 14", 120_000, 5, 2)

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

def test_string_to_number(items):
    assert items.string_to_number('5') == 5
    assert items.string_to_number('5.0') == 5
    assert items.string_to_number('5.5') == 5
    assert items.string_to_number('55.5') == 5

def test_instantiate_from_csv(items,instantiateCSVerror):
    assert Item.all[0].name == "Смартфон"
    with pytest.raises(FileNotFoundError):
        open(".../src/item.csv")
    assert instantiateCSVerror.message == "Message"




   #with pytest.raises(InstantiateCSVError,match='must be positive'):
       #items.instantiate_from_csv()


def test_getters(items):
    assert items.name == "Смартфон"

def test_setters(items):
    items.name = "Телефон"
    assert items.name == "Телефон"
    items.name = "Смартфон"
    assert items.name == "Смартфон"
    items.name = "Сотовый"
    assert items.name == "Сотовый"

def test_str_repr(items):
    assert repr(items) == "Item('Смартфон', 10000, 20)"
    assert str(items) == 'Смартфон'

def test_add(items,phones):
    assert items + phones == 25
    assert phones + phones == 10

