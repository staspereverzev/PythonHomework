# Lambda

# def calc(op, a, b):
#     print(op(a,b))

# calc(lambda x,y: x+y, 4, 5)
 
# List Comprehension

# list = [i for i in range(0,101)]
# print(list)

# list = [i for i in range(0,101) if i%2 ==0]
# print(list)


# def select(f,col):
#     return [f(x) for x in col] # формируем новый список и его возвращает

# def where(f,col):
#     return [x for x in col if f(x)] #  возвращает список если выполняется условие



data = '1 2 3 5 8 15 23 38'.split()

# res  = select(int, data) # из data формирует список int
res = map(int, data)
print(res)
# res = where(lambda x: not x%2, res) #формирует список только четных чисел
res = list(filter(lambda x: not x%2, res))
print(res)
# res = select(lambda x:(x, x**2), res) #формирует кортеж из числа и квадрата
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Перевод строки в числа
# data = list(map(int,input().split))
# print(data)


