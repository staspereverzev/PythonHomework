arr = [['.','.','.'], ['.','.','.'], ['.','.','.']]


for i in range(len(arr)):
    for j in range(len(arr[i])):  
        print(arr[i][j], end=' ')
    print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        while arr[i][j] == '.':
            print("Ходит первый игрок")
            i1 = int(input('Введите куда постаивть '))
            j1 = int(input('Введите куда постаивть '))
            arr[i1][j1] = 'X'

            for i in range(len(arr)):
                for j in range(len(arr[i])):  
                    print(arr[i][j], end=' ')
                print()

            print("Ходит второй игрок")
            i2 = int(input('Введите куда постаивть '))
            j2 = int(input('Введите куда постаивть '))
            arr[i2][j2] = 'O'


            for i in range(len(arr)):
                for j in range(len(arr[i])):  
                    print(arr[i][j], end=' ')
                print()



