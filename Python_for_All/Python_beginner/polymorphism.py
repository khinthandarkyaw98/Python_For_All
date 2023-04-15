# Polymorphism

# gnerealizes the functionality
# different class, same method name
# important in OOP

class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")
    
animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()