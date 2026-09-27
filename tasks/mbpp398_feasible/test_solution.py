from solution import *

def test_1():
    assert sum_of_digits([10,2,56])==14

def test_2():
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19

def test_3():
    assert sum_of_digits([10,20,-4,5,-70])==19
