user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(float, user_string))

print(numbers)

minn = round(numbers[0]%1,5)
maxx = round(numbers[0]%1,5)

for i in range (0,len(numbers)):
    temp = round(numbers[i]%1,5)
    print (round(numbers[i]%1,5))
    if temp > maxx:
        maxx = temp
    elif temp < minn:
        minn = temp

print(maxx, ' - ' , minn, ' = ', maxx - minn)
