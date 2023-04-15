# Tuples 
# create an immutable object
# once when created, you cannot add or remove
names = ("Roger", "Syd", "Beau")

print(names[0])
print(names.index("Roger")) # 0
print(len(names))
print("Roger" in names)
print(names[0: 2])

# sorted function for tuple
print(sorted(names))
print(names)

# we can combine two tuples 
# but the resulting tuple must be a new tuple
# bc we cannot modify the original tuple
newTuple = names + ("Tina", "Quincy")
print(newTuple)
