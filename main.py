from math import sqrt
from triangulo import Triangulo

xA = float(input("Digite o primeiro lado do triangulo 1"))
xB = float(input("Digite o primeiro lado do triangulo 1"))
xC = float(input("Digite o primeiro lado do triangulo 1"))
yA = float(input("Digite o primeiro lado do triangulo 2"))
yB = float(input("Digite o primeiro lado do triangulo 2"))
yC = float(input("Digite o primeiro lado do triangulo 2"))

x = Triangulo(xA, xB, xC)
y = Triangulo(yA, yB, yC)
areax = x.Area
areay = y.Area
print(areax)
print(areay)

if(areax > areay):
    print("Area x é maior")
else:
    print("Area y é maior")