#!/usr/bin/python3.7

#ord('a')=97
#chr(97)=a
'''
print('Wprowadz tekst do zaszyfrowania: ')
plain_text = input()

def to_cezar(plain_text, cypher_number=3):
    ciphered_text = ''
    for character in plain_text:
        number = ord(character)
        number += cypher_number
        ciphered_text += chr(number)
    return ciphered_text
print(to_cezar(plain_text))
a = to_cezar(plain_text)

assert to_cezar('a') == 'd'
assert to_cezar('b') == 'e'

def from_cezar(plain_text, cypher_number=3):
    ciphered_text = ''
    for character in plain_text:
        number = ord(character)
        number -= cypher_number
        ciphered_text += chr(number)
    return ciphered_text 
print(from_cezar(a))
'''
'''
print('wprowadz cyfre, z ktorej wyliczysz silnie: ')
cyfra = int(input())

def silnia(cyfra):
    if cyfra >= 1:
        wynik=1
        for x in range(1, cyfra+1):
            wynik=wynik*x #mozna to napisac wynik*=x
        return wynik
    else:
        print('funcja przyjmuje cyfry tylko wyzsze rowne 1')
print(silnia(cyfra))    
               
#rekursja
def silnia(n):
    if n == 1:
        return 1
    return n * silnia(n-1)
print(silnia(5))
'''

################# LEPSZY FOR #######################
'''
slownik = 
for e in slownik:
    print(e, slownik[e])

for key, value in slownik.items():
    print(key, value)


l = [[1,2,3], [4,5,6], [7,8,9]]

for i, j, k in l:
    print(i, j, k)
'''
string = 'qqwertgfdsahjklasdfglkjhqwertgfdsahjkl'
'''
l = set(string)
print(l)

for element in l:
    print(f'{element}: {s.count(element)}')
'''
'''
slownik = {}

for i in string:
    if i in slownik:
        slownik[i] += 1
    else:
        slownik[i] = 1
print(slownik)


from collections import Counter
print(Counter(slownik.split())) # split jesli bylby text i musialoby dzielic na slowach
'''

l = [1, 5, -8, 9, 44, 2, 99, -47, 123, 5, 31]
l.sort()
print(l[0])

print(min(l))
