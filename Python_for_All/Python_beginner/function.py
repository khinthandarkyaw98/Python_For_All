# Functions
# decompose a program into mangaable parts
# readiblity and reuse
# function's name should be descriptive

# function
def hello():
    print("Hello!")

# call the function
hello()
hello()
hello()

# pass parameter def hell_(name):
def hello_(name = "my friend"):
    print("Hello " + name)

# pass argument
hello_("Coral")
hello_("Nita")
hello_()

def hello2(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old!")

hello2("Coral", 24)


##################################################
def change(value):
    # changing the parameter inside the function
    # does not reflect outside the function
    # this case is expctional for dictionary
    value = 2

val = 1
change(val)

print(val)

##################################################
def change(value):
    # in this case
    # the value of the dic val will be changed
    # bc dict is mutable
    # changing the value of the dict in the function
    # reflects even outside of the function
    value["name"] = "Syd"

val = {"name" : "beau"}
change(val)

print(val)

# return statement
def hello3(name = "Coral"):
    if not name:
        return 
    print("Hello " + name + "!")
    return (name + " loves honey!")
    # when the func sees return
    # the function ends
    print("END") # this wont appear

print(hello3("Pooh"))

# global variable 
age = 8

def test():
    print(age)
    # local variable
    food = "meat"

test()
# print(food) # error occurs due to the local variable being called outside the function

