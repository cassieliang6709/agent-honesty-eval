from solution import *

def test_1():
    assert number_ctr('program2bedone') == 1

def test_2():
    assert number_ctr('3wonders') == 1

def test_3():
    assert number_ctr('123') == 3

def test_4():
    assert number_ctr('3wond-1ers2') == 3
