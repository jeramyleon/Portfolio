# Given a sorted array of n integers and a target value, determine if the target exists in the array in logarithmic time using the binary search algorithm. If target 
# exists in the array, print the index of it.
from math import *

arr = [1, 2, 3, 4, 5]
target = 5

def search(arr, target):
    left = 0
    right = len(arr) - 1 

    while left <= right:
        mid = floor(((left + right) / 2)
