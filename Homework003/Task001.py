user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(int, user_string))

def SumSecond(numbers):
    sum = 0
    for i in range (0, len(numbers),2):
        sum = sum + numbers[i]

    print(sum)

SumSecond(numbers)