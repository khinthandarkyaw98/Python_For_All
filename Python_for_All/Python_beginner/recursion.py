# RecursionError : when the base case is not included
# a function calls itself
# factorial
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 * = 24

def factorial(n):
    # base case
    if n == 1: return 1

    # recursive case
    return n * factorial(n -1)

print(factorial(3))
print(factorial(4))