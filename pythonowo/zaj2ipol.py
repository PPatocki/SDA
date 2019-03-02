#!/usr/bin/python3.7

#LISTY, moze wiec wiele elementow roznego typu
l=['a', 1, 1.2, True, None, zmienna, [], ]
print(l)
print(len(l))
print(l[4])
print([len(l)-1])
print(l[-1]) ostatni element
l[-1] = [1, 2, 3]
l[-1][2] wyswietla 2gi indeks w liscie wewnetrznej i stringach
string jest nie mutowalny a lista tak
l[0][4] = 4
onacza to ze mozna podmieniac elementy w listach 

###### SLICY #####
l[2:] wyswietlaj od 2go indeksu do konca
l[:2] wyswietlaj do 2go indeksu od poczatku ale bez 2go
l[::2] wyswietla co drugi element ::3 to co trzeci
l[::-1] odwraca kolejnoscia liste

# dokladanie elementow do listy
l.append('dupa') doda element na ostatnim miejscu
l.insert(miejsce, to co chcemy wsadzic)
###################################################################################################################

LISTA jest mutowalna TUPLE #***NIE***#
Jesli w tuplu jest lista to ja MOZNA modyfikowac
#TUPLE - krotka?
#uzywane np do listowania settingsow

t = (5, 'a', None,() )

help(x) gdzie x jest zmienna i help rozpoznaje co to jest
##################################################################################################################

#SLOWNIK
Slownik do kazdego argumentu potrzebuje klucza i wartosci
s = {'kolor': 1, 'typ': 1234, 'model': 'Ford', 1: 123}
indeksy nie istnieja, tylko klucze
s['kolor']
zwroci 1
s['dupa'] = 1234
dodaje element do slownika o wartosci 1234
'dupa' in s da True bo element znajduje sie w slowniku 'd' in s da False
