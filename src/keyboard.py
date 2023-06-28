from src.item import Item
class MixKeyboard:

    #ID = 0
    def __init__(self):
        self.language = "RU"
        #MixKeyboard.ID +=1

        #if MixKeyboard.ID == 1:
            #self.language = "RU"
        #elif MixKeyboard.ID == 2:
            #self.language = "RU"

class KeyBoard(MixKeyboard):
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.language = "EN"
        #self.__language = "EN"  # для ошибки AttributeError: property 'language' of 'KeyBoard' object has no setter


    #@property
    #def language(self): # для ошибки AttributeError: property 'language' of 'KeyBoard' object has no setter
        #return self.__language
    def __str__(self):
        return self.name
    def change_lang(self):
        super().__init__()
        return self



