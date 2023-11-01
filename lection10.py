import time

class Auto:  

    def __init__(self, brande, age, mark,color: str = "White",weight: float = 1.5):
        self.brande = brande
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    

    def move(self) -> str:
        move = "move"
        print(move)
        return move
    
    def stop(self) -> str:
        stroka = "stop"
        print(stroka)
        return stroka
    
    def birthday(self) -> int:
        self.age += 1
        return self.age
    
    def auto_print(self):
        print(self.brande,self.age,self.color,self.mark,self.weight)
    
    def color_set(self,new_color: str) -> str:
        self.color = new_color
        return self.color
    
    def weight_set(self, new_weight: int | float) -> int | float:
        self.weight = new_weight
        return self.weight



class Truck(Auto):

    def __init__(self,max_load, brande, age, mark, color: str = "White",weight: float = 1.5):
        super().__init__(brande, age, mark, color, weight)
        self.max_load = max_load
    
    def move(self) -> str:
        print("Attention")
        super().move()

    def load(self) -> str:
        stroka = "Load"
        time.sleep(1)
        print(stroka)
        time.sleep(1)
        return stroka
    
    def truck_print(self):
        super().auto_print()
        print(self.max_load)
    
class Car(Auto):

    def __init__(self,max_speed,brande, age, mark, color: str = "White",weight: float = 1.5):
        super().__init__(brande, age, mark, color, weight)
        self.max_speed = max_speed
    
    def move(self) -> str:
        super().move()
        stroka = "Max speed is " + self.max_speed
        print(stroka)
        return stroka
    
    def car_print(self):
        super().auto_print()
        print(self.max_speed)
    





truck_v1 = Truck(100,"Mersedes",0,"G-15")

truck_v2 = Truck(130,"Porshe",2,"A-15")

car_v1 = Car(120,"Scania",0,"P-10")

car_v2 = Car(150,"Reno",5,"Z-15")


truck_v1.truck_print()
truck_v2.truck_print()

car_v1.car_print()
car_v2.car_print()
auto_v1 = Auto("Mersedes",0,"G-14")
auto_v1.move()
auto_v1.stop()
auto_v1.auto_print()
auto_v1.color_set("black")
auto_v1.weight_set(2.5)
auto_v1.birthday()
auto_v1.birthday()
auto_v1.auto_print()