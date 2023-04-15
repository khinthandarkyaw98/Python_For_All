# this is a commented line.
name = "Beau" 
print(isinstance(name, str))

# convert from one datatype to another
# via class constructor
# aka casing
age = float(2)
print(isinstance(age, float))

age = int("20")
print(isinstance(age, int))

number = "20"
age = int(number)
print(isinstance(age, int))

############################################################
############################################################


# operation 
# 1 + 1 # 2
# 2 - 1 # 1
# 2 * 2 # 4
# 4 / 2 # 2.0
# 4 % 3 # 1
# 4 ** 2 # 16
# 5 // 2 # 2


age = 8
age += 8  # age = age + 8
print(age)

a = 1
b = 2
a == b  # False
a != b  # True
a > b  # False
print(a <= b)  # True 

condition1 = True
condiition2 = False
print(not condition1)  # False

# or evaluates the 2nd argument if the 1st one is False
###################################################################
print(0 or 1)  # return 1, bc or return the True value only
print(False or 'hey')   # 'hey'
print('hi' or 'hey')  # 'hi'
print([] or False)   # 'False', bc '[]' is False so it returns the 2nd value which is 'False'
print(False or [])  # '[]'

# and only evaluates the 2nd argument if the 1st one is True
# if x is False then y
###################################################################
print(0 and 1)  # 0
print(1 and 0)  # 0
print(False and 'hey')  # False
print('hi' and 'hey')   # 'hey'
print([] and False)     # []
print(False and [])     # False

# & performs binary AND
# | performs binary OR
# ^ performs binary XOR
# ~ performs binary NOT
# << shift left operation
# >> shift right operation

def is_adult(age):
    if age > 18:
        return True
    else: 
        return False

# Turnary operator
def is_adult2(age):
    return True if age > 18 else False

name = "Beau"
name += " is my name."
print(name)

age = str(39)
print(age)

# mulitple line strings
##########################################
print("""
Beau is

39 years

old.
""")

# built-in print functions
##########################################
print("bEau".upper())
print("BEAU".lower())
print("beau person".title())  # 'Beau Person'
print("beau".islower())  # True

# The followings do not modify the original string.
##########################################
# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contans characters or digits and is not empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get an uppercase version of a string
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startswith() to check if the string starts with a specific substring
# endswith() to check if the string end with a specific substring
# replace() to replace a part of a string
# split() to trim the whtiespace from a string
# join() to append new letters to a string
# find() to find the position of a substring

name = "Beau"
print(f"name.lower() = {name.lower()}")
print(f"name = {name}")
print(len(name))

# check the substring
#########################
print("au" in name)

# escaping the character
#########################
name = "Be\au" # Beu
print(name)

name = "Be\"au"
print(name)

name = 'Be"au'
print(name)

name = "Be\"\'au"
print(name)

# add a new line
#########################
name = "Be\nau"
print(name)

# Indexing
#########################
name = "Beau"
print(name[-1])
print(name[1:2])

# Boolean
#########################
done = True

if done:
    print("yes")
else:
    print("no")

done = "" # this means False bc of its empty string
print("yes") if done else print("no")
print(type(done) == bool)

ingredients_purchased = True
meal_cooked = False

# return True only when elements in the list of all are True
ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve)
























