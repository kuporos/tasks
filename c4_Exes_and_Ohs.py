# №4 Exes and Ohs
# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    o=0
    x=0
    for a in s:
        if a.lower()=="o":
            o+=1
        elif a.lower()=="x":
            x+=1
    if (o==x) or (o==0 and x==0):
        return True
    else: return False