#!/usr/bin/python3
'''
virtualenv testowy
source ~/SDA/pythonowo/testowy/bin/activate
virtualenv -p python3 testowy

from cmath import cos
from math import cos as math_cos
#w tym momencie mozna uzywac obu, inaczej by sie nadpisaly

from math import *
import math

pip install -r requirements.txt
#w pliku znajduje sie lista pakietow a polecenie to sciagnie all
'''

start = "79-900"
stop = "80-155"

a, b = start.split('-')
c, d = stop.split('-')
startx = a + b
stopx = c + d


def kody():
    result = []
    for i in range(int(startx), int(stopx)+1):
        a = str(i)[:2] + '-' + str(i)[2:]
        result.append(a)
    return result

print(kody())
        
