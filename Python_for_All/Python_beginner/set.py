# sets
# similar to tuple
# not in order
# mutable : you can change
# also similar to dict
# but no key
# immutable set = forzen set
# do mathematical operation
# set cannot have TWO OR MORE same items

set1  = {"Roger", "Syd"}
set2  = {"Roger", "Luna"}

# intersect
intersect = set1 & set2
print(f"intersect = {intersect}")

# union
mod = set1 | set2
print(f"Union = {mod}")

# differnce
diff = set1 - set2
print(f"difference = {diff}")

# superset
# do all elements of set2 exist in set1
sup = set1 > set2 
print(f"Is set1 is a superset of set2? = {sup}")

# subset
# do all elements of set1 exist in set2
sub = set1 < set2
print(f"Is set1 a subset of set2? = {sub}")

# list constructor
# convert set to list
print(list(set1))

# no duplicate
set1 = {"Roger", "Syd", "Roger"}
print(f"set1 = {set1}")