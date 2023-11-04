class Soda:
    def __init__(self, dobavka: str = ""):
        self.dobavka = dobavka
    
    def show_my_drink(self):
        if self.dobavka == "":
            print("Usual sodovoay")
        else :
            print(f"Sodovoay and {self.dobavka}")

a = Soda()

b = Soda("cherry")

a.show_my_drink()

b.show_my_drink()

class TriangleChecker:
    def __init__(self, a: int = 2, b: int = 3, c: int = 4):
        self.a = a
        self.b = b
        self.c = c
    
    def __isnoll(self):
        if (self.a == 0) or (self.b == 0) or (self.c == 0):    
            return True
        else :
            return False
    
    def __isnegative(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            return True
        else:
            return False
    
    def __isstring(self):
        if type(self.a) == int and type(self.b) == int and type(self.c) == int:
            return False
        else :
            return True
    
    def __ispossibletobuild(self):
        if self.a < self.b + self.c or self.b < self.a +self.c or self.c < self.a + self.b:
            return True
        else:
            return False

    
    def is_triangle(self):
        if self.__isnoll():
            print("Ноль это не сторона!")
        elif self.__isstring():
            print("Нужно вводить только числа!")
        elif self.__isnegative():
            print("С отрицательными числами ничего не выйдет!")
        elif self.__ispossibletobuild():
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать.")

trieug = TriangleChecker()
trieug.is_triangle()

class KgToPounds:
    def __init__(self, kg: int = 0):
        self.__kg = kg
    
    def to_pounds(self):
        return self.__kg * 2.2046
    
    def set_kg(self, number):
        if type(number) == int or type(number) == float:
            self.__kg = number
        else :
            return 0
    
    def get_kg(self):
        return self.__kg

massa = KgToPounds(5)

print(f"Масса в наст момент в кг:   {massa.get_kg()}")
print(f"Масса в наст момент в фунтах:   {massa.to_pounds()}")

massa.set_kg(10)

print(f"Масса в наст момент в кг:   {massa.get_kg()}")
print(f"Масса в наст момент в фунтах:   {massa.to_pounds()}")


class KgToPounds:
    def __init__(self, kg: int | float = 0):
        self.__kg = kg
    
    def to_pounds(self) -> int | float:
        return self.__kg * 2.2046
    
    @property
    def kg(self) -> int | float :
        return self.__kg
    
    @kg.setter
    def kg(self, number: int | float):
        if type(number) == int or type(number) == float:
            self.__kg = number
        else :
            return 0
    
    def get_kg(self):
        return self.__kg

massa = KgToPounds(5)

print(f"Масса в наст момент в кг:   {massa.kg}")
print(f"Масса в наст момент в фунтах:   {massa.to_pounds()}")

massa.kg = 10

print(f"Масса в наст момент в кг:   {massa.kg}")
print(f"Масса в наст момент в фунтах:   {massa.to_pounds()}")

class RealString:
    def __init__(self, stroka1: str = "Apple", stroka2: str = "Яблоко"):
        self.__stroka1 = stroka1
        self.__stroka2 = stroka2
    
    def is_string_eq(self):
        if len(self.__stroka1) == len(self.__stroka2):
            print("Строки равны!")
            return True
        else :
            print("Строки не равны!")
            return False
    
    @property
    def stroka_1(self) -> str:
        return self.__stroka1
    
    @property
    def stroka_2(self) -> str:
        return self.__stroka2
    
    @stroka_1.setter
    def stroka_1(self, stroka):
        if type(stroka) == str:
            self.__stroka1 = stroka
        else:
            self.__stroka1 = self.__stroka1
    
    @stroka_2.setter
    def stroka_2(self,stroka):
        if type(stroka) == str:
            self.__stroka2 = stroka
        else :
            self.__stroka2 = self.__stroka2

stroks = RealString()
stroks.is_string_eq()
print(stroks.stroka_1)
print(stroks.stroka_2)

stroks.stroka_1 = "green"
stroks.stroka_2 = "Зелёные строки тут!"

stroks.is_string_eq()
print(stroks.stroka_1)
print(stroks.stroka_2)

stroks.stroka_1 = "green"
stroks.stroka_2 = "Зелён"

stroks.is_string_eq()
print(stroks.stroka_1)
print(stroks.stroka_2)

