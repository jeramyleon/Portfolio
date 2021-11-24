# Given an array of integers, calculate the ratios of its elements 
# that are positive, negative, and zero. Print the decimal value of 
# each fraction on a new line with  places after the decimal.


def plusMinus(arr):
    # Write your code here
    length = len(arr)
    npz = [0, 0, 0]
    # index 0 is amount of positive, 1 is negative, 2 is zero
    
    for num in arr:
        if num > 0:
            npz[0] += 1
        elif num < 0:
            npz[1] += 1
        else:
            npz[2] += 1
    
    ratios = [float(str(num/length).ljust(6, '0')) for num in npz]
    for ratio in ratios:
        print(ratio)
    

array = [1, 1, 0, -1, -1]
plusMinus(array)
