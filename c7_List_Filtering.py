# List Filtering

# In this kata you will create a function that takes a list of non-negative integers and strings and
# returns a new list with the strings filtered out.
# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


list1=[1,'a','b',0,15]
list2=[]
for a in range(len(list1)):
    try:
        if (list1[a]/2) or (list1[a]==0):
            list2.append(list1[a])
    except: pass
print (list2)

##############################################################

list1=[1,'a','b',0,15]
list2=[]

for a in list1:
    try:
        if a>=0:
            list2.append(a)
    except TypeError: pass
print(list2)

##############################################################

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]