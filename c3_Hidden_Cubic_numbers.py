###############################################################

s = "&z371 upon 407298a --- dreary, ###100.153 I thought, 9926315strong and weary -127&() 1"


list=[]
list2=[]
number=0

for a in range(len(s)+1):
    try:
        number = f"{number}{int(s[a])}"
    except:
        if number == "00":
            list.append("0")
        if number == "01":
            list.append("1")
        if number != 0:
            if len(number)<3:
                pass
            else:
                n=(len(number))// 3
                if len(number) < 6:
                    list.append(str(number)[1:])
                else:
                    d = 1
                    e = 4
                    for c in range(n):
                        list.append(str(number)[d:e])
                        d+=3
                        e+=3
        number = 0
print (list)


for b in range (len(list)):
    sum_count=0
    for c in range (len(list[b])):
        sum_count=sum_count+int(list[b][c])**3
    if sum_count == int(list[b]):
        list2.append(str(sum_count))


# if len(list2)==0:
#     print('"No numbers!,"' + ' "Unlucky"')
# else:
#     print('"' +s+'", ' + '"'+" ".join(list2) + " Lucky" + '"')

if len(list2)==0:
    print("Unlucky")
else:
    print(" ".join(list2) + " " + " ".join(list2) + ' Lucky')

print('371 407 153 1 932 Lucky')