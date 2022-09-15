number_fib1 = 0
number_fib2 = 1
 
n = int(input("Номер элемента ряда Фибоначчи: "))
index = 0
numbers = []

if n == 1: 
    numbers = [0, 1]
elif n == 0:
    numbers = [0]

if n >= 2:
    numbers = [-1,0,1]
    k = 1
    while index < n - 2:
        sum_fib = number_fib1 + number_fib2
        number_fib1 = number_fib2 
        number_fib2 = sum_fib
        index += 1
        numbers.append(number_fib2)
        numbers.insert(0,number_fib2*(k))
        k *= -1

print(numbers)
