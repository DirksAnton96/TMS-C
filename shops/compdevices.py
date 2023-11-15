from dataclasses import dataclass, field
from .abstract import Product
from .realshop import RealShop

@dataclass
class Computer(Product):
    country: str
    isfullcomplectetion: bool = False

class ComputerShops(RealShop):
    
    def __init__(self):
        self._value_in_shop = []

    def add_product(self, obg: Computer):
        if self.is_valid(obg): 
            self._value_in_shop.append(obg)

    def sell_product(self, obg: Computer):
        if self.is_valid(obg): 
            self._value_in_shop.remove(obg)

    def all_products(self) -> Computer:
        return self._value_in_shop
    
    
    def is_valid(self, product: Computer) -> bool:
        if not isinstance(product,Computer):
            raise NonProductError(f"переданый экземпляп не является экземпляром класса Book - NonProductError")
        else:
            return True
