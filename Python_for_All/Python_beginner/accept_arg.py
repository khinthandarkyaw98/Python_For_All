# Accepting Arguments
import sys

# click + sign in vs code terminal
# there you will see zsh terminal in vs code aka shell
# do not run the code using UI from vs code
# run by cmd in shell
# otherwise you can directly open the terminal
# locate directory by cd
# python3 accept_arg.py Beau 39
# output = ['accept_arg.py', 'Beau', '39']
print(sys.argv)

name = sys.argv[1]
print("Hello " + name)


import argparse

parser = argparse.ArgumentParser(
    description = "This program prints the name of my dogs"
)

# arguement you want to accept
# choices make you accept only options defined in the dict
parser.add_argument("-c", "--color", metavar = "color",
required = True, choices = {"red", "yellow"}, help = "the color to search for")

args = parser.parse_args()

print(args.color)