from solution import *

def test_1():
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True

def test_2():
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False

def test_3():
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True
