

numbers = [1,2,3,4,5,6,7]
print([(numbers[i]*numbers[-(i+1)]) for i in range(0,round(len(numbers)/2))])