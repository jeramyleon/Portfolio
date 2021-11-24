import pytest 
from tax_calculator import tax_calculator

def test1():
    assert tax_calculator('12', 'maine') == True
    
def test2():
    assert tax_calculator('e', 'lasdkl;askd') == False

def test3():
    assert tax_calculator('12', 'sddmada') == False

def test4():
    assert tax_calculator('e', 'wyoming') ==  False