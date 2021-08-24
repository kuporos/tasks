shape = input()
square = 0
from math import sqrt
if shape=="треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p=1/2*(a+b+c)
    square = 2*((sqrt(p*(p-a)*(p-b)*(p-c)))/a)

elif shape == "прямоугольник":
    a = int(input())
    b = int(input())
    square=a*b
elif shape == "круг":
    a = int(input())
    square=3.14*(a**2)
print(square)
