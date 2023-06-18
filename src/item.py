import csv
FILE_CSV = "items.csv"
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
        Item.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity


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
    def instantiate_from_csv(cls,file):
        cls.all = []
        with open(file, newline='',encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.all.append(row["name"])
            return cls.all


    @staticmethod
    def string_to_number(word):
        if word.isdigit():
            return int(word)
        else:
            return float(word[0])


#print(Item.instantiate_from_csv("items.csv"))









