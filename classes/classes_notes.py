# ============================================================
#                    PYTHON CLASSES
# ============================================================

# A class lets us create our own types of objects.
#
# We have already used built-in types:
#
# str
# int
# list
# dict
#
# Now we can create our own types.


# ============================================================
# 1. WHAT IS A CLASS?
# ============================================================

# Imagine we want to represent a player in a game.
#
# A player has information:
#
# name
# health
# level
# gold
#
# A player can also do things:
#
# attack
# heal
# level up
#
# A class lets us put all of this together.


# ============================================================
# 2. CREATING A CLASS
# ============================================================

class Player:
    pass


# "class" creates a class.
#
# Player is the name of our class.
#
# pass means:
#
# "There is nothing inside this class yet."


# ============================================================
# 3. CREATING AN OBJECT
# ============================================================

class Player:
    pass


player1 = Player()

print(player1)


# Player is the class.
#
# player1 is an object created from that class.
#
# Think of it like:
#
# Class = blueprint
# Object = thing created from the blueprint


# ============================================================
# 4. MULTIPLE OBJECTS
# ============================================================

class Player:
    pass


player1 = Player()
player2 = Player()
player3 = Player()

print(player1)
print(player2)
print(player3)


# All three objects were created from the same class.


# ============================================================
# 5. __init__()
# ============================================================

# __init__ is a special method.
#
# It runs automatically when we create an object.


class Player:

    def __init__(self):
        print("A player was created!")


player1 = Player()
player2 = Player()


# Output:
#
# A player was created!
# A player was created!


# ============================================================
# 6. SELF
# ============================================================

# self refers to the specific object
# that is using the method.


class Player:

    def __init__(self):
        print("Player created")


player1 = Player()
player2 = Player()


# When we create player1:
#
# self refers to player1.
#
# When we create player2:
#
# self refers to player2.


# ============================================================
# 7. ATTRIBUTES
# ============================================================

# Attributes are pieces of information
# stored inside an object.


class Player:

    def __init__(self):
        self.name = "Hero"
        self.health = 100
        self.level = 1


player1 = Player()

print(player1.name)
print(player1.health)
print(player1.level)


# ============================================================
# 8. DIFFERENT OBJECTS CAN HAVE DIFFERENT VALUES
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health


player1 = Player("Hero", 100)
player2 = Player("Wizard", 80)

print(player1.name)
print(player1.health)

print(player2.name)
print(player2.health)


# player1 and player2 are both Player objects,
# but they contain different information.


# ============================================================
# 9. PARAMETERS IN __init__()
# ============================================================

class Player:

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level


player1 = Player("Hero", 100, 1)

print(player1.name)
print(player1.health)
print(player1.level)


# When we create the object:
#
# Player("Hero", 100, 1)
#
# The values are passed into __init__.


# ============================================================
# 10. UNDERSTANDING self
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health


player1 = Player("Hero", 100)

# This means:
#
# player1.name
# player1.health


# self.name means:
#
# "The name belonging to this particular object."


# ============================================================
# 11. METHODS
# ============================================================

# A function inside a class is called a method.


class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def say_hello(self):
        print("Hello! My name is", self.name)


player1 = Player("Hero", 100)

player1.say_hello()


# Notice:
#
# player1.say_hello()
#
# We use the object to call the method.


# ============================================================
# 12. METHODS CAN CHANGE ATTRIBUTES
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health = self.health - damage


player1 = Player("Hero", 100)

print("Health:", player1.health)

player1.take_damage(25)

print("Health:", player1.health)


# Output:
#
# Health: 100
# Health: 75


# ============================================================
# 13. HEALING
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def heal(self):
        self.health = self.health + 20


player1 = Player("Hero", 50)

print(player1.health)

player1.heal()

print(player1.health)


# ============================================================
# 14. METHODS WITH PARAMETERS
# ============================================================

class Player:

    def __init__(self, name, gold):
        self.name = name
        self.gold = gold

    def add_gold(self, amount):
        self.gold = self.gold + amount


player1 = Player("Hero", 50)

print(player1.gold)

player1.add_gold(100)

print(player1.gold)


# ============================================================
# 15. METHODS THAT RETURN VALUES
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


player1 = Player("Hero", 100)

alive = player1.is_alive()

print(alive)


# ============================================================
# 16. IF STATEMENTS IN METHODS
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):

        self.health = self.health - damage

        if self.health <= 0:
            self.health = 0
            print(self.name, "has been defeated!")

        else:
            print(self.name, "has", self.health, "health remaining.")


player1 = Player("Hero", 100)

player1.take_damage(30)
player1.take_damage(80)


# ============================================================
# 17. LISTS INSIDE CLASSES
# ============================================================

