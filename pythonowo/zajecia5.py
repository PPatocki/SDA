#!/usr/bin/python3.7

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

'''
def average(list):
    return sum(list)/len(list)
print(average(list)

or

from statistics import mean
print(mean(list))
'''
'''
def selekcja(list):
    list2 = []
    for i in list:
        if i % 2  == 0:
            list2.append(i)
    return list2
print(selekcja(list))

#or

list2 = [i for i in list if i % 2 == 0]
print(list2)
'''
'''
dupa = [x for x in range(0, 101) if x % 3 == 0 and x % 5 == 0]
print(dupa)
'''

##################### List Comprehension z szyfrem cezara
'''
text = 'Litwo ojczyzno moja'
s = ''.join([chr(ord(c) + 3) for c in text])
print(s)
'''
'''
l = [[1,2,3], [4,5,6], [7,8,9]]

dupa = [[a * 3, b * 3, c * 3] for a, b, c in l]
print(dupa)
dupa2 = [a * 3 for x in l for a in x]
print(dupa2)
'''
######################## Dictionary comprehension
'''
#toopla na dicta zmienia // na chuj?
s1 = ((1, 2), (2, 3), (3, 4))

s2 = {k: v for k, v in s1}
print(s2)
# to jest set \/
s3 = {1, 2, 3, 4, 5, 6}

#zamiast modulo w rangu dodaje 3 i wyswietli co trzeci
dupa = [x for x in range(0, 101, 3)][::-1]
print(dupa)
'''
################## Petla niekonczaca sie dopuki nie wpisze sie dobrego inputu
################## Error handling?
'''
incorrect_input = True
while incorrect_input:
    incorrect_input = False
    try:
        a = int(input('Enter your number: '))
    except ValueError:
        incorrect_input = True
        print('Wrong input')
        continue
    try:
        b = (10/a)
    except (ZeroDivisionError, NameError):
        print('Wrong input bitch')
        incorrect_input = True

print('Zwyciestwooooo')
'''
#o kurwa ale nie mam sily...
'''
def numbers(a, b):
    while True:
        try:
            a = int(input('Podaj poczatek zakresy: '))
            b = int(input('Podaj koniec zakresu: '))
        except ValueError:
            print('invalid value')
            continue
    result = [liczba for liczba in range(a, b+1) if liczba % 5 == 0 and liczba % 7 == 0]

print(numbers(a, b))
'''
#3 przedmioty o najwyzszej wartosci i je wyswietlic
data = {'piwo': 45.50, 'kielbasa': 35, 'wodka': 22, 'fajki': 15, 'kartofelki': 7.30}

z = list(data.values())
z.sort()
for k, v in data.items():
    if v in z[-3:]:
        print(k, v)
# nie dziala jak cos
