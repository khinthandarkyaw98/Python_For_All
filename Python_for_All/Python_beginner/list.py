# essential in DS
# hold different types of data types 
dogs = ["Roger", 1, "Syd", True]

print("Roger" in dogs) # True

# Indexing
print(dogs[0]) # "Roger"
print(dogs[-1]) # True

# Updating the list
dogs[2] = "Beau"
print(dogs)

# Slicing
print(dogs[1: 3])
print(dogs[:3])

# length
print(len(dogs))

# add items to the list
dogs.append("Quincy")
dogs.append(7)
dogs.append("Judah")
dogs.append(2)
print(dogs)

# extend 
dogs.extend(["Apple", 10])
print(dogs)

# plus equal
dogs += ["Pole", 5]
print(dogs)

# remove
dogs.remove("Pole")
print(dogs)

# pop : move and return the single item
print(dogs.pop()) # 5
print(dogs)

# insert : add item at the specific index
dogs.insert(2, "Test")
print(dogs)

# add multiple items into the list
dogs[1: 1]  = ["Kawaii", "usoi"]
print(dogs)

# sort the list
dogs = [str(item) for item in dogs]
dogs.sort()
print(dogs)

# ignore the uppercase or the lowercase in sorting
dogs.sort(key = str.lower)
print(dogs)

# copying
dogsCopy = dogs[:]
print("Copying")
print(dogs)
print(dogsCopy)

items = ["Xo", "Kaa", "Apple", "apple"]

# I do not want to modify the original list while sorting
# call the global function, sorted()
print(sorted(items, key = str.lower)) # ['Apple', 'apple', 'Kaa', 'Xo']
print(items) # ["Xo", "Kaa", "Apple", "apple"]


