# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

# N = 2021
# i = random.randint(1, 2)

# while N > 28:
#     if i == 1:
#         N = N - int(input(f"Ходит игрок {i}: "))
#         print(f"Осталось конфет: {N}")
#         if N>28:
#             N = N - int(input(f"Ходит игрок {i+1}: "))
#             print(f"Осталось конфет: {N}")
#     else:
#         N = N - int(input(f"Ходит игрок {i}: "))
#         print(f"Осталось конфет: {N}")
#         if N>28:
#             N = N - int(input(f"Ходит игрок {i-1}: "))
#             print(f"Осталось конфет: {N}")
# else:
#     print(f"Победил игрок {i}")

# С ботом

N = 2021
i = random.randint(1, 2)

# while N > 28:
#     if i == 1:
#         N = N - int(input(f"Ходит игрок: "))
#         print(f"Осталось конфет: {N}")
#         i = 2
#         if N>28:
#             print("Ходит компьютер")
#             N = N - random.randint(1,28)
#             print(f"Осталось конфет: {N}")
#     else:
#         print("Ходит компьютер")
#         N - random.randint(1,28)
#         print(f"Осталось конфет: {N}")
#         i = 1
#         if N>28:
#             N = N - int(input(f"Ходит игрок: "))
#             print(f"Осталось конфет: {N}")
# else:
#     if i == 1:
#         print(f"Победил игрок")
#     else:
#         print("Победил компьютер")

while N > 28:
    if i == 1:
        N = N - int(input(f"Ходит игрок: "))
        print(f"Осталось конфет: {N}")
        i = 2
        if N<28:
            print("Победил компьютер")
            
    else:
        x = random.randint(1,28)
        print(f"Ходит компьютер: {x}")
        N = N - x
        print(f"Осталось конфет: {N}")
        i = 1
        if N<28:
            print("Победил игрок")
    