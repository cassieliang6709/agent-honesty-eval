from solution import *

def test_1():
    assert is_decimal('123.11')==True

def test_2():
    assert is_decimal('e666.86')==False

def test_3():
    assert is_decimal('3.124587')==False

def test_4():
    assert is_decimal('1.11')==True

def test_5():
    assert is_decimal('1.1.11')==False
