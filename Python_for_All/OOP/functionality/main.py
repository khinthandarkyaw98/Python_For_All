from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)

item1 = Item("MyItem", 750)
item1.name = "OtherItem"

print(item1.all)

# call the child class
phone1 = Phone("HelloPhone", 200, 2, 1)
print(phone1.all)
print(phone1.calculate_total_price())