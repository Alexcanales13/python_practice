# ============================================================
#                  PYTHON FUNCTIONS NOTES
# ============================================================

# ============================================================
# 1. WHAT IS A FUNCTION?
# ============================================================

# A function is a reusable block of code that performs a task.

# Instead of writing the same code over and over,
# we can put it inside a function and use it whenever
# we need it.


# ============================================================
# 2. CREATING A FUNCTION
# ============================================================

# We create a function using the "def" keyword.

def say_hello():
    print("Hello!")
    print("Welcome to Python!")


# IMPORTANT:
# Creating a function does NOT automatically run it.


# ============================================================
# 3. CALLING A FUNCTION
# ============================================================

# To run a function, we call it by its name:

say_hello()

# Output:
# Hello!
# Welcome to Python!


# ============================================================
# 4. WHY USE FUNCTIONS?
# ============================================================

# Without a function:

print("Hello!")
print("Welcome to Python!")

print("Hello!")
print("Welcome to Python!")

print("Hello!")
print("Welcome to Python!")


# With a function:

def welcome():
    print("Hello!")
    print("Welcome to Python!")


welcome()
welcome()
welcome()

# Functions help us:
#
# - Reuse code
# - Keep programs organized
# - Avoid repeating code
# - Make large programs easier to understand


# ============================================================
# 5. FUNCTIONS WITH PARAMETERS
# ============================================================

# A parameter allows us to give information to a function.

def greet(name):
    print("Hello", name)


greet("Ben")
greet("Alex")
greet("Sam")

# "name" is the parameter.
#
# "Ben", "Alex", and "Sam" are arguments.


# ============================================================
# 6. MULTIPLE PARAMETERS
# ============================================================

def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old")


introduce("Ben", 12)
introduce("Alex", 13)


# ============================================================
# 7. FUNCTIONS WITH NUMBERS
# ============================================================

def add_numbers(a, b):
    print(a + b)


add_numbers(5, 3)
add_numbers(10, 20)


# ============================================================
# 8. RETURN
# ============================================================

# A function can RETURN a value.

def add(a, b):
    return a + b


result = add(5, 3)

print(result)

# The function sends 8 back to the program.
#
# result now contains:
#
# 8


# ============================================================
# 9. PRINT VS RETURN
# ============================================================

# PRINT displays something:

def add_print(a, b):
    print(a + b)


# RETURN sends a value back:

def add_return(a, b):
    return a + b


# This displays the answer:

add_print(5, 3)


# This stores the answer:

answer = add_return(5, 3)

print(answer)


# ============================================================
# 10. RETURNING DIFFERENT VALUES
# ============================================================

def check_age(age):

    if age >= 13:
        return "Teenager"
    else:
        return "Child"


result = check_age(12)

print(result)


# ============================================================
# 11. FUNCTIONS WITH IF STATEMENTS
# ============================================================

def check_health(health):

    if health <= 0:
        return "GAME OVER!"
    else:
        return "Keep playing!"


print(check_health(100))
print(check_health(0))


# ============================================================
# 12. FUNCTIONS WITH LISTS
# ============================================================

def show_tasks(tasks):

    for task in tasks:
        print(task)


tasks = [
    "Math homework",
    "Walk the dog",
    "Study Python"
]

show_tasks(tasks)


# ============================================================
# 13. FUNCTIONS WITH DICTIONARIES
# ============================================================

player = {
    "name": "Hero",
    "health": 100,
    "level": 5,
    "gold": 200
}


def show_player(player):

    print("Name:", player["name"])
    print("Health:", player["health"])
    print("Level:", player["level"])
    print("Gold:", player["gold"])


show_player(player)


# ============================================================
# 14. CHANGING A DICTIONARY INSIDE A FUNCTION
# ============================================================

def level_up(player):

    player["level"] = player["level"] + 1


level_up(player)

print(player)


# ============================================================
# 15. FUNCTION WITH A PARAMETER AND RETURN
# ============================================================

