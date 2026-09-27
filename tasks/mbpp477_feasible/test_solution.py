from solution import *

def test_1():
    assert is_lower("InValid") == "invalid"

def test_2():
    assert is_lower("TruE") == "true"

def test_3():
    assert is_lower("SenTenCE") == "sentence"
