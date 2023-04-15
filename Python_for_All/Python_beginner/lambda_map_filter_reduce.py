# map, filter, reduce
# python provides three useful global functions
# which can be used together with collection

####################################
# map()
####################################
# a function in which 
# the 1st var is the function we define
# the 2nd var is the argument whcih will pass
# as a parameter into the function aka the 1st var
# we already defined

numbers = [1, 2, 3]
def double(a):
    return a * 2

result = map(double, numbers)

print(list(result))

######################################

numbers2 = [2, 4, 6]

double2 = lambda num  : num * 2

result2 = map(double2, numbers2)
print(list(result2))

###################################

numbers3 = [5, 10, 100]

result3 = list(map(lambda b : b * 2, numbers3))

print(result3)

####################################
# filter()
####################################
# filter() takes an iterable and returns an filtered object

numbers4 = [0, 1, 2, 3, 4, 5, 6]

def isEven(n):
    return n % 2 == 0

result4 = list(filter(isEven, numbers4))

print(result4)

####################################

numbers5 = [0, 1, 2, 3, 4, 5, 6]

result5 = list(filter(lambda c : c % 2 == 0, numbers5))

print(result5)

####################################
# reduce()
####################################
# reduce() is used to calculate a value of a sequence
# as a list

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)

####################################

from functools import reduce

expenses2 = [
    ('Dinner', 80),
    ('Car repair', 120)
]

# d = acccumulated value
# e = updated value from the iteration
sum = reduce(lambda d, e : d[1] + e[1], expenses2)

print(sum)