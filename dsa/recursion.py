def factorial(num):
    if num >= 1:
        return num * factorial(num-1)
    else:
        return 1

def fib(num):
    fibonacci = 1 + 1
    num = num - 3

    while num != 0:
        fibonacci = fibonacci + (fibonacci + 1)
    return fibonacci

       