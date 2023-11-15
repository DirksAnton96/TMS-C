from dataclasses import dataclass, field
from .abstract import Product
from .realshop import RealShop

@dataclass
class Book(Product):
    isdanie: int
    isjournal: bool = False
    
    

class BookShops(RealShop):
    
    def __init__(self):
        self._value_in_shop = []

    def add_product(self, obg: Book):
        if self.is_valid(obg): 
            self._value_in_shop.append(obg)

    def sell_product(self, obg: Book):
        if self.is_valid(obg): 
            self._value_in_shop.remove(obg)

    def all_products(self) -> Book:
        return self._value_in_shop
    
    
    def is_valid(self, product: Book) -> bool:
        if not isinstance(product,Book):
            raise NonProductError(f"переданый экземпляп не является экземпляром класса Book - NonProductError")
        else:
            return True


