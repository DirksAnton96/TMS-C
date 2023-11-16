from dataclasses import dataclass, field

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class Book(Product):
    isdanie: int
    isjournal: bool = False

@dataclass
class Computer(Product):
    country: str
    isfullcomplectetion: bool = False