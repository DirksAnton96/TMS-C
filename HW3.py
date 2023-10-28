#По середине 
#Написать программу, которая будет принимать на вход строку и выводить её в следующем виде:
#Текст должен располагаться по средине 
#Длина шапки всегда равна 30 символов, если предложение слишком длинное, то обрезать его. 

#stroka = input("Enter the string: ")

#text = f"""
#==================================================
#{stroka.center(30)[:30]}
#==================================================
#"""

#print(text)

#Только +
#Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел 

#number_1 = int(input("Enter value 1: "))
#number_2 = int(input("Enter value 2: "))
#number_3 = int(input("Enter value 3: "))
#sum = 0

#if number_1 > 0:
#    sum = sum + number_1
#if number_2 > 0:
#    sum = sum + number_2
#if number_3 > 0:
#    sum = sum + number_3
#print(sum)

#Високосный год 
#Напишите программу, которая определяет, является ли год с данным номером високосным. 
#Если год является високосным, то выведите «Да», иначе выведите «Нет».

#value_of_year = int(input("Enter the year: "))
#
#if (value_of_year // 4) or (value_of_year % 100 == 0) or (value_of_year % 400 ==0) :
#    print("Leap year: ", value_of_year)
#else:
#    print(value_of_year, " - isn't leap year")



#Ход ладьи 
#На вход программе подаются две клетки шахматной доски в формате «а7» «e3». 
#Значение клетки необходимо считывать за один input. 
#Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. 
#Программа должна вывести «Да», если из первой клетки ходом ладьи можно попасть во вторую, или «Нет» в противном случае.

#coordinates_start = input("Enter value like a7: ")
#coordinates_end = input("Enter value like e3: ")
#
#if (coordinates_end[0]==coordinates_start[0]) or (coordinates_start[1]==coordinates_end[1]):
#    print("Possible  ")
#else:
#    print("Impossible  ")


#1. Напишите программу, которая принимает на вход список чисел и выводит на экран сумму всех элементов списка. 
#Используйте цикл while и переменную-счетчик

#numbers = [1,2,3,4,5,6,7,8,9.10]

#n = len(numbers)
#i = 0
#sum = 0

#while i < n:
#    sum = sum + int(numbers[i])
#    i += 1

#print("sum of list elements: ", sum)


#2. Напишите программу, которая принимает на вход строку и выводит на экран  количество гласных букв в ней. 
#Гласными буквами считаются “а”, “е”, “и”, “о”, “у”, “ы”, “э”, “ю”, “я”. 
#Используйте цикл while. 

#stroka = input("Enter the string: ")

#vowels = ('а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')

#n = len(stroka)

#i = 0

#p = len(vowels)

#k = 0

#vowels_count = 0

#while i < n :
#    while k < p:
#        if stroka[i] == vowels[k]:
#            vowels_count = vowels_count + 1
#        k += 1
#    i += 1
#    k = 0
#print("The number of vowels: ", vowels_count)


#3. Напишите программу, которая принимает на вход список слов и выводит на экран самое длинное слово из списка и его длину. 
#Если таких слов несколько, выведите первое из них. 
#Используйте цикл while и переменные для хранения  максимальной длины и самого длинного слова. 

#stroka = input("Enter the string: ")

#list_stroka = stroka.split()

#i = 0

#max_long_word = list_stroka[0]

#while i < len(list_stroka):
#    if len(max_long_word) < len(list_stroka[i]):
#        max_long_word = list_stroka[i]       
#    i += 1
#print(max_long_word)


#4. Напишите программу, которая принимает на вход список чисел и выводит на экран новый список,
#  в котором все четные числа умножены на 2, а все нечетные  остались без изменений. 
# Используйте цикл while и оператор % для определения четности числа.

#stroka = input("Enter the numbers: ")

#list_numbers = stroka.split()

#print (list_numbers)
#i = 0
#k = 0

#while i < len(list_numbers):
#    if int(list_numbers[i]) % 2 == 0:
#        k = int(list_numbers[i]) * 2
#        list_numbers.pop(i)
#        list_numbers.insert(i, k)
#    i += 1
#print(list_numbers)



#5. Напишите программу, которая принимает на вход список чисел и выводит на экран индекс 
# и значение минимального элемента в списке. 
#Если таких элементов несколько, выведите первый индекс из них. 
#Используйте цикл while и переменные для хранения минимального значения и его индекса. 

#stroka = input("Enter the numbers: ")

#list_numbers = stroka.split()

#i = 0

#min = int(list_numbers[0])

#index = 0

#while i < len(list_numbers):
#    if int(list_numbers[i]) < min:
#        min = int(list_numbers[i])
#        index = i
#    i += 1
#print("Min element: ", min, "Index of this element: ", index)  

#6. Напишите программу, которая принимает на вход строку и выводит на экран 
#новую строку, в которой все слова записаны в обратном порядке. 
#Например, строка “Привет, мир!” должна превратиться в “мир! Привет,”. 
# Используйте цикл while и метод split() для разбиения строки на слова и метод join() для объединения слов в строку

#stroka = input("Enter the string: ")

#list_stroka = stroka.split()

#i = len(list_stroka) - 1

#new_word_list = []

#while i > -1:
#    new_word_list.append(list_stroka[i])
#    i -= 1


#stroka = ' '.join(new_word_list)
#print(stroka)