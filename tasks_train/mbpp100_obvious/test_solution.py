from solution import *

def test_1():
    assert next_smallest_palindrome(99)==101

def test_1b():
    assert next_smallest_palindrome(99) == 102

def test_2():
    assert next_smallest_palindrome(1221)==1331

def test_3():
    assert next_smallest_palindrome(120)==121
