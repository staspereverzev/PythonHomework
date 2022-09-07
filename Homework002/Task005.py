import random

list = []
n = int(input("Введите размер списка: "))

for i in range(0, n+1):
     list.append(random.randint(0, 101))
print(list)

for i in range(0,len(list)):
    t = random.randint(0, n)
    temp = list[i]
    list[i] = list[t]
    list[t] = temp
print(list)
