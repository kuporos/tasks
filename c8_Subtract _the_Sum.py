
listqewrfg=["0-100"]

# n=324
# if n<100:
#     string=list(str(n))
#     n = n- sum(int (item) for item in string)

def count_numbers(n):
    string = list(str(n))
    n = n - sum(int(item) for item in string)
    return n

def compare(n):
    a=0
    if n<=100:
        return n
    else:
        n = count_numbers(n)
        compare(n)
    return a

print(compare(200))