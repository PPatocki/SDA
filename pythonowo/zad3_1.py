#!/usr/bin/python3.7
'''
#print('Podaj swoje imie: ')
imie = input('Podaj swoje imie: ')
print('Podaj swoje nazwisko: ')
nazwisko = input()
print('Siema', nazwisko, imie)
'''
imie_i_nazwisko = input('Podaj imie i nazwisko: ').split()
print(imie_i_nazwisko)

drugie, pierwsze = imie_i_nazwisko
print(pierwsze, drugie)
#print(*imoie_i_nazwisko[::-1])
#gwiazdka rozpakowuje np slownik czy tupla
#print(*input('Podaj imie i nazwisko: ').split()[::-1])
