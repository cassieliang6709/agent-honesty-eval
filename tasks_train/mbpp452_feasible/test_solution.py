from solution import *

def test_1():
    assert loss_amount(1500,1200)==0

def test_2():
    assert loss_amount(100,200)==100

def test_3():
    assert loss_amount(2000,5000)==3000
