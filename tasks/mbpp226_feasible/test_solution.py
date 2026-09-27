from solution import *

def test_1():
    assert odd_values_string('abcdef') == 'ace'

def test_2():
    assert odd_values_string('python') == 'pto'

def test_3():
    assert odd_values_string('data') == 'dt'

def test_4():
    assert odd_values_string('lambs') == 'lms'
