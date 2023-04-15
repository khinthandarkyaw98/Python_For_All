# Classes
# we can declare our own classes
# we can instantiate our own objects
# an object is an instance of the class
# a class is also a type of an object

######################################
# IMPORTANT feature
# INHERITANCE

# INHERITANCE
#################################################
# Let's call a class before the class Dog

class Animal:
    # self must always be passed to point the current object which is class Animal
    def walk(self):
        print("Walking........")

class Dog: 
    # self as an argument of the method will point 
    # to the current object instance
    # whcih must be satisfied when defining the method
    def bark(self): 
        print("woof!")

roger = Dog()
print(type(roger))

###################################
# a special method
# __init__ aka CONSTRUCTOR

# For Dog2 class to inherit Animal class
# put parentheses after Dog to which class Animal must be passed
class Dog2(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof!")

roger2 = Dog2("Roger", 8)

# access the information of the class's constructor
##################################################
print(roger2.name)
print(roger2.age)

roger2.bark()
roger2.walk()


