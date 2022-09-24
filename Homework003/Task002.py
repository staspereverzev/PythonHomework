# user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
# numbers = list(map(int, user_string))

# k = 0
# for i in range(0, round(len(numbers)/2)):
#     print(numbers[i]*numbers[len(numbers)-1-k])
#     k +=1

numbers = [1,2,3,4,5,6,7]
# k = 1
# # print([(numbers[i]*numbers[len(numbers)-1-k]) for i in range(0,round(len(numbers)/2),)])
# x = 1
# y = 2

# def mult(op,x,y):
#     print(op(x,y))
#     k+=1

# f = lambda: x,y,x*y
# mult(f,4,5)

# k = 0
# tables = [lambda x = x: x*10 for x in numbers]
# for table in tables:
#     print(table())

# f = lambda: x,y,x*y

# def calc(op,a,b):
#     print(op(a,b))

# # calc(mylt,4,5)

# f = lambda q,w: q*w
# calc (f,numbers[1],numbers[5])

print([(numbers[i]*numbers[-(i+1)]) for i in range(0,round(len(numbers)/2))])
# for i in range(len(numbers)):
#     print(numbers[-1])
