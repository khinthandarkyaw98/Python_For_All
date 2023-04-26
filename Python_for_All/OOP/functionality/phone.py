from item import Item

"""
when we initialize the constructor in the child class,
python forces us to call function intentionally.
Its name is super() which allows us to access all attributes of the parent class.
By using super(), we do not need to hard code.
"""

class Phone(Item):
    # all = []
    def __init__(self, name:str, price:float, quantity:int, broken_phones=0):
        # Call super function to have access to all attributes/me
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to the received arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero."
        # assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero."
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to zero."
        
        """ # we will replace the following by super() shown above
        self.name = name
        self.price = price
        self.quantity = quantity """
        self.broken_phones = broken_phones
        
        # Actions to execute
        # Phone.all.append(self)
        
        