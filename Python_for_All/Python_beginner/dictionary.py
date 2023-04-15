# Dictionaries
# key : value pair
# key must be immutable
dog = {"name" : "Roger", "age" : 8}
print(dog["name"]) # Roger

# change value stored at the specific index
dog["name"] = "Syd"
print(dog)

# get mehthod
print(dog.get("name"))

# return brown as defualt if there is no color key in dog dict
print(dog.get("color", "brown"))
dog["color"] = "green"
print(dog.get("color", "brown"))

# pop() to remove the key and value by specific key
print("pop() = "  + dog.pop("name")) # remove and return the value of the key removed
print(dog)

# popitem() to remove the last key, value pair
print(f"popitem() = {dog.popitem()}") # remove and return the last item removed as a tuple
print(dog)

print("color" in dog)

# get a list of keys by the key of dict
print(dog.keys())
print(list(dog.keys()))

# get a list of values 
print(dog.values())
print(list(dog.values()))

# get keysand values in the list form
print(list(dog.items()))

print(len(dog))

# add new values by keys
dog["name"] = "Roger"
dog["favorite food"] =  "Meat"
dog["color"] = "brown"
print(dog)

# copy the dictionary
dogCopy = dog.copy()
print(dogCopy)

# delete items by keys
del dog["color"]
print(dog)