from solution import *

def test_1():
    assert remove_lowercase("PYTHon")==('PYTH')

def test_2():
    assert remove_lowercase("FInD")==('FID')

def test_3():
    assert remove_lowercase("STRinG")==('STRG')
