import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        #return "Item('Смартфон', 10000, 20)"
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"
    def __str__(self):
        return self.__name
    def __add__(self, other):
        if issubclass(other.__class__,self.__class__):
            return self.quantity + other.quantity
        raise Exception


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price*=self.pay_rate

    @property
    def name(self):

        return self.__name
    @name.setter
    def name(self,value):
        if len(value) >= 10:
            #print("Длина наименования товара превышает 10 символов")
            print(value[:10])
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        file = "../src/items.csv"
        with open(file,encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(word):
        if word.isdigit():
            return int(word)
        else:
            return float(word[0])










