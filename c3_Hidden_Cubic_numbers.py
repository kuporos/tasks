###############################################################

s = "aqdf&0#1xyz!22[153(777.777"

nine="ge"
list=[]
number=0

for a in range(len(s)+1):
    try:
        if int(s[a])/2:
            number=f"{number}{s[a]}"
    except:
        list.append(number)
        number=0
print (list)