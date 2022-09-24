import random

n = int(input("Введите число N: "))
list = []

# for i in range(0, n*2):
#      list.append(random.randint(-n, n+1))
# print(list)

x = (input("Введите позиции элементов: "))
p1 = int(x[0])
p2 = int(x[2])

# print(list[p1] * list[p2])

# n=5
# p1 = 2
# p2 = 5

list = [(random.randint(-n, n+1)) for i in range(0, n*2)]
print(list)
res = lambda x,y: x*y
print(res(list[p1],list[p2]))