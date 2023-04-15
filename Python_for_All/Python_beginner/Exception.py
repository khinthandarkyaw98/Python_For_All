# Exceptions
# important to handle errors

""" try: 
    # some lines of code
except <Error1>:
    # handler <Error1>
except <Error2>:
    # handler <Error2>
except:
    # handle the rest of the Exceptions
else: 
    # if no error occurs, execute else
finally:
    # do something in any case """

try: 
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot be divided by zero!")
finally: 
    result = 1
print(result) #1

# this will execute an error no matter what!
# Lines after this raise exception
# will not be executed
# to avoid this
# put this in try except
# raise Exception("An error!")

try: 
    raise Exception("An error!")
except Exception as error:
    print(error)

###################################################
# you can also define your own Exceptin calss
# which must extend from exception
# meaning (pass Exception as an argument into your 
# # own Exception class)
###################################################

class DogNotFoundException(Exception):
    print("Inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog Not Found!")

##################################################
# Open the file with try finally 
##################################################
filename = "/Users/khinthandarkyaw/Documents/Python/test.txt"

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()