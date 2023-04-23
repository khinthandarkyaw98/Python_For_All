class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    # constructor
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # method 
    def calculate_total_price(self): # pass its object as argument
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# create an instance of the class
item1 = Item("Phone", 100, 1) # call __init__ method automatically
item1.apply_discount()
print(item1.price) # pull pay_rate from class level

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7 # define at the instance level
item2.apply_discount()
print(item2.price) # pull pay_rate from instance level

#print(Item.__dict__) # All the attributes for Class level
#print("=" * 50)
#print(item1.__dict__) # ALl the attributes for instance level