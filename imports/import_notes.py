# ============================================================
#                    PYTHON IMPORTS
# ============================================================

# ============================================================
# 1. WHAT IS AN IMPORT?
# ============================================================

# An import lets us use code that was written somewhere else.

# Python comes with many built-in modules that we can use.

# Example:

import random


# ============================================================
# 2. WHAT IS A MODULE?
# ============================================================

# A module is a Python file containing code we can reuse.

# Python has many built-in modules.

# Some examples:

# random  -> random numbers
# math    -> mathematical functions
# time    -> time-related functions
# os      -> operating system tools


# ============================================================
# 3. IMPORTING A MODULE
# ============================================================

import random

# Once we import random, we can use functions from it.

number = random.randint(1, 10)

print(number)

# randint(1, 10) gives us a random integer
# between 1 and 10.


# ============================================================
# 4. USING FUNCTIONS FROM A MODULE
# ============================================================

import random

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)

print(number1)
print(number2)


# Every time you run the program,
# you may get different numbers.


# ============================================================
# 5. RANDOM CHOICE
# ============================================================

import random

foods = [
    "Pizza",
    "Burger",
    "Tacos",
    "Pasta"
]

food = random.choice(foods)

print("Today's food:", food)

# random.choice() picks one item from a list.


# ============================================================
# 6. RANDOM CHOICE WITH STRINGS
# ============================================================

import random

colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow"
]

color = random.choice(colors)

print("Your color is:", color)


# ============================================================
# 7. THE MATH MODULE
# ============================================================

import math

# math contains useful mathematical functions.

print(math.sqrt(25))

# sqrt means square root.

print(math.sqrt(100))


# ============================================================
# 8. MATH CONSTANTS
# ============================================================

import math

print(math.pi)

# math.pi gives us the value of π.


# ============================================================
# 9. ROUNDING UP AND DOWN
# ============================================================

import math

number = 4.2

print(math.ceil(number))

# ceil() rounds UP.

print(math.floor(number))

# floor() rounds DOWN.


# ============================================================
# 10. IMPORTING A SPECIFIC FUNCTION
# ============================================================

# Instead of importing the entire module,
# we can import one specific function.

from random import randint

number = randint(1, 10)

print(number)


# Notice that we don't need:

# random.randint()

# We can just use:

# randint()


# ============================================================
# 11. IMPORTING MULTIPLE FUNCTIONS
# ============================================================

from random import randint, choice

number = randint(1, 100)

colors = [
    "Red",
    "Blue",
    "Green"
]

color = choice(colors)

print(number)
print(color)


# ============================================================
# 12. IMPORTING EVERYTHING
# ============================================================

# You may sometimes see:

# from random import *

# This imports everything from the module.

# However, this is generally NOT recommended.

# It is better to be specific about what you are importing.


# ============================================================
# 13. IMPORTING WITH AN ALIAS
# ============================================================

import math as m

print(m.sqrt(25))
print(m.pi)

# "m" is now another name for the math module.


# Another example:

import random as r

number = r.randint(1, 10)

print(number)


# ============================================================
# 14. IMPORTING YOUR OWN FILE
# ============================================================

# You can also create your own modules.

# Imagine you have a file called:

# helpers.py


# Inside helpers.py:

def say_hello():
    print("Hello!")


# Then another Python file could use:

# import helpers

# helpers.say_hello()


# ============================================================
# 15. IMPORTS + FUNCTIONS
# ============================================================

import random

def roll_dice():
    number = random.randint(1, 6)
    return number


roll = roll_dice()

print("You rolled:", roll)


# ============================================================
# 16. IMPORTS + LISTS
# ============================================================

import random

items = [
    "Sword",
    "Shield",
    "Potion",
    "Bow"
]

random_item = random.choice(items)

print("You found:", random_item)


# ============================================================
# 17. IMPORTS + INPUT
# ============================================================

import random

name = input("What is your name? ")

number = random.randint(1, 10)

print(name, "your random number is", number)


# ============================================================
# 18. IMPORTS + LOOPS
# ============================================================

import random

for i in range(5):
    number = random.randint(1, 10)
    print(number)


# This generates 5 random numbers.


# ============================================================
# 19. IMPORTS + WHILE LOOPS
# ============================================================

import random

number = random.randint(1, 10)

guess = 0

while guess != number:

    guess = int(input("Guess the number: "))

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("You got it!")


# ============================================================
# 20. IMPORTS + FUNCTIONS + LOOPS
# ============================================================

import random


def guessing_game():

    number = random.randint(1, 10)

    guess = 0

    while guess != number:

        guess = int(input("Guess the number: "))

        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print("You won!")


guessing_game()


# ============================================================
# 21. WHY USE IMPORTS?
# ============================================================

# Imports allow us to reuse code.

# Instead of writing our own random-number system,
# we can use Python's random module.

# Instead of calculating square roots ourselves,
# we can use math.sqrt().


# ============================================================
# 22. COMMON BUILT-IN MODULES
# ============================================================

# random
# Useful for:
# - Random numbers
# - Random choices
# - Games

# math
# Useful for:
# - Square roots
# - Pi
# - Rounding
# - Mathematical calculations

# time
# Useful for:
# - Delays
# - Timing programs

# os
# Useful for:
# - Working with files and folders
# - Operating system information


# ============================================================
# 23. IMPORTANT VOCABULARY
# ============================================================

# IMPORT
# Loads code from another module.

# MODULE
# A Python file containing reusable code.

# LIBRARY
# A collection of reusable code and modules.

# FUNCTION
# A reusable piece of code that performs a task.

# ALIAS
# Another name for an imported module.

# Example:

# import math as m


# ============================================================
# 24. QUICK REFERENCE
# ============================================================

# Import an entire module:

# import random

# Use a function:

# random.randint(1, 10)


# Import a specific function:

# from random import randint

# Use it:

# randint(1, 10)


# Import multiple functions:

# from random import randint, choice


# Import with an alias:

# import math as m

# Use it:

# m.sqrt(25)


# ============================================================
# 25. THE BIG IDEA
# ============================================================

# IMPORTS LET YOU USE CODE THAT ALREADY EXISTS.

# You don't have to write everything yourself.

# Python gives you many useful modules,
# and you can eventually create your own modules too.


# ============================================================
#                      SUMMARY
# ============================================================

# import random
# import math
# from random import randint
# import math as m

# random.randint(1, 10)
# random.choice(list)

# math.sqrt(25)
# math.pi
# math.ceil(4.2)
# math.floor(4.8)

# Imports become especially powerful when combined with:
#
# - Functions
# - Lists
# - Dictionaries
# - Loops
# - If statements
# - Input
#
# Next project:
#
# NUMBER GUESSING GAME
#
# Use random + functions + while loops + if statements.
# ============================================================