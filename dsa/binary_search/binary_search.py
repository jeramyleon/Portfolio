from math import *

arr = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11 

def search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = floor((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1 

print(search(arr, target))





arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 9

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1 

    while left <= right:
        mid = floor((left + right) / 2)
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1 
    
    return -1 

print(binary_search(arr, target))
















































