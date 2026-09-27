from solution import *

def test_1():
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']

def test_2():
    assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']

def test_3():
    assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']

def test_4():
    assert extract_quotation("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []
