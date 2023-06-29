from src.item import Item
class MixKeyboard:

    #ID = 0
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        self.__language = "RU"
        return self
    @property
    def language(self): # для ошибки AttributeError: property 'language' of 'KeyBoard' object has no setter
        return self.__language




class KeyBoard(MixKeyboard):
    def __init__(self,name, price, quantity):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name



