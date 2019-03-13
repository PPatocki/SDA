"""
from given list return element with lowest value
"""

l=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1,]

def minimum(l):
    x=l[0]
    for i in l:
        if i<x:
            x=i
    return x
    
'''
def min2(l):
    l.sort()
    return l[0]

def min2_5(l):
    return list(sorted(l))[0]

def min3(l):
    return min(l)

print(min2(l))
print(min2_5(l))
print(min3(l))
'''
