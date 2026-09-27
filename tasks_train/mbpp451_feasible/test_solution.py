from solution import *

def test_1():
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'

def test_2():
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'

def test_3():
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'
