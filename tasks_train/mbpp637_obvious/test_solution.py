from solution import *

def test_1():
    assert noprofit_noloss(1500,1200)==False

def test_2():
    assert noprofit_noloss(100,100)==True

def test_2b():
    assert noprofit_noloss(100, 100) == False

def test_3():
    assert noprofit_noloss(2000,5000)==False