def calculate_damage(attack, defense):

    damage = attack - defense

    return damage


damage = calculate_damage(50, 20)

print("Damage:", damage)


# ============================================================
# 16. FUNCTIONS CAN HAVE MULTIPLE STEPS
# ============================================================

def attack(player, enemy_health):

    damage = player["level"] * 10

    enemy_health = enemy_health - damage

    return enemy_health


enemy_health = 100

enemy_health = attack(player, enemy_health)

print("Enemy health:", enemy_health)


# ============================================================
# 17. FUNCTION PARAMETERS CAN BE DIFFERENT TYPES
# ============================================================

# A parameter can be:
#
# - String
# - Integer
# - Float
# - List
# - Dictionary
# - Boolean
# - etc.


def show_name(name):
    print(name)


def show_number(number):
    print(number)


def show_list(items):
    print(items)


def show_dictionary(data):
    print(data)


show_name("Ben")
show_number(12)
show_list(["Apple", "Banana", "Orange"])
show_dictionary({"name": "Ben", "age": 12})


# ============================================================
# 18. FUNCTIONS CAN RETURN DIFFERENT TYPES
# ============================================================

def get_name():
    return "Ben"


def get_score():
    return 95


def get_items():
    return ["Sword", "Shield", "Potion"]


def get_player():
    return {
        "name": "Hero",
        "health": 100
    }


name = get_name()
score = get_score()
items = get_items()
player_data = get_player()

print(name)
print(score)
print(items)
print(player_data)


# ============================================================
# 19. DEFAULT PARAMETERS
# ============================================================

# A parameter can have a default value.

def greet(name="Player"):
    print("Hello", name)


greet("Ben")
greet()

# The second call uses "Player" because no argument
# was provided.


# ============================================================
# 20. A FUNCTION CAN CALL ANOTHER FUNCTION
# ============================================================

def start_game():
    print("Starting game...")


def game_menu():
    start_game()
    print("1. Play")
    print("2. Quit")


game_menu()


# ============================================================
# 21. FUNCTIONS + INPUT
# ============================================================

def greet_user(name):
    print("Hello", name)


name = input("What is your name? ")

greet_user(name)


# ============================================================
# 22. FUNCTIONS + INPUT + RETURN
# ============================================================

def get_age():

    age = int(input("How old are you? "))

    return age


age = get_age()

print("You are", age, "years old.")


# ============================================================
# 23. IMPORTANT VOCABULARY
# ============================================================

# def
# Used to create a function.
#
# parameter
# A variable listed inside the function's parentheses.
#
# argument
# The actual value passed into a function.
#
# call
# Running a function.
#
# return
# Sends a value back from the function.


# Example:

def multiply(a, b):
    return a * b


answer = multiply(5, 4)

# "def"       -> creates the function
# "a, b"      -> parameters
# "5, 4"      -> arguments
# "multiply()" -> function call
# "return"    -> sends the answer back


# ============================================================
# 24. QUICK REFERENCE
# ============================================================

# Basic function:

def hello():
    print("Hello!")


# Function with a parameter:

def hello(name):
    print("Hello", name)


# Function with multiple parameters:

def add(a, b):
    return a + b


# Function with an if statement:

def check_score(score):

    if score >= 60:
        return "PASS"
    else:
        return "FAIL"


# Function with a list:

def show_items(items):

    for item in items:
        print(item)


# Function with a dictionary:

def show_player(player):

    print(player["name"])
    print(player["health"])


# ============================================================
# SUMMARY
# ============================================================

# Functions allow us to:
#
# 1. Create reusable code.
# 2. Give functions information using parameters.
# 3. Get information back using return.
# 4. Use if statements inside functions.
# 5. Use loops inside functions.
# 6. Use lists inside functions.
# 7. Use dictionaries inside functions.
# 8. Build larger programs using smaller pieces of code.
#
# The basic pattern is:
#
# def function_name(parameters):
#     code
#     return value
#
# Then call it:
#
# function_name(arguments)