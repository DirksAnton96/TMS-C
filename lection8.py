#Напишите код, который принимает список чисел и возвращает новый список, 
#содержащий только четные числа из исходного списка. Используйте функцию 
#filter и лямбда-выражение.

#numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#numbers_2 = list(filter(lambda x: x % 2 == 0, numbers))

#print(numbers_2)

#Напишите код, который принимает список кортежей вида (имя, возраст) и 
#возвращает новый список, отсортированный по возрастанию возраста. 
#Используйте функцию sorted и ключ сортировки.

#list_tupple = [("Anton",27),("Ilya",26),("Gleb",30)]

#list_new = list(sorted(list_tupple,key=lambda x: x[1]))

#print(list_new)

#Напишите код, который принимает список строк и возвращает новый список, 
#содержащий только те строки, которые начинаются с гласной буквы. (Да да, 
#снова эти гласные) Используйте функцию filter и множество.

#list_stroka = ("Антон", "Илья", "Глеб", "Пётр")

#vowels = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

#list_new = list(filter(lambda x: x[0].lower() in vowels,list_stroka))

#print(list_new)


#Напишите код, который принимает список чисел и возвращает новый список, 
#содержащий квадраты этих чисел. Используйте функцию map и lambda.

#numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#numbers_2 = list(map(lambda x: x ** 2,numbers))

#print(numbers_2)


#Напишите код, который принимает список слов и возвращает новый список, 
#отсортированный по убыванию длины слов. Используйте функцию sorted и 
#обратный порядок сортировки

#list_stroka = ("Антон", "Илья", "привет", "арифметика", "функциональность")

#list_new = list(sorted(list_stroka,key=len))

#print(list_new)

#Напишите код, который принимает строку и возвращает список, содержащий 
#только те буквы, которые встречаются в слове “python”. Используйте функцию 
#filter и оператор in.

#l_sets = {'p','y','t','h','o','n'}

#stroka = "Hi i am a programmist in python. what about you?"

#list_new = list(filter(lambda x: x in l_sets,stroka.lower()))

#print(list_new)

#Напишите код, который принимает список чисел и возвращает новый список, 
#содержащий эти же числа, умноженные на 10. Используйте функцию.

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# numbers_list = list(map(lambda x: x * 10, numbers))

# print(numbers_list)

#Напишите код, который принимает список слов и возвращает новый список, 
#отсортированный по алфавиту. Используйте функцию sorted.

# list_stroka = ("Антон", "Илья", "привет", "арифметика", "функциональность")

# list_n_s = list(sorted(list_stroka,key= lambda x: x[0].lower()))

# print(list_n_s)

#Напишите функцию, которая принимает список строк и возвращает новый 
#список, содержащий только те строки, которые являются палиндромами. 
#Палиндром — это слово, которое читается одинаково слева направо и справа 
#налево. Используйте функцию filter и сравнение строк.

# list_stroka = ("Антон", "Илья", "привет", "арифметика", "функциональность", "дед", "мам", "казак")

# list_n_s = list(filter(lambda x: x == x[::-1], list_stroka))

# print(list_n_s)

#Напишите код, который принимает список слов и возвращает новый список, 
#отсортированный по возрастанию количества гласных букв в словах. 
#Используйте функцию sorted и ключ сортировки.
#Для подсчета гласных букв 
#используем встроенную функцию sum

# list_stroka = ["привет", "арифметика", "функциональность", "дед", "мам", "казак"]

# list_n_s = list(sorted(list_stroka,key=lambda x: sum(c in 'аеиоуыэюя' for c in x)))

# print(list_n_s)


#Напишите код, который принимает список строк и возвращает новый список, 
#содержащий эти же строки в верхнем регистре. Используйте функцию map и 
#встроенный метод строк upper.

# list_stroka = ("Антон", "Илья", "Глеб", "Петр")

# list_n_s = list(map(lambda x: x.upper(),list_stroka))

# print(list_n_s)

#Напишите код, который принимает список строк и возвращает новый список, 
#содержащий эти же строки с добавленным префиксом “Hello”. Используйте 
#функцию map и конкатенацию строк.

# list_stroka = ("Антон", "Илья", "Глеб", "Петр")

# list_n_s = list(map(lambda x: "Hello " + x +"!",list_stroka))

# print(list_n_s)

#Напишите код, который принимает список слов и возвращает новый список, 
#отсортированный по возрастанию количества букв “a” в словах. Используйте 
#функцию sorted и ключ сортировки

# list_stroka = ["привет", "арифметика", "функциональность", "дед", "мам", "казака"]

# list_n_s = list(sorted(list_stroka,key=lambda x: sum(c in 'а' for c in x)))

# print(list_n_s)

#Напишите код, который принимает список слов и возвращает новый список, 
#отсортированный по возрастанию количества уникальных букв в словах. 
#Используйте функцию sorted и ключ сортировки.

# list_stroka = ["привет", "арифметика", "функциональность", "дед", "мам", "казак"]

# list_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
#     'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
#      'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# list_n_s = list(sorted(list_stroka,key=lambda x: sum(c in list_letters for c in x)))

# print(list_n_s)

#Напишите декоратор retry_five, который повторяет вызов декорируемой 
#функции 5 раз

# def counter(func):
#     count = 0
#     while count < 5:
#         def wrapper(*args,**kwargs):
#             nonlocal count
#             count += 1
#             print(f"Функция была вызвана {count} раз(а)")
#             func(*args,**kwargs)
#             func(*args,**kwargs)
#             func(*args,**kwargs)
#             func(*args,**kwargs)
#             func(*args,**kwargs)
#         return wrapper
#     return count



# def counter(func):
    
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         return func(*args, **kwargs)
    
#     wrapper.count = 0
#     return wrapper

# @counter
# def f():
#     print("Hello")


# f()
# f()
# f()

# print(f.count)

# import time


# def count_time(func):
#     def wrapper(*wrapper_args, **wrapper_kwargs):
#         time_start = time.perf_counter_ns()  # Сколько сейчас времени

#         res = func(*wrapper_args, **wrapper_kwargs)

#         time_end = time.perf_counter_ns()  # Сколько сейчас времени
#         print("Функция выполнялась", time_end - time_start, "нс")
#         return res

#     return wrapper

# @count_time
# def get_positive_numbers(numbers: list[int | float]) -> list[int | float]:
#     new_numbers = []
#     for number in numbers:
#         if number > 0:
#             new_numbers.append(number)
#     return new_numbers


# @count_time
# def get_zero_numbers(numbers: list[int | float]) -> list[int | float]:
#     new_numbers = []
#     for number in numbers:
#         if number == 0:
#             new_numbers.append(number)
#     return new_numbers


# numbers1 = [1, 23, 14.43, -234, 0, -2.23, 4, 1]

# print(get_positive_numbers(numbers1))




############################## Рабочий вариант  ##########################################################
# def counter(func):
#     def wrapper(*args,**kwargs):
#         count = 0
#         result = 0
#         while count < 5:
#             count += 1
#             print(f"Функция была вызвана {count} раз(а)")
#             result = result + func(*args,**kwargs)
#         return result
#     return wrapper

# @counter
# def add_numbers(x, y):
#     return x + y


# res = add_numbers(2,3)
# print("result func after five reguests: ", res)
##############################################################################################################