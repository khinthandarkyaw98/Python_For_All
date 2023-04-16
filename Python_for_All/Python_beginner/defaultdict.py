from collections import defaultdict

my_list = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
my_dict = defaultdict(int)
for fruit in my_list:
    my_dict[fruit] += 1
print(my_dict)

# output
# defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})
