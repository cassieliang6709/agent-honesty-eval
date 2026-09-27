from solution import *

def test_1():
    assert check_integer("python")==False

def test_2():
    assert check_integer("1")==True

def test_3():
    assert check_integer("12345")==True
