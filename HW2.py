####Сумма трёх чисел
#
#number_1 = int(input("enter first number: "))
#number_2 = int(input("enter second number: "))
#number_3 = int(input("enter third number: "))

#print("sum of all numbers: ", number_1 + number_2 + number_3)

#### Следующее и предыдущее 
#Напишите программу, которая считывает целое число, после чего на 
#экран выводится следующее и предыдущее целое число с 
#пояснительным текстом. 

#number_1 = int(input("enter the number: "))

#print("the next number: ", number_1 + 1)
#print("the privious number: ", number_1 -1)

#Расстояние в метрах 
#Напишите программу, которая находит полное число метров по 
#заданному числу сантиметров. 

#number_of_sm = int(input("enter the number of sm: "))
#print("the number of meters: ", number_of_sm//100)


#Пересчет временного интервала 
#Напишите программу для пересчёта величины временного интервала, 
#заданного в минутах, в величину, выраженную в часах и минутах. 

#number_of_minutes = int(input("enter the number of minutes: "))

#print("number of hours: ",number_of_minutes//60,  "number of minutes: ",  number_of_minutes%60)

#Трехзначное число 
#Напишите программу, в которой рассчитывается сумма и произведение 
#цифр положительного трёхзначного числа. 

#number = input("enter the number 3x: ")

#print("the sum of numbers: ",int(number[0])+int(number[1])+int(number[2]))
#print("operation * of the numbers: ", int(number[0])*int(number[1])*int(number[2]))

#Четное или нечетное? 
#Напишите программу, которая определяет, является число четным или 
#нечетным.

#number = int(input("the number: "))
#print("Чётное: ", number % 2 ==0)

#Квадрат 
#Написать программу, принимающую сторону квадрата, и возвращающую 
# 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата. 

#number = int(input("enter the number: "))
#print("периметр квадрата: ", number*4, " площадь квадрата: ", number*number, " диагональ квадрата: ", number*(2**0.5))

#СПИСКИ 
#1. Создать произвольный список длиной в 3 элемента 
#2. Добавить новый элемент типа str в конец списка 
#3. Добавить новый элемент типа int на первое место в списке 
#4. Добавить новый элемент типа list в конец списка 
#5. Добавить новый элемент типа tuple на место с индексом 2 
#6. Удалить первый элемент списка 
#list_v = []
#list_v.append(input("first value: "))
#list_v.append(input("second value: "))
#list_v.append(input("third value: "))

#list_v.append(input("enter string: "))

#list_v.insert(0,int(input("enter int: ")))

#list_v.append(list(input("enter string: ")))

#list_v.insert(2,tuple(input("enter string for tuple: ")))

#del list_v[0]

#print(list_v)


#Простой Фибоначчи 
#Написать программу, которая принимает на вход n, где 𝑛 ∈ [1; 20], а на 
#выходе выдает число Фибоначчи, которое находится под этим номером. 
#Подсказка: последовательность всегда одинаковая, а диапазон вводимых чисел в задании жестко ограничен

#list_f=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,621,998,1619,2617,4236,6853]
#number = int(input("Enter value from 1 to 20: "))
#print(list_f[number-1])

#Выбрать нижний
# На вход программе подается число n, где 𝑛 ∈ [1; 20], а на выходе 
# необходимо вывести элемент из данной прогрессии в виде вещественного 
# числа.

#list_ar = [1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10,1/11,1/12,1/13,1/14,1/15,1/16,1/17,1/18,1/19,1/20,1/21]
#number = int(input("enter value from 1 to 20: "))
#print(list_ar[number-1])

#Вычислить длину
#Программа должна вычислять длину отрезка по двум точкам в декартовой системе координат. 
#Длина отрезка по двум точкам в декартовой системе координат вычисляется по формуле: 
#где (x1,y1) и (x2,y2) - координаты двух точек. 
#На вход программе необходимо передать координаты двух точек в виде 
#целых чисел разделенные запятой (см. пример) 

#x1y1 = input("Enter x1, y1: ")
#x2y2 = input("Enter x2, y2: ")

#x1y1=x1y1.split()
#x2y2=x2y2.split()

#d = ((int(x2y2[0]) ^ 2 - int(x1y1[0]) ^ 2) + (int(x2y2[1]) ^ 2 - int(x1y1[1]) ^ 2)) ** 0.5
#print(d)

# И наклон 
#Основываясь на программе «Вычислить длину» необходимо вывести 
#дополнительно синус угла между отрезком и осью X. 
#Синус угла между отрезком и осью X вычисляется по формуле
#где d - длина отрезка 

#x1y1 = input("Enter x1, y1: ")
#x2y2 = input("Enter x2, y2: ")

#x1y1=x1y1.split()
#x2y2=x2y2.split()

#d = ((int(x2y2[0]) ^ 2 - int(x1y1[0]) ^ 2) + (int(x2y2[1]) ^ 2 - int(x1y1[1]) ^ 2)) ** 0.5
#print(d)

#sinus = (int(x2y2[1]) - int(x1y1[1]))/d

#print(sinus)

#Три в ряд
#Имеется геометрическая прогрессия:
#На вход программе подается число n, где 𝑛 ∈ [2; ∞), а на выходе необходимо 
#вывести предыдущий элемент, текущий и следующий из данной прогрессии 
#в виде строк (см. пример). 

#number = int(input("Enter value since 2: "))

#privious_n = 1 / ( 2^ (number-1) )
#curent_n = 1/ ( 2 ^ (number) )
#next_n = 1/ ( 2 ^ (number+1) )

#print("previous n: ", privious_n)
#print("curent n: ", curent_n)
#print("next n: ", next_n)
