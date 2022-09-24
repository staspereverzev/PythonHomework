# 1.Кортежи

# a = (4,5)
# a = (4,)

# my_list = [123, 123]
# my_list = tuple(my_list)
# print(my_list)

# 2. Множество

# my_list = [1,1,3,4,5]
# my_list = set(my_list)
# # my_list = {'gr','ddf', 'sd'}
# print(my_list)

# 3. Словарь

# my_dict = {
#     47: 'Диван',
#     85: 'Кресло'
# }

# print(my_dict[47])

#4. Функции

# import math
# # num_1 = 2
# # num_2 = 3

# def my_func(num_1: int = 1, num_2: int = 2) -> int:
#     return num_1**num_2

# res = my_func()
# print(res)

# 4. Файлы

# f = open('text.txt', 'w')
# f.write('Hello')
# f.close("text")

with open('text.txt', 'w') as f:
    f.write('new')