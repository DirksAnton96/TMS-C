from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class Pizza(Product):
    diametr: int
    content: list

@dataclass
class Coffee(Product):
    volume: float
    type_coffee: str

class AbstractShop(ABC):

    @abstractmethod
    def add_product(self, obg: Product):
        """
        add product
        """
    
    @abstractmethod
    def sell_product(self, obg: Product):
        """
        sell product
        """
        
    @abstractmethod
    def all_products(self) -> Product:
        """
        all products
        """

class RealShop(AbstractShop):

    def __init__(self):
        self._value_in_shop = []

    def add_product(self, obg: Product):
        self._value_in_shop.append(obg)

    def sell_product(self, obg: Product):
        self._value_in_shop.remove(obg)

    def all_products(self) -> Product:
        return self._value_in_shop

pizza_1 = Pizza(1,"Margarita",20.6,17,["майнез","кетчуп","сыр"])
coffee_1 = Coffee(1,"якобс",14.5,0.3,"крепкий")

pr = RealShop()

pr.add_product(pizza_1)
pr.add_product(coffee_1)

print(pr.all_products())

pr.sell_product(pizza_1)
print(pr.all_products())
    


    

    


