# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, 
# multiply it by 3 and add 1.
number = 50

def collatz(number):
    steps = 0

    while number != 1:
        if number % 2 == 0:
            steps += 1
            print('Step ' + str(steps) + ': ' + str(number) + ' / 2 = ' + str(number/2)) # Step 1: 5 / 2 = 2.5 
            number = number / 2
        else:
            steps += 1
            print('Step ' + str(steps) + ': ' + str(number) + ' * 3 + 1 = ' + str(number * 3 + 1))
            number = number * 3 + 1 

collatz(number)

    


