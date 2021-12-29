given_list = [1, 2, 3, 4, 5]

def find_sum(given):
    sum = 0 # O(1)
    for i in given: # n   Time = O(1) + n*O(1) + O(1)      
        sum += i # O(1)   Time = O(1) + n*O(1)
    return sum # O(1)     Time = O(n)

# as the size of given increases, the overall runtime increases
# linear time O(n) 
# constant time O(1)
# quadratic time O(n^2)

def stupid_function(given):
    total = 0 # O(1)            Time = O(1) + O(1) = O(1)
    return total # O(1)         Two constant times will give you a constant

array_2d = [[1, 4, 3], [3, 1, 9], [0, 5, 2]]

def find_sum_2d(array_2d):
    total = 0 # O(1)            Time = O(1)+O(1)+n^2*O(1)
    for each in array_2d: # n   Time = O(1) + N^2*O(1)
        for i in each: # n      Time = O(n^2)
            total += i #O(1)
    return total # O(1)




