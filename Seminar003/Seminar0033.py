# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time

# def my_random(minn, maxx):
#     time.sleep(0.3) # приостанавливаем программу на 0.3 сек
#     return int((time.time() % 1  * (maxx - minn)) + minn)
# #                     0.9                  7           1

# for i in range(10):
#     print(my_random(1, 9))


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']


list = ['efg23', '79234gefg', 'sdgs', 'g53', '23']
x = '23'


def Entry(list, x):
    count = 0
    for i in range(0, len(list)):
        if x in list[i]:
            count += 1
    print(count)

Entry(list, x)



# 3. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# list = ["qwe", "asd", "qwe", "zxc", "qwe", "ertqwe"]
# x = 'qwe'



# def Entry(list, x):
#     count = 0
#     for i in range(0, len(list)):
#         if x in list[i]:
#             count += 1
#             if count == 2:
#                 print(i)
                
# Entry(list, x)

# def findstr(my_list: list, find_string: str) -> int:
#     count = 0
#     for i in range(len(my_list)):
#         if find_string == my_list[i]:
#             count += 1
#             if count == 2:
#                 return i
#     return -1

# list_find = ["йцу", "фыв","йцу", "ячс", "цук", "йцукен"]
# find_string = "йцу"

# print(findstr(list_find, find_string))
