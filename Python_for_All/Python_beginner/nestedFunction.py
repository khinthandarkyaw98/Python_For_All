def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ') # create a list out of the string by every space
    for word in words:
        say(word)

talk('I am going to buy the milk')


def count():
    count = 0

    def increment():
        nonlocal count # to call the outside local var
        count = count + 1
        print(count)

    increment()

count()

# closure
##############################################################
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment  # here we return the increment() function
    
increment = counter()
print(increment()) #1
print(increment()) #2
print(increment()) #3