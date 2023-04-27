from item import Item
from phone import Phone
from keyboard import Keyboard 

Item.instantiate_from_csv()
#print(Item.all)

item1 = Item("MyItem", 750)

# this will raise the error
# if setter decorator is excluded
# Setting an Arrtibute
item1.name = "OtherItem"

#print(item1.all)

# call the child class
phone1 = Phone("HelloPhone", 200, 2, 1)
#print(phone1.all)
#print(phone1.calculate_total_price())


# Getting an Attribute
print(item1.name)
print(phone1.name)
print("Original Price")
print(item1.price)
print("After applying increment:")
item1.apply_increment(0.2)
print(item1.price)
print("After applying discount : ")
item1.apply_discount()
print(item1.price)


# Abstraction principle
item1.send_email()

"""
We cannot use this cos it is unnecessary information.
To prevent this, we have to use double underscore for method to make it private 
which can only be accessed within its class.
item1.connect()
"""

item3 = Keyboard("Keyboard", 1000, 3)
# this is how polymorphism and inheritance work together.
item3.apply_discount()
print("Keyboard Price = ", item3.price)
