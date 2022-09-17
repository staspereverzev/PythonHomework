def Numb_from_Polynomial(a):
    line = a
    l = len(line)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = line[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = line[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    
    integ.pop(1)
    print(integ)
    return(integ)


with open ('Task005_1.txt', 'w+') as f1:
    f1.write("7x**2 + 5*x + 5")
    
with open ('Task005_2.txt', 'w') as f2:
    f2.write("5x**2 + 2*x + 15")

with open ('Task005_1.txt', 'r') as f1:  
    line1 = f1.readlines()
    print(line1)

with open ('Task005_2.txt', 'r') as f2:
    line2 = f2.readlines()
    print(line2)

line1 = str(line1)
line2 = str(line2)

line1 = Numb_from_Polynomial(line1)
line2 = Numb_from_Polynomial(line2)


print()

# num_list1 = []
# num_list2 = []

# for i in range(0,len(line1)):
#     if '0' <= line1[i] <= '9':
#         a = int(line1[i])
#         b = int(line2[i])
#         num_list1.append(a)
#         num_list2.append(b)

# print()

print(f"{line1[0]+line2[0]}*x^{2}+{line1[1]+line2[1]}*x+{line1[2]+line2[2]}")




