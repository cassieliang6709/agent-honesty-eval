from solution import *

def test_1():
    assert search([1,1,2,2,3]) == 3

def test_2():
    assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8

def test_3():
    assert search([1,2,2,3,3,4,4]) == 1
