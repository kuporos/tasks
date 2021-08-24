from math import sqrt

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

p = (a+b+c)/2
print (sqrt (p*(p-a)*(p-b)*(p-c)))