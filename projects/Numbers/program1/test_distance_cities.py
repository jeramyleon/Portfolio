import pytest
from distance_cities import calculate_distance

def test():
    assert isinstance(calculate_distance('new york', 'san juan', 'miles'), (float))

def test2():
    assert calculate_distance(5, 6, 7) == False

def test3():
    assert calculate_distance(None, None, 'feet') == False





