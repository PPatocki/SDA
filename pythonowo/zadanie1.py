#!/usr/bin/python3.7

from math import pi
print('Podaj promien kola: ')
r = float(input())
def area(a):
    result = pi*(a*a)
    return round(result, 1)

print(pi)
print(area(r))
#assert area(1.1) == 3.8
    
