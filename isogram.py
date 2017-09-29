#Conor Kennedy
#9/29/17

'''
Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.
'''

def isogram(s):
    s = s.lower()
    for x in s:
        if s.count(x) > 1:
            return False
    return True
    
print (isogram("aba"))
print (isogram("abcd"))
print (isogram("abcd a"))
