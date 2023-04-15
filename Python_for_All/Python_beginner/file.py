filename = "/Users/khinthandarkyaw/Documents/Python/test.txt"

# here we do not need to write
# file.close()
# with will call close() automatically for it
with open(filename, "r") as file:
    content = file.read()
    print(content)