day = int(input("Введите день: "))

if day in range(1, 6):
    print("Нет")
elif day in range(6, 8):
    print("Да")
elif day>7 or day<0:
     print("Такого дня нет")
