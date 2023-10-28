# Напишите функцию root(x), которая возвращает квадрат своего аргумента.
#def root(x):
#    return x * x

#number = int(input("Enter the value: "))
#result = root(number)
#print(result)

# Напишите функцию is_even(n), которая проверяет, является ли число 
# четным или нечетным. Функция должна возвращать True, если число четное, 
# и False, если число нечетное.

#def is_even(n):
#    return n % 2 == 0

#number = int(input("Enter the value: "))
#result = is_even(number)
#print(result)

#Напишите функцию factorial(n), которая вычисляет факториал своего 
#аргумента. Факториал числа n — это произведение всех натуральных чисел от 
#1 до n. Например, factorial(4) = 4×3×2×1 = 24. 
#Функция должна возвращать факториал числа или -1, если число отрицательное.

#def factorial(n):
#    i = 0
#    fact = 0
#    while i < n + 1:
#        if i == 0:
#            fact = 1
#        else:
#            fact = fact * i
#        i += 1
#    return fact

#def factorial(n):
#    if n == 1:
#        return 1
#    return factorial(n - 1) * n

#number = int(input("Enter the value: "))
#result = factorial(number)
#print(result)

# Напишите функцию reverse(s), которая принимает строку s и возвращает 
# ее в обратном порядке. Например, reverse("hello") должна вернуть "olleh".

#def reverse(s):
#    i = len(s)
#    s_n = ""
#    while i > 0:
#        s_n = s_n + s[i - 1]
#        i -= 1
#    return s_n

#def reverse(s):
#    return s[::-1]


#stroka = input("Enter the string: ")
#result = reverse(stroka)
#print(result)

# Напишите функцию fibonacci(n), которая возвращает n-ый член 
# последовательности Фибоначчи. Первые два числа равны 1.  

#def fibonacci(n):
#    if n in (1, 2):
#        return 1
#    return fibonacci(n - 1) + fibonacci(n - 2)

#number = int(input("Enter the value: "))
#result = fibonacci(number)
#print(result)

#Напишите функцию count_vowels(s), которая подсчитывает количество 
#гласных букв в строке s. Гласные буквы — это а, е, ё, и, о, у, ы, э, ю, я.
#Например, count_vowels("привет") должна вернуть 2.

#def count_vowels(s):
#    count = 0
#    for letter in s:
#        if letter in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
#            count += 1
#    
#    return count

#stroka = input("Enter the string: ")
#result = count_vowels(stroka)
#print(result)

#Напишите функцию is_palindrome(s), которая проверяет, является ли 
#строка s палиндромом. 
#Палиндром — это слово или фраза, которая читается одинаково слева направо 
#и справа налево. Функция должна возвращать True, если строка палиндром, 
#и False, если нет.
#Например, is_palindrome("топот") должна вернуть True, а 
#is_palindrome("привет") должна вернуть False.

#def is_palindrome(s):
#    return s[::1] == s[::-1]

#stroka = input("Enter the string: ")
#result = is_palindrome(stroka)
#print(result)

#Напишите функцию power(x, n), которая возводит число x в степень n.
#Например, power(2, 3) должна вернуть 23 = 8

#def power(x, n):
#    return x ** n

#number_x = int(input("Enter the value x: "))
#number_n = int(input("Enter the value n: "))
#result = power(number_x, number_n)
#print(result)


#Напишите функцию is_anagram(s1, s2), которая проверяет, являются ли 
#две строки s1 и s2 анаграммами. 
#Анаграмма — это слово, составленное из перестановки букв другого слова. 
#Функция должна возвращать True, если строки анаграммы, и False, если 
#нет. Например, is_anagram("кот", "ток") должна вернуть True, а 
#is_anagram("кот", "собака") должна вернуть False.

#def is_anagram(s1, s2):
#    return sorted(s1) == sorted(s2)

#stroka_s1 = input("Enter the string: ")
#stroka_s2 = input("Enter the string: ")
#result = is_anagram(stroka_s1, stroka_s2)
#print(result)

#Напишите функцию is_pangram(s), которая проверяет, является ли строка s панграммой или нет. 
#Панграмма — это строка, которая содержит все буквы алфавита хотя бы один 
#раз. Функция должна возвращать True, если строка панграмма, и False, если нет. 
#Например, is_pangram("Аэрофотосъёмка ландшафта уже выявила 
#земли богачей и процветающих крестьян.") должна вернуть True, 
#а is_pangram("Привет, мир") должна вернуть False

#def is_pangram(s):
#    list_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
#     'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
#      'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#    for letter in list_letters:
#        if letter not in s:
#            return False
#    return True

#stroka_s1 = input("Enter the string: ")
#result = is_pangram(stroka_s1)

#print(result)

#Напишите функцию is_anagram(s1, s2), которая проверяет, являются ли 
#две строки s1 и s2 анаграммами. 
#Анаграмма — это слово, составленное из перестановки букв другого слова. 
#Функция должна возвращать True, если строки анаграммы, и False, если 
#нет. Например, is_anagram("кот", "ток") должна вернуть True, а 
#is_anagram("кот", "собака") должна вернуть False.

# def is_anagram(s1, s2):
#    return set(s1.lower()) == set(s2.lower())  and len(s1) == len(s2)

# def is_anagram(s1, s2):
#     set1 = set(s1.lower())
#     set2 = set(s2.lower())
#     for letter in set1:
#         if s1.count(letter) != s2.count(letter):
#             return False
#     return True

# stroka_s1 = input("Enter the string: ")
# stroka_s2 = input("Enter the string: ")
# result = is_anagram(stroka_s1, stroka_s2)
# print(result)

# Напишите функцию fibonacci(n), которая возвращает n-ый член 
# последовательности Фибоначчи. Первые два числа равны 1. 

# def fibonacci(n):
#     F_n = [0]
#     f0 = 0
#     f1 = 1
#     for i in range(n):
#         f0, f1 = f1, f0 +f1
#         F_n.append(f0)
#     return F_n


# number = int(input("Enter the value: "))
# result = fibonacci(number)
# print(result)