#!/usr/bin/python3.7
'''
numbers = input('Podaj swoje szczesliwe liczby: ').split()
print(numbers)
print('42' in numbers)
'''
##########################################################3
'''
d=0
def konwerter(C):
   # F=C*1.8 + 32
   # return round(F,1)
    return C*1.8+32

print('F=', konwerter(d))

assert konwerter(0) == 32
a = input('Podaj temperature w Celcjuszach: ')
print(konwerter(float(a)))
'''
##################################################################3
'''
import random

choices = ['paper', 'rock', 'scissors']
#computer = choices[random.randint(0, 2)]
computer = random.choice(choices)
player=input('Choose paper rock or scissors: ')

if player == computer:
    print('It is a tie. nobody wins')
elif player == 'scissors' and computer == 'rock':
    print('You lost! Go fuck yourself!!!')
elif player == 'scissors' and computer == 'paper':
    print('You win')
elif player == 'rock' and computer == 'paper':
    print('You loose!')
elif player == 'rock' and computer == 'scissors':
    print('You win!')
elif player == 'paper' and computer == 'scissors':
    print('You loose')
elif player == 'paper' and computer == 'rock':
    print('You win!!!')
else:
    print('You can only choose from paper rock and scissors')
'''
################################################################3
#podzielne przez 7 i 5 w przedziale 1500-2700
'''
i=1500
l = []
while i<=2700:
    if i % 5==0 and i % 7==0:
	l.appent(i)
        print(i)
    i+=1
print(l)
'''
'''
for i in range(1,51):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

#for i in range(1, 10):
#    print(str(i) *

from itertools import permutations

l=permutations(['a', 'e', 'i', 'o', 'u', 'y'])
b=0
for i in list(l):
    print(i)
    b+=1
print(b)
'''
#chr() i ord()
#szyfr cezara dziala a=c b=d






