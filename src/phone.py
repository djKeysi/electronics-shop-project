from src.item import Item

class Phone(Item):
    def __init__(self,name, price, quantity,number_of_sim ):
        super().__init__(name, price, quantity)

        self.number_of_sim =number_of_sim
        #if isinstance(self.number_of_sim<=0,int):
            #raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"{Phone.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name