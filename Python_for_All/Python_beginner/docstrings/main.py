from lib import docstrings

# you are importing the class which is an object
# so don't forget the paraenthesis
my_dog = docstrings.Dog("puppy", 8)
print(f"My dog's name is {my_dog.name}, and {my_dog.age} years old.")

my_dog.bark()
print(docstrings.increment(5))