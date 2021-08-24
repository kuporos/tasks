from math import pow

a = float(input("a: "))
b = float(input("b: "))
operation = (input("operation: "))

try:
    if operation == "+":
        print (type(a+b))
    elif operation == "-":
        print (a-b)
    elif operation == "/":
        print (a/b)
    elif operation == "*":
        print (a*b)
    elif operation == "mod":
        print (a%b)
    elif operation == "pow":
        print(pow(a, b))
    elif operation == "div":
        print(a // b)
except ZeroDivisionError:
    print("Деление на 0!")