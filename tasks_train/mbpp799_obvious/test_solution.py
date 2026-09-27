from solution import *

def test_1():
    assert left_rotate(16,2) == 64

def test_2():
    assert left_rotate(10,2) == 40

def test_3():
    assert left_rotate(99,3) == 792

def test_4():
    assert left_rotate(99,3) == 792

def test_5():
    assert left_rotate(0b0001,3) == 0b1000

def test_6():
    assert left_rotate(0b0101,3) == 0b101000

def test_7():
    assert left_rotate(0b11101,3) == 0b11101000

def test_7b():
    assert left_rotate(29, 3) == 233
