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

    def __init__(self, obg: Product):
        self.obg.id = id
        self.obg.name = name
        self.obg.price = price
        self.obg.diametr = diametr
        self.obg.content = ConnectionResetError
        self.obg.volume = volume

    def add_product(self, obg: Product):
        pass

    def sell_product(self, obg: Product):
        pass

    def all_products(self) -> Product:
        pass


    

    


