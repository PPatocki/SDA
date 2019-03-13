from unittest import TestCase

# TestCase jest clasa bo z duzych liter
# python3 -m unittest unittesty.py w command lajnie
def dziel(a, b):
    return a/b


class TestDziel(TestCase):
    def setUp(self):
        self.wynik = dziel(1,1)
        # setUp wykona sie przed kazdym z testow. tutaj wbijamy zmienne na ktorych ma pracowac
        # zeby nic nie nadpisywalo tylko zawsze mialo ta sama wartosc


    def test_two_positive_numbers(self):
        result = self.wynik
        self.assertEqual(result, 1)
        self.assertIs(type(result), float)
    
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError) as context:
            dziel(1,0)
        self.assertIs(ZeroDivisionError, type(context.exception))











'''
from unittest.mock import patch?
rozkminic co to jest mockowanie!!!
nigdy nie nadpisywac __init__ w unit testach
'''
