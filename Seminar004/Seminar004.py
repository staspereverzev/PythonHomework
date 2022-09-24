#1

# user_string = input("Введите строрку из чисел через пробел ").split(" ")

# print(user_string)

# for i in range(0, len(user_string)):
#     user_string[i] = int(user_string[i])

# minn = 0
# maxx = 0
# print(user_string[0])

# for i in range(0,len(user_string)):
#     if user_string[i] > maxx:
#         maxx = user_string[i]
#     if user_string[i] < minn:
#         min = user_string[i]

# print(minn, maxx)

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(int, user_string))
print(max(numbers), min(numbers))



# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
# 1) с помощью математических формул нахождения корней квадратного уравнения 
# 2) с помощью дополнительных библиотек Python

# from math import *

# def square_root(a: int = 0, b: int = 0, c: int = 0) -> list:
#     discriminant = (b ** 2) - (4 * a * c)
#     if discriminant < 0:
#         return []
#     elif discriminant == 0:
#         x = - (b / (2 * a))
#         return [x]

#     x1 = (-b + sqrt(discriminant)) / (2 * a)
#     x2 = (-b - sqrt(discriminant)) / (2 * a)
#     return [x1, x2]
    
# print('Ax² + Bx + C = 0')
# a = int(input('A= '))
# b = int(input('B= '))
# c = int(input('C= '))
# print(square_root(a, b, c))



# 3. Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# 1 вариант

# x = int(input("Введите X"))
# y = int(input("ВВедите Y"))

# if x > y: 
#     greater = x 
# else: 
#     greater = y 
# while(True): 
#     if((greater % x == 0) and(greater % y == 0)): 
#         lcm = greater 
#         break 
#     greater += 1

# print(lcm)

#2 вариант

# import math
# a = int(input("a = "))
# b = int(input("b = "))
# print(math.lcm(a, b))

#3 вариант

# print("Введите число")
# a = int (input())
# print("Введите второе число")
# b = int (input())
# нод = 0
# нок = a*b
# while (a!=b):
#     if (b>a):
#         b = b-a
#     else:
#         a = a-b
# else: нод = a
# нок = нок/нод
# print(нок)


# ДЗ
# Вычислить число c заданной точностью d Пример: при d = 0.001, π = 3.141.d=0.001,π=3.141.

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# Вычислить число c заданной точностью d Пример: при d = 0.001, π = 3.141.d=0.001,π=3.141.10^{-1} ≤ d ≤10^{-10}10 −1 ≤d≤10 −10 
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
