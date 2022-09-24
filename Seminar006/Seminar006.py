# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;
        
# expression = input('Что вычислить?')
# print(eval(expression))

# for i in user_str:
#     if i in '/*':
#         index = user_str.find(i)
#         for k in range(len(user_str[: index])):
#             if user_str[: index][ -k -1] in '+-/*':
#                 index_2 = user_str.find(user_str[: index][ -k -1])
#                 a = user_str[index_2 + 1 : index]

#         for k in range(len(user_str[index + 1:])):
#             if (user_str[index + 1:][k] in '+-/*') and k != len(user_str[index + 1:]) - 1:
#                 index_2 = user_str.find(user_str[index + 1:][k])
#                 b = user_str[index + 1: index_2]
# print(a, b)

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_string = input("Введите елементы через пробел : ").split()
# i = 0
# while (i < len(my_string)):
#     j = i + 1
#     countt = 0
#     while j < len(my_string):
#         if my_string[i] == my_string[j]:
#             my_string.pop(j)
#             countt +=1
#             j = i
#         j += 1
#     if countt != 0 :
#         my_string.pop(i)
#         i = -1
#     i += 1
# print(my_string)

my_list = [1, 1, 2, 3, 4, 4, 5]

print(tuple(filter(lambda num: my_list.count(num) == 1, my_list)))

