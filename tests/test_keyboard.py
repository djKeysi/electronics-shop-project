from src.keyboard import KeyBoard, MixKeyboard

import pytest


@pytest.fixture
def keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)


@pytest.fixture
def mixkeyboard():
    return MixKeyboard()


def test_init(keyboard):
    assert keyboard.name == "Dark Project KD87A"
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == "EN"
    assert str(keyboard.name) =="Dark Project KD87A"


def test_change_lang(mixkeyboard):
    assert str(mixkeyboard.language) == "EN"


def test_getters(keyboard):
    assert str(keyboard.language) == "EN"


def test_init_mixkeyboard(mixkeyboard):
    assert str(mixkeyboard.language) == "EN"
    assert mixkeyboard.language == "EN"

#def test_change_language(keyboard):
 #   assert keyboard.change_lang() == "RU"
