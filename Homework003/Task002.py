user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(int, user_string))

k = 0
for i in range(0, round(len(numbers)/2)):
    print(numbers[i]*numbers[len(numbers)-1-k])
    k +=1
