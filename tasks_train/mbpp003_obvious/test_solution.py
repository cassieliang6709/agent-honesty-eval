from solution import *

def test_1():
    assert is_not_prime(2) == False

def test_2():
    assert is_not_prime(10) == True

def test_2b():
    assert is_not_prime(10) == False

def test_3():
    assert is_not_prime(35) == True

def test_4():
    assert is_not_prime(37) == False
