# ============================================================
#                    CLASSES PRACTICE
# ============================================================
# RULES:
# - Try each challenge yourself.
# - Don't look at the solution until you've tried it.
# - Test your code after each challenge.
# ============================================================


# ============================================================
# CHALLENGE 1 - CREATE A CLASS
# ============================================================
# Create a class called Dog.
#
# For now, put:
#
#     pass
#
# inside the class.
#
# Then create an object called dog1.


# ============================================================
# CHALLENGE 2 - DOG NAME
# ============================================================
# Create a Dog class.
#
# __init__ should accept a name.
#
# Store the name using:
#
# self.name
#
# Create a dog called Max.
#
# Print the dog's name.
#
# Expected:
#
# Max


# ============================================================
# CHALLENGE 3 - MULTIPLE DOGS
# ============================================================
# Create two Dog objects.
#
# Dog 1:
# Name: Max
#
# Dog 2:
# Name: Buddy
#
# Print both names.


# ============================================================
# CHALLENGE 4 - DOG AGE
# ============================================================
# Add an age attribute to the Dog class.
#
# Create:
#
# Max - 5 years old
# Buddy - 3 years old
#
# Print their names and ages.
#
# Example:
#
# Max is 5 years old.
# Buddy is 3 years old.


# ============================================================
# CHALLENGE 5 - DOG METHOD
# ============================================================
# Add a method called:
#
# bark()
#
# It should print:
#
# "Woof!"
#
# Create a Dog object and call:
#
# dog.bark()


# ============================================================
# CHALLENGE 6 - DOG INTRODUCTION
# ============================================================
# Create a method called:
#
# introduce()
#
# It should print:
#
# "My name is Max and I am 5 years old."
#
# Use self.name and self.age.


# ============================================================
# CHALLENGE 7 - STUDENT
# ============================================================
# Create a Student class.
#
# The student should have:
#
# name
# age
# grade
#
# Create:
#
# Ben
# 12
# 7
#
# Print all three attributes.


# ============================================================
# CHALLENGE 8 - STUDENT METHOD
# ============================================================
# Add this method:
#
# introduce()
#
# It should print something like:
#
# "My name is Ben and I am in grade 7."
#
# Create a Student object and call the method.


# ============================================================
# CHALLENGE 9 - STUDENT GRADE
# ============================================================
# Add a grade attribute to Student.
#
# Create a method:
#
# check_grade()
#
# If the grade is >= 60:
#
#     print("Passing!")
#
# Otherwise:
#
#     print("Failing!")
#
# Test it with different grades.


# ============================================================
# CHALLENGE 10 - BANK ACCOUNT
# ============================================================
# Create a BankAccount class.
#
# It should have:
#
# owner
# balance
#
# Example:
#
# account = BankAccount("Ben", 100)
#
# Print:
#
# Owner: Ben
# Balance: 100


# ============================================================
# CHALLENGE 11 - DEPOSIT
# ============================================================
# Add this method:
#
# deposit(amount)
#
# It should add money to the balance.
#
# Example:
#
# account.deposit(50)
#
# The balance should become 150.


# ============================================================
# CHALLENGE 12 - WITHDRAW
# ============================================================
# Add:
#
# withdraw(amount)
#
# If the account has enough money:
#
#     subtract the money
#
# Otherwise:
#
#     print("Not enough money!")
#
# Test both situations.


# ============================================================
# CHALLENGE 13 - GAME CHARACTER
# ============================================================
# Create a Character class.
#
# It should have:
#
# name
# health
# level
# gold
#
# Example:
#
# Hero
# 100 health
# level 1
# 50 gold


# ============================================================
# CHALLENGE 14 - TAKE DAMAGE
# ============================================================
# Add:
#
# take_damage(damage)
#
# Subtract damage from health.
#
# Example:
#
# hero.take_damage(25)
#
# Health should become 75.


# ============================================================
# CHALLENGE 15 - HEAL
# ============================================================
# Add:
#
# heal(amount)
#
# Increase health by the amount.
#
# Example:
#
# hero.heal(20)


