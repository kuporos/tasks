min = int(input("min: "))
max = int(input("max: "))
ann = int(input("you time of sleep: "))

if ann<min:
    print ("Недосып")
elif ann>max:
    print("Пересып")
else:
    print("Это нормально")