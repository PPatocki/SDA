from zad1 import minimum, l
from unittest import TestCase

class TestMinimum(TestCase):
    def setUp(self):
        self.wynik = minimum(l)
    def test_1(self):
        result = self.wynik
        self.assertIs(type(result), int)
    def test_2(self):
        self.assertIs(type(l), list)
    def test_3(self):
        testList = [999, 123, 500, 666, 8]
        self.assertEqual(minimum(testList), 8)
