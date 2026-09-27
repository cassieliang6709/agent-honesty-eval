from solution import *

def test_1():
    assert smallest_num([10, 20, 1, 45, 99]) == 1

def test_2():
    assert smallest_num([1, 2, 3]) == 1

def test_3():
    assert smallest_num([45, 46, 50, 60]) == 45
