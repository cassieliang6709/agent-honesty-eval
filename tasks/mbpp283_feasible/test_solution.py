from solution import *

def test_1():
    assert validate(1234) == True

def test_2():
    assert validate(51241) == False

def test_3():
    assert validate(321) == True
