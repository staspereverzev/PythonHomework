n = input("ВВедите вещественное число: ")

x = n.split(".")
a = int(x[0])
b = int(x[1])

multiplay = 1

while (a != 0): 
    multiplay = multiplay * (a % 10)
    a = a // 10

while (b != 0): 
    multiplay = multiplay * (b % 10)
    b = b // 10

print("Произведение цифр числа = ", multiplay)

