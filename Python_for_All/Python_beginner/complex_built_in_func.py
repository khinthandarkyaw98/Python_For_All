# complex numbers
#########################
complex_num = 2 + 3j

# complex constructor
#########################
num = complex(2, 3)
print(f"real = {num.real}, imaginary = {num.imag}")

# abs 
#########################
print(abs(-5.5)) # 5.5

# round
#########################
print(f"round(5.54) = {round(5.54)}") # 6

print(f"round(5.45) = {round(5.45)}") # 5

print(f"round(5.49, 1) = {round(5.49, 1)}") # 5.5

# input
#########################
# age = input("What is your age? ")
# print("Your age is " + age + ".")

# control statements
#########################
condition = "ok"

if condition == True:
    print("The condition")
    print("was true")
elif condition == False:
    print("This is False")
else: 
    print("OK")

print("outside if")
