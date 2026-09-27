from solution import *

def test_1():
    assert change_date_format("2026-01-02") == '02-01-2026'

def test_2():
    assert change_date_format("2020-11-13") == '13-11-2020'

def test_3():
    assert change_date_format("2021-04-26") == '26-04-2021'
