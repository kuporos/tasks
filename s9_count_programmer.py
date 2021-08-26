
# от 0 до 1000
# 0,5-20, 25-30, 100 программистов (0, 5-9)
# 1, 21, 31 программист (1)
# 2-4, 22-24, 32-34 программиста (2-4)
#

programmer=int(input())
len_programmer = int(str(programmer)[-1])

def count(len_programmer):
    if (len_programmer == 0 or ((len_programmer >= 5) and (len_programmer <= 9)) or (
                programmer >= 11 and programmer <= 20)):
        return f"{programmer} программистов"

    elif (len_programmer) == 1:
        return f"{programmer} программист"
    elif ((len_programmer >= 2) and (len_programmer <= 4)):
        return f"{programmer} программиста"

def first_count(programmer):
    if programmer>=0 and programmer<=1000:
        if len(str(programmer))==3:
            if (((int((str(programmer)[1:3]))) >= 11) and ((int((str(programmer)[1:3]))) <= 14)):
                return f"{programmer} программистов"
            else:
                return count(len_programmer)
        else: return count(len_programmer)

print(first_count(programmer))

