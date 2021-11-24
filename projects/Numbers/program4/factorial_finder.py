# Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as 
# being 1. Solve this using both loops and recursion.

def factorial_finder(num): # using loop 
    if num == 0:
        return 1
    
    n = 1
    while num >= 1:
        n = n * num
        num = num - 1
    return n




def factorial_finder2(num): # using recursion
    if num == 1:
        return 1 
    elif num == 0:
        return 1
    else: 
        return num * factorial_finder2(num-1)

        

    
