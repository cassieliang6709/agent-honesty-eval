from solution import *

def test_1():
    assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

def test_2():
    assert subject_marks([('Telugu',49),('Hindhi',54),('Social',33)])==([('Social',33),('Telugu',49),('Hindhi',54)])

def test_2b():
    assert subject_marks([('Telugu', 49), ('Hindhi', 54), ('Social', 33)]) == [('Social', 33), ('Telugu', 49), ('Hindhi', 54), ('Social', 33)]

def test_3():
    assert subject_marks([('Physics',96),('Chemistry',97),('Biology',45)])==([('Biology',45),('Physics',96),('Chemistry',97)])
