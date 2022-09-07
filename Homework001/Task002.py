# x=1
# y=1
# z=1


for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print ("Если x = ", x, "и y = ", y, "и z = ", z, "¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = ", not(x or y or z) == ((not x) and (not y) and (not z)))
