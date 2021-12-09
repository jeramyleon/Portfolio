# Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and 
# repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends
# in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

# 4, do 4 squared,16, then do 1 squared plus 6 squared, then the result of that do both numbers squard until you reach 1.

def is_happynumber(number):
    # convert number to string and then into an array
    # loop through the array and add the squares of each digit
    # re assign value of that sum 
    # continue until you get 1
    if len(str(number)) == 1:
        number = number * number 
    else:
        number = list(str(number))
        



is_happynumber(16)

    