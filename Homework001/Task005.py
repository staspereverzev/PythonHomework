xA=int(input("Введите координату X точки A: "))
yA=int(input("Введите координату Y точки A: "))
xB=int(input("Введите координату X точки B: "))
yB=int(input("Введите координату Y точки B: "))

import math
distance = math.sqrt( ((xB-xA)**2)+((yB-yA)**2) )
distance = float('{:.3f}'.format(distance))
print(distance)