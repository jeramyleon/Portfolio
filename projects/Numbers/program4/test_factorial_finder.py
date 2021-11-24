import pytest
from factorial_finder import factorial_finder
from factorial_finder import factorial_finder2



def test1():
    assert factorial_finder(7) == 5040

def test2():
    assert factorial_finder(0) ==  1

def test3():
    assert factorial_finder2(0) == 1

def test4():
    assert factorial_finder2(7) == 5040

def test5():
    assert factorial_finder2(6) == 720

def test6():
    assert factorial_finder2(5) == 120