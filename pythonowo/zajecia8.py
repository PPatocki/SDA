#!/usr/bin/python3
'''
def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in word1:
        if i not in word2:
            return false
    for i in word2:
        if i not in word1:
            return False
    return True

print(is_anagram('koks', 'skos'))


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
print(is_anagram('koks', 'skok'))
'''
import random
def funkcja(nawiasy):
    if len(nawiasy) % 2 == 1:
        return False
    while '[]' in nawiasy:
        nawiasy = nawiasy.replace('[]', '')
        if nawiasy == '':
            return True
    return False

print(funkcja('[]'))
print(funkcja('[]][[]'))
print(funkcja('[[[[[[[[[[]]]]]]]]]]'))

def gen(n):
    result = ''
    for _ in range(n):
        if random.random() > 0.5:
            result += '['
        else:
            result += ']'
    return result
