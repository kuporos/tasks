programmer=int(input())
# от 0 до 1000
# 0,5-20, 25-30, 100 программистов (0, 5-9)
# 1, 21, 31 программист (1)
# 2-4, 22-24, 32-34 программиста (2-4)
#



if programmer>=0 and programmer<=1000:
    if (int(str(programmer)[-1]))==1:
        print (programmer , "программист")
    elif ((int((str(programmer)[-1]))>=2) and ((int(str(programmer)[-1]))<=4)):
        print(programmer, "программиста")
    else: print (programmer, "программистов")


