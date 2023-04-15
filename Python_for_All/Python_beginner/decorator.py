# Decorators
# @ symbol followed by the decorator name
# just before the def function

# whenever the function is called
# the decorator is also called

# the decorator is a function that takes 
# the function as a parameter
# and wraps the function in its inner function
# and does the job supposed to be done 
# returns the value from its innner function
# returns that inner function from the outer function

# mostly used in test cases
# when we want to do some changes to the function
# without modifying the original function

def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val
    return wrapper

# the function hello has
# the logtime decorator
@logtime
def hello():
    print("Hello!")

hello()