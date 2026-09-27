from solution import *

def test_1():
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'

def test_2():
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'

def test_3():
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

def test_3b():
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617x'
