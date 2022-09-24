# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

import random

n = int(input("Введите число N: "))
list = []

x = (input("Введите позиции элементов через пробел: "))
p1 = int(x[0])
p2 = int(x[2])

list = [(random.randint(-n, n+1)) for i in range(0, n*2)]
print(list)
res = lambda x,y: x*y
print(res(list[p1],list[p2]))