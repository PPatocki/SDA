#!/usr/bin/python3.7
'''
otwieramy pliki w pythonie poleceniem
file = open('test.txt', 'r/w')
file.close()
trzeba tez to przypisac do zmiennej zeby cos z tym zrobic
drugi atrybut wskazuje tryb w jakim otwieramy plik.
Jak jest 'w' to musimy dac close() bo inne procesy nie dostana sie do pliku

file.write()
file.readlines()
file.read()

####### CONTEXT MANAGER ###############3

with open('test.txt', 'w') as file_handler:
    pass
    file_handler.write('dupa')
otwiera plik ale tylko wewnatrz tej "funkcji".file_handler to tylko nazwa zmiennej

'''
########### PETLE #############
'''
#patrz zad3_2.py
liczba = int(input('Wprowadz liczbe: '))

if liczba > 2:
    print('Liczba jest wieksza od dwa')
elif liczba == 2:
    print('liczba jest rowna 2')
else:
    print('klamstewko')
'''

######## WHILE  #######
'''
petle nieskonczona tworzymy przy programach okienkowych. break dziala wtedy jak user zamknie okno. Bez tego petla caly czas dziala i renderuje okienko

warunek = True
while warunek:
    if 45<int(input()):
        warunek = False
       # break #absolutnie konczy dzialanie petli
    else:
	continue #odsyla nas na poczatek petli
    print('dupa')




i = 0
while i<3:
    i=i+1 to to samo co i+=1
    #i=i-1 to to samo co i-=1 
    #i/=4 dzieli przez 4 i zapisuje do i
    #i*=4 mnozy przez 4 i zapisuje do i


lista = ['karkowka', 'piwo', 'wodka', 'fajki']
ceny = {
    'karkowa': 1,
    'piwo': 2,
    'wodka': 10,
    'fajki': 15
}
i = 0
while i < len(lista):
    print(lista[i], ceny[lista[i]])
    i+=1
'''
########## List comprehension  ###################
'''
 i=1500
 51 l = []
 52 while i<=2700:
 53     if i % 5==0 and i % 7==0:
 54         l.appent(i)
 55         print(i)
 56     i+=1
 57 print(l)
# to jest to samo \/
print([l for l in range(1500, 2701) if l % 5 ==0 and  l % 7 == 0])
'''
################### FOR #####################################
from time import sleep

for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        sleep(2)

#o tyle jest dobre ze nie trzeba inkrementowac
