import unittest

def sum_elements_in_list(list):
    return sum(list)




def find_biggest_number(list):
    return max(list)



def fibonacci_sequence(index_to_find):
    if index_to_find == 0:
        return 0
    elif index_to_find == 1:
        return 1
    else:
        return fibonacci_sequence(index_to_find-1) + fibonacci_sequence(index_to_find-2)



class Exam(unittest.TestCase):
    def test_sum_elements_in_list(self):
        self.assertEqual(sum_elements_in_list([1, 2, 3, 4]), 10)

    def test_find_biggest_number(self):
        self.assertEqual(find_biggest_number([8, 7, 100, 24]), 100)


    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(20), 6765)
