from solution import *

def test_1():
    assert check_expression("{()}[{}]") == True

def test_2():
    assert check_expression("{()}[{]") == False

def test_3():
    assert check_expression("{()}[{}][]({})") == True
