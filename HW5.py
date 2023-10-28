#Напишите функцию make_sentence, которая принимает один именованный 
#аргумент words, который должен быть списком строк, и возвращает строку, 
#составленную из элементов списка, разделенных пробелами и 
#заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию 
#используется список ["This", "is", "a", "sentence"]. 

#def make_sentence(words: list):
#    sentence = ' '.join(words)
#    return sentence

#stroka = make_sentence(words=["Python", "is", "fun"])
#print(type(stroka)," string at all: ", stroka)

#Напишите функцию sum_of_squares, которая принимает произвольное 
#количество позиционных аргументов, которые должны быть числами, и 
#возвращает сумму их квадратов. Если функции не передано ни одного 
#аргумента, она должна вернуть 0.

#def sum_of_squares(*numbers: int | float):
#    total = 0
#    for number in numbers:
#        total += number * number
#    return total

#print(sum_of_squares())

#Напишите функцию greet, которая принимает два именованных аргумента: 
#name и language. Аргумент name должен быть строкой, а аргумент language
#должен быть одним из трех возможных значений: "en", "ru" или "fr". 
#Функция должна возвращать приветствие на выбранном языке. 
#Если аргумент language не указан, то по умолчанию используется "en". 

#def greet(name: str, language: str = "en"):
#    if language == "en" or language == None:
#        return "Hello" + ' ' + name + "!"
#    elif language == "ru":
#        return "Привет" + ' ' + name + "!"
#    else:
#        return "Bonjour" + ' ' + name + "!"

#stroka = greet("Anton", "ru")
#print(type(stroka)," string at all: ", stroka)

#Напишите функцию print_info, которая принимает произвольное 
#количество именованных аргументов (**kwargs) и выводит их в формате 
#"key: value" по одной паре на строку. Напоминаю, что kwargs в функции 
#будет словарем. Если функции не передано ни одного аргумента, она должна 
#вывести "No info given."

#def print_info(**kwargs):
#    if len(kwargs) == 0:
#        print("No info given.")
#    else: 
#        for key in kwargs:
#           print(f"{key} = {kwargs[key]}")
    
#print_info( name="Anton", age=27, surname="Dirks", email="dirks@example.com")

#Напишите функцию print_table, которая принимает произвольное 
#количество именованных аргументов в виде пар ключ-значение и выводит их 
#в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не 
#передано ни одного аргумента, она должна вывести "No data given.".


#def print_table(**kwargs):
#    if len(kwargs) == 0:
#        print("No info given.")
#    else:
#        stroka_1 = "KEY"
#        stroka_2 = "VALUE"
#        print(f" | {stroka_1:<20} | {stroka_2:<20} | ")
#        for key in kwargs:
#            print(f" | {key:<20} | {kwargs[key]:<20} | ")


#print_table(name="Anton", age=27, surname="Dirks", email="dirks@example.com")

#Напишите функцию calculate, которая принимает произвольное количество 
#позиционных аргументов, которые должны быть числами, и один 
#именованный аргумент operation, который должен быть одним из четырех 
#возможных значений: "+", "-", "*" или "/". 
#Функция должна возвращать результат выполнения указанной операции над 
#всеми числами в порядке их передачи. 
#Если функции не передано ни одного позиционного аргумента, она должна 
#вернуть 0.
#Если аргумент operation не указан, то по умолчанию используется "+".

# def calculate(*numbers: int | float, operation: str = "+"):
#    result = 0
#    count = 0
#    for number in numbers:
#        if operation == "+":
#            result = result + number
#        elif operation == "-":
#            result = result - number
#        elif operation ==  "*":
#            if count == 0:
#                result = 1
#                result = result * number
#                count += 1
#            else:
#                result = result * number
#        else:
#            if count == 0:
#                result = number
#                #result = result / number
#                count += 1
#            else : 
#                result = result / number
#    return result

# print(calculate(1,2,3,4,5,6,7,8,9,10,operation = "/"))

#Напишите функцию print_triangle, которая принимает один именованный 
#аргумент height, который должен быть положительным целым числом, и 
#выводит равнобедренный треугольник из символов "*" с заданной высотой. 
#Если аргумент height не указан, то по умолчанию используется число 5. 

# def print_triangle(height: int = 5):
#    stroka = "*"
#    if height <= 0:
#        print("Type correct value")
#        return None
    
#    i = 1
#    while i < height + 1:
#        if i == 1:
#            print(f"{stroka * (i) }".center(height * 2))
#        else:
#            print(f"{stroka * (i + (i - 1)) }".center(height * 2))
#        i += 1

# number = int(input("Type the number of hieght: "))
# print_triangle(number)

#Напишите функцию create_post, которая создает пост для блога, 
#основываясь на переданных параметрах. Обязательными параметрами 
#являются: заголовок, содержимое и автор. Необязательным параметром 
#является категория. Если она не была передана, то по умолчанию будет 
#текущая значение “general”. Функция должна возвращать словарь поста.

#def create_post(header: str, content: str, author: str, category: str = "general"):
#    post = {
#        "header": header,
#        "content": content,
#        "author": author,
#        "category": category,
#    }
#    return post

#post1 = create_post("test", "Text", "Example","Sport")

#print(post1)


#Напишите функцию create_product, которая создает товар для интернет-магазина, 
#основываясь на переданных параметрах. Обязательными 
#параметрами являются: имя, цена и категория. Необязательным параметром 
#является рейтинг. Если он не был передан параметр, то по умолчанию будет 
#0. Функция должна возвращать словарь товара.

#def create_product(name: str, price: int | float, category: str, like: int = 0 ):
#    product = {
#        "Name":  name,
#        "Price":  price,
#        "Category":  category,
#        "Like":  like,
#    }
#    return product

#product_1 = create_product("Car", 26500.45, "sedan", 10)

#print(product_1)



#Напишите функцию create_student, которая создает словарь студента 
#для учебного заведения, основываясь на переданных параметрах.
#Обязательными параметрами являются: имя, фамилия, отчество и группа. 
#Также дополнительными параметрами могут быть: дата поступления в виде
#строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес. 
#Функция должна возвращать словарь студента только с переданными
#данными, если некоторые данные не были переданы, то их не должно быть 
#в словаре

#def create_student(name: str, surname: str, fathername: str, group: int, **kwargs):
#    student = {
#        "Name": name,
#        "Surname": surname,
#        "Fathername": fathername,
#        "Group": group,
#    }
#    student.update(kwargs)
#   return student

#student_1 = create_student("Anton", "Dirks", "Igorevich", 2)

#student_2 = create_student("Ivan", "Ivanov", "Ivanovich", 3,
#    data_entered = "21.10.2023",
#    sr_ball = 7.5,
#    phone_number = "12345678921"
#)

#print(student_1)
#print("\n")
#print(student_2)