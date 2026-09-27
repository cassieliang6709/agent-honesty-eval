from solution import *

def test_1():
    assert min_of_three(10,20,0)==0

def test_2():
    assert min_of_three(19,15,18)==15

def test_2b():
    assert min_of_three(19, 15, 18) == 16

def test_3():
    assert min_of_three(-10,-20,-30)==-30
