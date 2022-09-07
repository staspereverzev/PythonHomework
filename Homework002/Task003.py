k = int(input("Введите число: "))
i=1
for i in range(1,k+1):
    print(f"{i}: {(1+1/i)**i}")
    i+=1