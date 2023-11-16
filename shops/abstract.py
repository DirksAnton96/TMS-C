from abc import ABC, abstractmethod
from .product import Product

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



