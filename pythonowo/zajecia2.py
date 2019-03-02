#!/usr/bin/python3.7
# zmienna przechowuje referencje do miejsca w pamieci a nie wartosc
'''
a = 4
b = -1
c=a
a=b
b=c
print(a, b)

a, b = b, a
print(a, b)

assert a == 4
assert b == -1
'''
#assert to taki test jednostkowy, zwraca error 
# przy definiowaniu fukncji to a i b to tylko placeholdery
# potem mozna podaj bylejakie
def swap(a, b):
   # pass
   # return None, None
    return b, a

print('paczatek programu')
# bez napisu pass bylby error. jak napisze pass to parser ja pomija
# wszystko po 4 spacjach jak pass jest w ciele funkcji a wracajac do poczatku linii jest poza
a = 4
b = -1

a, b = swap(a, b) 
# Kazda f() zwraca cos. jak jest "pass" to zwraca none. Dajac None, None jest ok bo 2 zmienne
# dostaja 2 wartosci

assert a == -1
assert b == 4
print(f'a={a}, b={b}')
print('koniec programu')

#imie = input()
#print('Siema', imie)
#print(f'siema {imie}')
print(input('Podaj\t swoje\n imie: '))
# \t wstawia tabulator; \n nowa linja


