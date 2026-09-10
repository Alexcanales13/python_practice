# ============================================================
#              DICTIONARY PRACTICE 2
# ============================================================

# CHALLENGE 1 - Create a Dictionary
# Create a dictionary called pet with:
# name
# animal
# age
# color
#
# Print the entire dictionary.


# CHALLENGE 2 - Access Values
# Print just the pet's:
# name
# animal
# age
# color


# CHALLENGE 3 - Change Values
# Change the pet's age.
# Change the pet's color.
#
# Print the dictionary afterward.


# CHALLENGE 4 - Add Information
# Add these new keys:
# favorite_food
# favorite_toy
#
# Print the dictionary.


# CHALLENGE 5 - Check for a Key
# Ask the user for a key:
#
# "What information do you want to check? "
#
# If the key exists, print:
# "That information exists!"
#
# Otherwise print:
# "That information does not exist."


# CHALLENGE 6 - Loop Through a Dictionary
# Create this dictionary:

player = {
    "name": "Alex",
    "level": 10,
    "health": 100,
    "gold": 250,
    "weapon": "Sword"
}

# Use a for loop to print every key and value.
#
# Example:
# name : Alex
# level : 10
# health : 100


# CHALLENGE 7 - Update Player Stats
# Using the player dictionary:
#
# - Increase the level by 1
# - Add 50 gold
# - Change health to 80
# - Change the weapon to "Magic Sword"
#
# Print the updated player.


# CHALLENGE 8 - Inventory Dictionary
# Create a dictionary called inventory:

inventory = {
    "Potion": 3,
    "Sword": 1,
    "Shield": 1,
    "Arrow": 25
}

# Use a for loop to print each item and how many
# the player has.
#
# Example:
# Potion : 3


# CHALLENGE 9 - Check Inventory
# Ask the user:
#
# "What item are you looking for? "
#
# Check if the item exists in the inventory.
#
# If it exists, print how many the player has.
#
# Otherwise print:
# "You don't have that item."


# CHALLENGE 10 - Dictionary + If Statement
# Create this dictionary:

scores = {
    "Alex": 85,
    "Jamie": 92,
    "Sam": 55,
    "Taylor": 73
}

# Loop through the dictionary.
#
# If the score is 60 or higher:
#     print the name and "PASS"
#
# Otherwise:
#     print the name and "FAIL"


# CHALLENGE 11 - Find the Highest Score
# Using the scores dictionary above:
#
# Find the highest score WITHOUT using max().
#
# Hint:
# Create a variable called highest_score.
# Start it at 0.
#
# Then use a for loop and an if statement.


# CHALLENGE 12 - Count Players
# Using the scores dictionary:
#
# Print how many players are in the dictionary.
#
# Hint:
# You can use len().


# CHALLENGE 13 - User Input Dictionary
# Create an empty dictionary called friends.
#
# Ask the user for the names of 3 friends.
# Ask for each friend's favorite game.
#
# Store the information like:
#
# friends = {
#     "Alex": "Minecraft",
#     "Sam": "Fortnite"
# }
#
# Finally, loop through the dictionary and print
# each friend's name and favorite game.


# ============================================================
# FINAL CHALLENGE - RPG CHARACTER
# ============================================================

# Create a dictionary called character with:
#
# name
# level
# health
# gold
# weapon
# inventory
#
# The inventory should be a LIST inside the dictionary.
#
# Example:
#
# character = {
#     "name": "Dragon Slayer",
#     "level": 5,
#     "health": 100,
#     "gold": 200,
#     "weapon": "Sword",
#     "inventory": ["Potion", "Shield", "Key"]
# }


# Your program should:
#
# 1. Print the character's information.
#
# 2. Use a for loop to print the inventory.
#
# 3. Increase the character's level.
#
# 4. Add 100 gold.
#
# 5. Change the weapon.
#
# 6. Add an item to the inventory.
#
# 7. Remove an item from the inventory.
#
# 8. Check if the character has a "Potion".
#
# 9. Check the character's health.
#
# If health is 0 or less:
#     print "GAME OVER!"
#
# Otherwise:
#     print "The adventure continues!"
#
# 10. Print the final character information.


# ============================================================
# BONUS CHALLENGE
# ============================================================

# Create a dictionary of 5 students and their grades.
#
# Example:
#
# grades = {
#     "Alex": 85,
#     "Jamie": 92,
#     "Sam": 78,
#     "Taylor": 95,
#     "Jordan": 88
# }
#
# Find:
# - The highest grade
# - The lowest grade
# - How many students passed
#
# Do NOT use max() or min().
#
# Use for loops and if statements.