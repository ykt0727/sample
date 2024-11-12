class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

x = Item('burger', 100)
#x.price = -100
print(x.name, x.price)