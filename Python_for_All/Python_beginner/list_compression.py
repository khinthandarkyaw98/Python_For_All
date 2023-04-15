# List Compression
###############################################

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

###############################################
# if we do not use
# list compression
# we have to write like the followings
# multiple lines of code

numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
print(numbers_power_2)

###############################################
# or you can use the map as well

numbers_power_2 = []
numbers_power_2 = list(map(lambda n : n**2, numbers))
print("map() = ", numbers_power_2)