#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний
user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(int, user_string))

print([(numbers[i]*numbers[-(i+1)]) for i in range(0,round(len(numbers)/2))])