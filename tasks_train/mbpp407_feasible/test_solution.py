from solution import *

def test_1():
    assert rearrange_bigger(12)==21

def test_2():
    assert rearrange_bigger(10)==False

def test_3():
    assert rearrange_bigger(102)==120
