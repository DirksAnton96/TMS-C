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

class NonProductError(ValueError):
    pass

class RealShop(AbstractShop):

    def __init__(self):
        self._value_in_shop = []

    def add_product(self, obg: Product):
        self._value_in_shop.append(obg)

    def sell_product(self, obg: Product):
        self._value_in_shop.remove(obg)

    def all_products(self) -> Product:
        return self._value_in_shop
    
    def is_valid(self, product: Product) -> bool:
        if not isinstance(product,Product):
            raise NonProductError(f"переданый экземпляп не является экземпляром класса Product - NonProductError")
        else:
            return True
    



# class Validator:

#     def __init__(self, product: Product):
#         self._product = product
    
#     def is_valid(self):
#         if not isinstance(self._product,Product):
#             raise NonProductError(f"переданый экземпляп не является экземпляром класса Product - NonProductError")
#         else:
#             return True
#         # try:
#         #     return isinstance(self._product, Product)
#         # except ValueError:
#         #     raise NonProductError(f"переданый экземпляп не является экземпляром класса Product - NonProductError")

@dataclass
class Furniture():
    id: int
    name: str
    price: float
    hight: float

@dataclass
class Table(Furniture):
    diametr: float
    type_table: str
    

@dataclass
class Chair(Furniture):
    type_chair: str
    width: float

@dataclass
class Closet(Furniture):
    type_closet: list
    color: str


class ShopFurniture(AbstractShop):
    
    def __init__(self):
        self._value_in_shop = []
    
    def add_product(self, furniture: Furniture):
        if self.__is_valid(furniture):
            self._value_in_shop.append(furniture)

    def sell_product(self, furniture: Furniture):
        if self.__is_valid(furniture):
            self._value_in_shop.remove(furniture)
            

    def all_products(self) -> Furniture:
        return self._value_in_shop
    
    def __is_valid(self, furniture: Furniture) -> bool:
        if not isinstance(furniture,Furniture):
            raise NonProductError(f"переданый экземпляп не является экземпляром класса Furniture - NonProductError")
        else:
            return True


table_1 = Table(1,"Чешский",15.5,4.1,2.0,"Кухонный")

chair_1 = Chair(1,"Офисный",25.5,3.1,"Комфортный",1.2)

closet_1 = Closet(1,"Большой",14.4,1.2,["Деревенский", "Домашний", "BloceRose"],"Green")

shf_1 = ShopFurniture()

shf_1.add_product(table_1)
shf_1.add_product(chair_1)
shf_1.add_product(closet_1)

print(shf_1.all_products())

shf_1.sell_product(chair_1)

print(shf_1.all_products())



pizza_1 = Pizza(1,"Margarita",20.6,17,["майнез","кетчуп","сыр"])
coffee_1 = Coffee(1,"якобс",14.5,0.3,"крепкий")

pr = RealShop()

# validatator = Validator(pr)

pr.add_product(pizza_1)
pr.add_product(coffee_1)

print(pr.all_products())

pr.sell_product(pizza_1)
print(pr.all_products())

print(pr.is_valid(coffee_1))

shf_1.add_product(pizza_1)

shf_1.is_valid(table_1)
shf_1.is_valid(coffee_1)

    

    


