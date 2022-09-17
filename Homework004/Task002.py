# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def Mnoj(n):
    list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(n)
        print(list)

n = int(input("Введите число: "))
Mnoj(n)