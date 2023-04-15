# loops

# while
# for

condition = True
while condition == True:
    print("The condition is True")
    condition = False # otherwise, this will become an infinite loop

count = 0 
while count < 10:
    print("The condition is True : count " + str(count))
    count += 1

print("After the loop")

########################################
# normally
# for is used to iterate the list
items = [1, 2, 3, 4]
for item in items:
    print(item)

print()

# iterate a specific range of for loop
for item in range(15):
    print(item)

print()

# get the index 
items = ['a', 'b', 'c']
for index, item in enumerate(items):
    print(index, item)

print()

# continue
# stops current iteration until the python executes a new one

# break
# stops the loop altogether and goes on with the next instruction after the loop ends
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue # skip 2
    print(item)

print() 

for item in items:
    if item == 2:
        break # end the loop after 1
    print(item)