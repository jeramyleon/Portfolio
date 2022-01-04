# Given a circularly sorted integer array, find the total number of times the array is rotated. Assume there are no duplicates in the array, and the rotation is in the 
# anti-clockwise direction.
from math import *
arr = [8, 9, 10, 2, 5, 6] # output should be 3 times 
arr1 = [9, 10, 2, 5, 6, 8]
def rotation_amount(arr):
    left = 0
    right = 2
    rotation_count = 0
    
    while arr[left] < arr[right]:
        mid = floor((left + right) / 2)
        right -= 1
        mid -= 1
        left -= 1
        rotation_count += 1

    return rotation_count

    
print(rotation_amount(arr1))

