a = 'add'
b = 'abc'
'''
def isomorphic(a,b):
    if len(a) != len(b):
        returne False
    else:

from collections import Counter
def isomorphic(a,b):
    a_counts = list(Counter(a).values())
    a_counts.sort()
    b_counts = list(Counter(b).values())
    b_counts.sort()
    if a_counts == b_counts:
        return True
    return False
print(isomorphic(a,b))
'''



def f(a,b):
    slownik = {}
    for iterator, character in enumerate(slowo_1):
        if character in slownik:
            if slowo_2[iterator] != slownik[character]:
                return False
        else:
                slownik[character] = slowo_2[iterator]
    return True
print(f(a,b))     
