# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141

from cmath import pi
import math
math.pi

x = int(input("Введите количество знаков после запятой: "))
pi = round(pi, x)
print (pi)