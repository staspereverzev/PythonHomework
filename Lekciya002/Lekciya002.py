numbers = [1,2,3,4,5]

k = -1
for i in numbers:
    print(numbers[i-1] + numbers[k])
    k -= 1