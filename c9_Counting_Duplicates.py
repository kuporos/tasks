# Count the number of Duplicates
#
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
#
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

text = "aA1B1b"
list2=[]
text2 = list(set(text.lower()))

for a in range(len(text2)):
    count = text.lower().count(text2[a])
    if count>=2:
        list2.append(list(set(text))[a])
print (len(list2))

##########################################################################

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

##########################################################################

from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)