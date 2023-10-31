class Auto:

    brande = ""
    age = 0
    color = ""
    mark = ""
    weight = 0.0

    def __init__(self, brande, age, mark):
        self.brande = brande
        self.age = age
        self.mark = mark

    

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


auto_v1 = Auto("Mersedes",0,"G-14")
auto_v1.move()
auto_v1.stop()
auto_v1.auto_print()
auto_v1.color_set("black")
auto_v1.weight_set(2.5)
auto_v1.birthday()
auto_v1.birthday()
auto_v1.auto_print()