class Player:

    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)


player1 = Player("Hero")

player1.add_item("Sword")
player1.add_item("Potion")

print(player1.inventory)


# ============================================================
# 18. LOOPING THROUGH OBJECT DATA
# ============================================================

class Player:

    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):

        print("Inventory:")

        for item in self.inventory:
            print("-", item)


player1 = Player("Hero")

player1.add_item("Sword")
player1.add_item("Potion")
player1.add_item("Shield")

player1.show_inventory()


# ============================================================
# 19. CHANGING AN ATTRIBUTE DIRECTLY
# ============================================================

class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100


player1 = Player("Hero")

print(player1.health)

player1.health = 75

print(player1.health)


# We can change attributes directly.


# ============================================================
# 20. MULTIPLE PLAYERS
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health


player1 = Player("Hero", 100)
player2 = Player("Wizard", 80)
player3 = Player("Knight", 120)

players = [
    player1,
    player2,
    player3
]

for player in players:

    print(
        player.name,
        player.health
    )


# ============================================================
# 21. CLASSES VS DICTIONARIES
# ============================================================

# Earlier we might represent a player like this:

player = {
    "name": "Hero",
    "health": 100,
    "gold": 50
}


# We could change the values:

player["health"] = player["health"] - 20


# With a class:

class Player:

    def __init__(self, name, health, gold):
        self.name = name
        self.health = health
        self.gold = gold

    def take_damage(self, damage):
        self.health = self.health - damage


player = Player("Hero", 100, 50)

player.take_damage(20)


# The class lets us keep the data
# and the actions together.


# ============================================================
# 22. CLASS + METHOD + RETURN
# ============================================================

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_health(self):
        return self.health


player1 = Player("Hero", 100)

health = player1.get_health()

print("Health:", health)


# ============================================================
# 23. A COMPLETE SIMPLE CLASS
# ============================================================

class Player:

    def __init__(self, name, health, gold):

        self.name = name
        self.health = health
        self.gold = gold
        self.inventory = []

    def show_player(self):

        print("\n===== PLAYER =====")
        print("Name:", self.name)
        print("Health:", self.health)
        print("Gold:", self.gold)

        print("Inventory:")

        for item in self.inventory:
            print("-", item)

    def add_item(self, item):

        self.inventory.append(item)

    def add_gold(self, amount):

        self.gold = self.gold + amount

    def take_damage(self, damage):

        self.health = self.health - damage

    def heal(self, amount):

        self.health = self.health + amount


player1 = Player("Hero", 100, 50)

player1.add_item("Sword")
player1.add_item("Potion")

player1.add_gold(100)

player1.take_damage(25)

player1.heal(10)

player1.show_player()


# ============================================================
# 24. CLASS VOCABULARY
# ============================================================

# CLASS
#
# A blueprint for creating objects.


# OBJECT
#
# An individual thing created from a class.


# INSTANCE
#
# Another word for an object created from a class.


# ATTRIBUTE
#
# Data stored inside an object.
#
# Example:
#
# self.name
# self.health
# self.gold


# METHOD
#
# A function that belongs to a class.
#
# Example:
#
# player.attack()


# __init__
#
# A special method that runs when
# an object is created.


# self
#
# Refers to the current object.


# ============================================================
# 25. THE BIG IDEA
# ============================================================

# BEFORE CLASSES:
#
# Data:
#
# player = {
#     "name": "Hero",
#     "health": 100
# }
#
# Functions:
#
# def heal(player):
#     player["health"] += 20


# WITH CLASSES:
#
# class Player:
#
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def heal(self):
#         self.health += 20
#
#
# player = Player("Hero", 100)
#
# player.heal()


# The data and behavior now belong together.


# ============================================================
# 26. QUICK REFERENCE
# ============================================================

class Example:

    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(self.value)

    def change_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value


example = Example(10)

example.show_value()

example.change_value(20)

print(example.get_value())


# ============================================================
#                       SUMMARY
# ============================================================

# class
# Creates a class.

# __init__
# Runs when an object is created.

# self
# Refers to the current object.

# attribute
# Data stored in an object.

# method
# A function belonging to an object.

# object
# A specific instance created from a class.


# The basic pattern is:
#
# class ClassName:
#
#     def __init__(self, data):
#         self.data = data
#
#     def method(self):
#         # do something
#
#
# object = ClassName(value)
#
# object.method()


# ============================================================
# NEXT:
#
# classes_practice.py
#
# Practice creating:
#
# 1. Dog
# 2. Student
# 3. BankAccount
# 4. GameCharacter
# 5. Inventory
#
# Then build a class-based RPG.
# ============================================================