#!/usr/bin/python3


# w nawiasie znajduje sie to po czym dana klasa dziedziczy
# obiekty maja typy, klasy nie

class Animal(object):
    count = 0
    def __init__(self, name='', age=0):
        self.name=name
        self.age=age

    def what_is_my_name(self):
        #print(self.name)
        print(f'My name is {self.name}')

class Cat(Animal):
    def Meow(self):
        print(f'{self.name}: Meow!')
        self.what_is_my_name
    def what_is_my_name(self):
        print(f'What? {self.name}')

class Dog(Animal):
    def Bark(self):
        print(f'{self.name}: Hau Hau Hau!')
        self.what_is_my_name

class Chimera(Dog, Cat):
    def what_is_my_name(self):
        #super znajduje klase nadrzedna i przekaz mnie tam
        super(Chimera, self).what_is_my_name()
        print(2)
    def meow(self):
        print(111)
        super(Chimera, self).meow()
    def __str__(self):
        return 'dupa'
    def __int__(self):
        return 5
    def __add__(self, a):
        return 5 + a
    def __len__(self):
        return 1000


'''
#Jak w klasie Animal jest atrybut name to kazdy kot bedzie mial taki atrybut i sie nie bedzie wywalac. Mozna wtedy smialo tak o\/ dopisywac imiona
cat.name = 'Puszek'

print(cat.name)

cat_2 = Animal()
print(cat_2.name)
#from nazwa pliku import klasa Animal
'''
cat = Animal(name = "Puszek", age=10)
cat_2 = Animal(age=4, name="Kicius")
cat_3 = Animal('Burek', 1)

cat.what_is_my_name()
cat_2.what_is_my_name()
cat_3.what_is_my_name()

c = Chimera(name='Monster', age=667)
c.Meow()
c.Bark()
################# __Metody magiczne__ #######################
#__str__ to rzutuje na stringa obiekt do wyswietlenia

class dict(dict):
    def __add__(self, a):
        return {**self, **a}

d1 = dict({'a': 'a'})
d2 = dict({'b': 'b'})
print(d1+d2)









