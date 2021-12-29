# Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and 
# repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends
# in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
numbers = [1, 7, 10, 13, 19, 23, 28, 31]
happy_numbers = [] # append the happy numbers here so we can go back and check them for answers to shorten the runtime of our program

def ishappynumber(num):
    num = str(num) # converting number to string so we can access the numbers seperately
    sum = 0
    for i in num:
        sum += int(i)**2  
    
    if sum == 1:
        return 1 
    elif sum != 1:
        ishappynumber(sum)


for n in numbers:
    if 



    












