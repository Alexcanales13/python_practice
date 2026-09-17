# ============================================================
#                 PYTHON FUNCTIONS PRACTICE
# ============================================================

# Instructions:
# Complete each challenge.
# Try to write the function yourself before looking for help.


# ============================================================
# 1. CREATE YOUR FIRST FUNCTION
# ============================================================

# Create a function called say_hello().
# It should print:
# Hello!
# Welcome to Python!


# ============================================================
# 2. FUNCTION WITH A PARAMETER
# ============================================================

# Create a function called greet_user(name).
# It should print:
# Hello, [name]!

# Example:
# greet_user("Ben")
# Output:
# Hello, Ben!


# ============================================================
# 3. FUNCTION WITH TWO PARAMETERS
# ============================================================

# Create a function called introduce(name, age).
# It should print:
# My name is [name]
# I am [age] years old

# Example:
# introduce("Ben", 12)


# ============================================================
# 4. FUNCTION THAT ADDS NUMBERS
# ============================================================

# Create a function called add_numbers(a, b).
# It should return the sum of a and b.

# Example:
# result = add_numbers(5, 3)
# print(result)
# Output:
# 8


# ============================================================
# 5. FUNCTION THAT CHECKS A NUMBER
# ============================================================

# Create a function called check_number(number).
#
# If the number is greater than 0, return:
# "Positive"
#
# If the number is less than 0, return:
# "Negative"
#
# Otherwise, return:
# "Zero"

# Example:
# print(check_number(-5))
# Output:
# Negative


# ============================================================
# 6. FUNCTION THAT CHECKS EVEN OR ODD
# ============================================================

# Create a function called even_or_odd(number).
#
# If the number is even, return:
# "Even"
#
# Otherwise, return:
# "Odd"
#
# Hint:
# A number is even when number % 2 == 0.

# Example:
# print(even_or_odd(8))
# Output:
# Even


# ============================================================
# 7. FUNCTION THAT CALCULATES DAMAGE
# ============================================================

# Create a function called calculate_damage(attack, defense).
#
# Damage should equal:
# attack - defense
#
# Return the damage.

# Example:
# damage = calculate_damage(50, 20)
# print("Damage:", damage)
# Output:
# Damage: 30


# ============================================================
# 8. FUNCTION THAT CHECKS HEALTH
# ============================================================

# Create a function called check_health(health).
#
# If health is less than or equal to 0, return:
# "GAME OVER!"
#
# Otherwise, return:
# "Keep playing!"

# Example:
# print(check_health(100))
# Output:
# Keep playing!


# ============================================================
# 9. FUNCTION THAT PRINTS A LIST
# ============================================================

# Create a function called show_items(items).
#
# The function should loop through the list
# and print each item.

# Example:
# items = ["Sword", "Shield", "Potion"]
# show_items(items)

# Expected output:
# Sword
# Shield
# Potion


# ============================================================
# 10. FUNCTION THAT COUNTS ITEMS
# ============================================================

# Create a function called count_items(items).
#
# It should return how many items are in the list.
#
# Hint:
# Use len().

# Example:
# items = ["Sword", "Shield", "Potion"]
# print(count_items(items))
# Output:
# 3


# ============================================================
# 11. FUNCTION THAT CHECKS AN INVENTORY
# ============================================================

# Create a function called has_item(inventory, item).
#
# If the item is in the inventory, return:
# True
#
# Otherwise, return:
# False

# Example:
# inventory = ["Sword", "Shield", "Potion"]
# print(has_item(inventory, "Potion"))
# Output:
# True


# ============================================================
# 12. FUNCTION THAT ADDS AN ITEM
# ============================================================

# Create a function called add_item(inventory, item).
#
# The function should add the item to the inventory
# using append().
#
# Test the function by printing the inventory afterward.

# Example:
# inventory = ["Sword", "Shield"]
# add_item(inventory, "Potion")
# print(inventory)
# Output:
# ["Sword", "Shield", "Potion"]


# ============================================================
# 13. FUNCTION WITH A DICTIONARY
# ============================================================

# Create a function called show_player(player).
#
# The player dictionary contains:
# name
# health
# level
# gold
#
# Print each value with a label.

# Example:
# player = {
#     "name": "Hero",
#     "health": 100,
#     "level": 5,
#     "gold": 200
# }
#
# show_player(player)


# ============================================================
# 14. FUNCTION THAT CHANGES A DICTIONARY
# ============================================================

# Create a function called level_up(player).
#
# Increase the player's level by 1.
#
# Example:
# player = {
#     "name": "Hero",
#     "level": 5
# }
#
# level_up(player)
# print(player)
#
# Expected result:
# {"name": "Hero", "level": 6}


# ============================================================
# 15. FUNCTION THAT ADDS GOLD
# ============================================================

# Create a function called add_gold(player, amount).
#
# Add amount to the player's gold.

# Example:
# player = {
#     "name": "Hero",
#     "gold": 100
# }
#
# add_gold(player, 50)
# print(player)
#
# Expected result:
# {"name": "Hero", "gold": 150}


# ============================================================
# 16. FUNCTION THAT RETURNS A PLAYER STATUS
# ============================================================

# Create a function called player_status(player).
#
# If the player's health is less than or equal to 0,
# return "Defeated".
#
# Otherwise, return "Alive".

# Example:
# player = {
#     "name": "Hero",
#     "health": 75
# }
#
# print(player_status(player))
# Output:
# Alive


# ============================================================
# 17. FUNCTION WITH INPUT
# ============================================================

# Create a function called ask_name().
#
# The function should ask the user:
# What is your name?
#
# Return the name entered by the user.
#
# Then call the function and print the result.


# ============================================================
# 18. FUNCTION WITH INPUT AND NUMBERS
# ============================================================

# Create a function called ask_age().
#
# The function should ask:
# How old are you?
#
# Convert the answer into an integer.
# Return the age.
#
# Then call the function and print:
# You are [age] years old.


# ============================================================
# 19. FUNCTION THAT RETURNS A DISCOUNTED PRICE
# ============================================================

# Create a function called discounted_price(price, discount).
#
# Calculate the discount:
# price * discount / 100
#
# Subtract the discount from the original price.
#
# Return the final price.

# Example:
# print(discounted_price(100, 20))
# Output:
# 80.0


# ============================================================
# 20. FINAL CHALLENGE: MINI RPG
# ============================================================

# Create a player dictionary:

player = {
    "name": "Hero",
    "health": 100,
    "gold": 50,
    "level": 1,
    "inventory": ["Sword", "Potion"]
}

# Create these functions:
#
# 1. show_character(player)
#    Prints the player's information.
#
# 2. heal_player(player)
#    Adds 20 health.
#
# 3. find_treasure(player)
#    Adds 100 gold.
#
# 4. add_inventory_item(player, item)
#    Adds an item to the player's inventory.
#
# 5. level_up(player)
#    Increases the player's level by 1.
#
# 6. is_alive(player)
#    Returns True if health is greater than 0.
#    Otherwise, returns False.
#
# Test every function.


# ============================================================
# BONUS CHALLENGE
# ============================================================

# Create a function called buy_item(player, item, price).
#
# If the player has enough gold:
# - Subtract the price from the player's gold.
# - Add the item to the player's inventory.
# - Print "Item purchased!"
#
# Otherwise:
# - Print "Not enough gold!"