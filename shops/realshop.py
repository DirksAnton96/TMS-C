from .abstract import AbstractShop, Product

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