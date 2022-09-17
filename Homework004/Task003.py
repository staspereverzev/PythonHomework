# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

#1 вариакт
# def get_unique_numbers(numbers):
#     unique = []

#     for i in numbers:
#         if i in unique:
#             continue
#         else:
#             unique.append(i)
#     return unique

# user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
# numbers = list(map(int, user_string))
# print(get_unique_numbers(numbers))

#2 вариант
user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(int, user_string))
numbers = set(numbers)
print(numbers)