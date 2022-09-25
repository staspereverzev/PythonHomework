#Вывести квадраты четных числе из заданной строки

data = input("Введите числа через пробел: ").split(" ")
res = list(map(int, data))
res = list(filter(lambda x: not x%2, res))
res = list(map(lambda x: (x, x**2), res))

print(res)