# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5


# with open ('Seminar005.txt', 'w') as f1:
#     f1.write('1 2 3 5')

# with open ('Seminar005.txt', 'r') as f1:  
#     line1 =list(f1.read().split())
#     print(line1)


# for i in range(1, len(line1)):
#     if int(line1[i])-1 != int(line1[i -1]):
#         print(int(line1[i])-1)

# path_1 = 'task1.txt'

# def read_file(path):
#     out_string = ''
#     res_txt = open(path, 'r')
#     out_string = res_txt.read()
#     res_txt.close()
#     out_list = out_string.split()

#     for i in range(0, len(out_list)):
#         out_list[i] = int(out_list[i])

#     return out_list

# def find_number(input_list: list):
    
#     for i in range(1, len(input_list)):
#         if input_list[i] - 1 != input_list[i - 1]:
#             number = input_list[i - 1] + 1
#             break
#     return number


# print(f'Не хватает числа {find_number(read_file(path_1))}')

# Лучший вариатн
# my_list = [1,2,4,5]
# res = [(my_list[i] - 1) for i in range(1, len(my_list)) if (my_list[i]-1) != my_list[i-1]]
# print(res)

# 2. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# Вариант

# num = [1, 5, 2, 3, 4, 6, 1, 7]

# def nextmax(listt):    
#     max = listt[0]
#     res = [listt[0]]
#     for i in range(len(listt)):
#         if listt[i] > max:
#             max = listt[i]
#             res.append(max)
        
#     return res

# Вариант
    

# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = [list[0]]
# max = list[0]
# for i in list:
#     if i > max:
#         new_list.append(i)
#         max = i
# print(new_list)

# Вариант

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# res = [my_list[0]]
# [res.append(item) for item in my_list if item > res[-1]]
# print(res)


# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавуабв!'
# 'Мы очень любим Питон!'

print (' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))


my_str = 'Мы неабв очень любим Питон иабв Джавуабв!'.split()
print(' '.join([word for word in my_str if 'абв' not in word]))

