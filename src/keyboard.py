from src.item import Item


class MixKeyboard:

    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):  # для ошибки AttributeError: property 'language' of 'KeyBoard' object has no setter
        return self.__language

    # @language.setter
    # def language(self, value):
    #     self.__language = value


class KeyBoard(Item, MixKeyboard):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)