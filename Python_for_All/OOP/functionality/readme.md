The **four main concepts** of `OOP` are :
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

### Encapsulation

We want to prevent the variables from being modified.

`@property` decorator has to be used.

`Property Decorator = Read-Only Attribute`

`@className.setter` decorator must be used to change a new value which is under `@property` decorator. For more details, see it in [item.py](https://github.com/khinthandarkyaw98/Python_For_All/blob/main/Python_for_All/OOP/functionality/item.py).

### Abstraction

It only shows the **necessary** attributes and hides the **unnecessary** information.

- [x] Hides **Unnecessary** details 

You can simply use the concept of `abstraction` by using **double underscores** before the method name, making it become a private method and keeping from being accessed outside of the class.


### Inheritance

The child class can reuse methods and attributes of its parent.

### Polymorphism

A single entity does know how to handle many different objects and does work with the concept of inheritance. See more details in [Keyboard.py](https://github.com/khinthandarkyaw98/Python_For_All/blob/main/Python_for_All/OOP/functionality/keyboard.py) and its called class in [main.py](https://github.com/khinthandarkyaw98/Python_For_All/blob/main/Python_for_All/OOP/functionality/main.py).