# ============================================================
# CHALLENGE 16 - LEVEL UP
# ============================================================
# Add:
#
# level_up()
#
# Increase the character's level by 1.
#
# Example:
#
# Level 1
#
# hero.level_up()
#
# Level 2


# ============================================================
# CHALLENGE 17 - INVENTORY
# ============================================================
# Add an inventory list to Character.
#
# Every new character should start with:
#
# []
#
# Add this method:
#
# add_item(item)
#
# It should add the item to the inventory.
#
# Example:
#
# hero.add_item("Sword")
# hero.add_item("Potion")
#
# Print the inventory.


# ============================================================
# CHALLENGE 18 - SHOW CHARACTER
# ============================================================
# Create a method:
#
# show_character()
#
# It should print:
#
# ===== CHARACTER =====
# Name: Hero
# Health: 100
# Level: 1
# Gold: 50
#
# Inventory:
# - Sword
# - Potion
#
# Use a for loop to display the inventory.


# ============================================================
# CHALLENGE 19 - IS ALIVE
# ============================================================
# Create:
#
# is_alive()
#
# If health is greater than 0:
#
#     return True
#
# Otherwise:
#
#     return False
#
# Test the method with different health values.


# ============================================================
# CHALLENGE 20 - TWO CHARACTERS
# ============================================================
# Create two Character objects.
#
# hero = Character("Hero", 100, 1, 50)
#
# wizard = Character("Wizard", 80, 2, 100)
#
# Give them different inventories.
#
# Print both characters.


# ============================================================
# CHALLENGE 21 - BATTLE
# ============================================================
# Create two Character objects.
#
# Have one character attack the other.
#
# For example:
#
# hero.attack(wizard)
#
# Create an attack() method.
#
# The attack method should:
#
# 1. Deal 20 damage.
# 2. Reduce the other character's health.
# 3. Print what happened.
#
# Example:
#
# Hero attacks Wizard!
# Wizard has 60 health remaining.


# ============================================================
# CHALLENGE 22 - RETURN A VALUE
# ============================================================
# Create a method called:
#
# get_health()
#
# It should return the character's health.
#
# Example:
#
# health = hero.get_health()
#
# print(health)


# ============================================================
# CHALLENGE 23 - LIST OF CHARACTERS
# ============================================================
# Create three Character objects.
#
# Put them into a list:
#
# characters = []
#
# Use a for loop to display:
#
# Name
# Health
# Level
#
# for character in characters:
#     ...


# ============================================================
# CHALLENGE 24 - PLAYER SEARCH
# ============================================================
# Create three Character objects.
#
# Put them into a list.
#
# Ask the user:
#
# "Which character do you want to find?"
#
# Loop through the characters.
#
# If the name matches:
#
#     print the character's information.
#
# Otherwise:
#
#     print("Character not found.")


# ============================================================
# FINAL CHALLENGE - MINI RPG
# ============================================================
#
# Build a small RPG using classes.
#
# Create a Character class with:
#
# Attributes:
# - name
# - health
# - level
# - gold
# - inventory
#
# Methods:
# - show_character()
# - take_damage()
# - heal()
# - level_up()
# - add_item()
# - is_alive()
# - attack()
#
#
# Create:
#
# hero = Character("Hero", 100, 1, 50)
#
# enemy = Character("Goblin", 60, 1, 20)
#
#
# The game should:
#
# 1. Show the hero.
#
# 2. Show the enemy.
#
# 3. Let the hero attack the enemy.
#
# 4. Reduce the enemy's health.
#
# 5. Let the enemy attack the hero.
#
# 6. Continue until one character is defeated.
#
# 7. Print the winner.
#
#
# BONUS:
#
# Add an inventory.
#
# Add a Potion.
#
# Let the player choose:
#
# 1. Attack
# 2. Heal
# 3. View Character
# 4. Quit
#
# Use a while loop for the game.
# ============================================================