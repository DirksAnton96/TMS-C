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



