# my_age = int(input("Введите возраст: "))
# print("Вам " + str(my_age) + " лет")

# my_age = int(input("Введите возраст: "))
# print (f"Вам {my_age} лет")

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# if (b/a == a) or (a/b == b):
   # print("True")
#else:
   # print("False")

# my_list = [8, 'r', 7, True]
# my_list.append('END!')
# my_list.pop(-1) #Удаляет эл. с индексом
# my_list[1] = 'Hellow World'
# print(my_list)

#for i in range(1, 10, 2):
#    print(i, end=" ")

# 1. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#    
#    Примеры:
#    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

# amount_of_numbers = 5
# number_list = []

# for i in range(amount_of_numbers):
#     number_list.append(int(input("Введите число: ")))

# max_number = number_list[0]

# for number in range(1, amount_of_numbers):
    
#     if max_number < number_list[number]:
#         max_number = number_list[number]

# print(max_number)


#2. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#    
#    *Примеры:* 
#    
#    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input("ВВедите число N: "))
# for i in range(-n, n + 1):
#     print(i, end = ' ')

# print(list(range(-n, n + 1)))


   
# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#    
#    *Примеры:*
#    
#    - 6,78 -> 7
#    - 5 -> нет
#    - 0,34 -> 3
   

# x = float(input())
# print(int(x * 10) % 10)

# x = input()
# print(x.split('.')[1][0])



# 4. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30).

# a = int(input('Введите число: '))
# if ((a % 5 == 0) and (a % 10 == 0)) or ((a % 15 == 0) and (a % 30 != 0)):
#     print("Yes")
# else:
#     print("No")


day_of_week = int(input("Проверь,является ли день выходным \nВведите номер дня: "))
def check_day(num_day):
    match num_day:
        case 1 :
            print("Нет")
        case 2 :
            print("Нет")
        case 3 :
            print("Нет")
        case 4 :
            print("Нет")
        case 5 :
            print("Нет")
        case 6 :
            print("Да")
        case 7 :
            print("Да")
        case default :
            print("Неверный номер дня")    

    
check_day(day_of_week)

# if day in range(1,5):
#     print("нет")
# else:
#     print("да")

