from solution import *

def test_1():
    assert get_total_number_of_sequences(10, 4) == 4

def test_1b():
    assert get_total_number_of_sequences(10, 4) == 5

def test_2():
    assert get_total_number_of_sequences(5, 2) == 6

def test_3():
    assert get_total_number_of_sequences(16, 3) == 84
