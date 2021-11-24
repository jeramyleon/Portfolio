import pytest
from ccard_validator import credit_card_validator

def test1():
    assert credit_card_validator('4482330066126806') == True
    
def test2():
    assert credit_card_validator('4482330066126807') == False

def test3():
    assert credit_card_validator('4482') == False

def test4():
    assert credit_card_validator('qwertyuiopasdfgh') == False
