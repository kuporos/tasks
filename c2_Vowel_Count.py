# №2 Vowel Count

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.


def getCount(sentence):
    vowels = ["a", "e", "i", "u", "o"]
    count=0
    for a in vowels:
        for b in list(sentence):
            if a==b:
                count+=1
    return count

print(getCount("qwqwqwqwqwaepppppppu"))




