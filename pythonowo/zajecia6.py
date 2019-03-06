#!/usr/bin/python3.7
'''
lista = ['dupa', 'janusz', 'roza', 'polisyndeton', 'kielbasa', 'piwo', 'fajki', 'mydlo', 'malpiszon', 'nosorozec', 'smieszek', 'kacper', 'mammamia', 'bmw', 'audi', 'mercedes', 'kia', 'opel', 'toyota', 'dacia', 'hyundai', 'renault', 'fizjologia', 'hirurgia', 'pulmonologia', 'abrakadabrabumcykcyk']
def filter_long_words(list, n):
    list2 = []
    for e in list:
        if len(e) >= n:
            list2.append(e)
    return list2
print(filter_long_words(lista, 7))

#mozna zapisac tak

#def f2(l, n): return [slowo for slowo in l if len(slowo) > n]
'''

lista = [1, 2, 3, 7, 8, 10]
'''
def sprawdzenie(list):
    list2 = []
    licznik = 1
    for e in list:
        if int(e) == licznik:
            licznik += 1
        else:
            list2.append(licznik)
    return list2

print(sprawdzenie(lista))
'''
#to dziala\/
'''
def n(l, n):
    result = []
    for i in range(1, n+1):
        if i not in l:
            result.append(i)
    return result

print(n(lista, 15)) 
'''
#Olka rozwiazanie\/
#ef missing(list_check, max):
 #  return list(set(range(1, max+1)) - set(list_check))

def zadanie():
    result = []
    i = 2
    while i <= 5.5:
        result.append(i)
        i += 0.5
        
    return result
print(zadanie())






