# Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and 
# repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends
# in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
numbers = list(range(1, 32))

def ishappynumber(num):
    num = str(num)
    past_numbers = []

    while num != '1':
        sum = 0
        for n in num:
            sum += int(n)**2
        num = str(sum)

        if num in past_numbers:
            return False

        past_numbers.append(num)    

    return True
    

for number in numbers:
    if ishappynumber(number):
        print(str(number) + ' Happy :)')
    else:
        print(str(number) + ' Unhappy :(')






    








    




    












