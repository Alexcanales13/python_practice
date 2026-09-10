# ============================================================
#              DICTIONARY PRACTICE
# ============================================================
#
# Try to solve every challenge yourself.
#
# Do not look for the solution until you have tried!
#
# ============================================================


# ------------------------------------------------------------
# CHALLENGE 1 - CREATE A DICTIONARY
# ------------------------------------------------------------

# Create a dictionary called student.

# It should contain:
#
# name
# age
# favorite_food
# favorite_color

# Give each key a value.


# ------------------------------------------------------------
# CHALLENGE 2 - ACCESS VALUES
# ------------------------------------------------------------

# Print the student's:
#
# name
# age
# favorite_food
# favorite_color

# Use the dictionary keys to access the values.


# ------------------------------------------------------------
# CHALLENGE 3 - CHANGE VALUES
# ------------------------------------------------------------

# Change the student's favorite food.

# Change their favorite color.

# Print the dictionary afterward.


# ------------------------------------------------------------
# CHALLENGE 4 - ADD INFORMATION
# ------------------------------------------------------------

# Add these new keys:
#
# favorite_game
# favorite_animal

# Give them your own values.


# ------------------------------------------------------------
# CHALLENGE 5 - REMOVE INFORMATION
# ------------------------------------------------------------

# Remove favorite_animal from the dictionary.

# Print the dictionary afterward.


# ------------------------------------------------------------
# CHALLENGE 6 - CHECK FOR A KEY
# ------------------------------------------------------------

# Check whether "age" exists in the dictionary.

# If it does:
#
# "Age exists!"


# ------------------------------------------------------------
# CHALLENGE 7 - LOOP THROUGH A DICTIONARY
# ------------------------------------------------------------

person = {
    "name": "Alex",
    "age": 12,
    "city": "Bridgeport",
    "hobby": "Gaming"
}

# Use a FOR LOOP to print:

# name : Alex
# age : 12
# city : Bridgeport
# hobby : Gaming


# ------------------------------------------------------------
# CHALLENGE 8 - GAME CHARACTER
# ------------------------------------------------------------

player = {
    "name": "Hero",
    "health": 100,
    "gold": 50,
    "weapon": "Sword"
}

# Print the player's information.

# Then:
#
# Change health to 75.
#
# Add a new key called "armor".
#
# Give armor a value.
#
# Add 25 gold to the player's gold.
#
# Print the final player information.


# ------------------------------------------------------------
# CHALLENGE 9 - STUDENT GRADES
# ------------------------------------------------------------

grades = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 95
}

# Use a FOR LOOP to print each subject and grade.

# Example:
#
# Math: 85
# Science: 92


# ------------------------------------------------------------
# CHALLENGE 10 - PASS OR FAIL
# ------------------------------------------------------------

# Using the grades dictionary above:

# Loop through every subject.

# If the grade is 60 or higher:
#
# "Math: PASS"
#
# Otherwise:
#
# "Math: FAIL"


# ------------------------------------------------------------
# CHALLENGE 11 - USER INPUT
# ------------------------------------------------------------

# Create an empty dictionary called favorite_foods.

# Ask 3 people for:
#
# Their name
# Their favorite food
#
# Store the information in the dictionary.
#
# Example:
#
# Alex -> Pizza
# Sarah -> Tacos
# Mike -> Burgers
#
# Then use a FOR LOOP to print everyone's
# favorite food.


# ------------------------------------------------------------
# CHALLENGE 12 - DICTIONARY + LIST
# ------------------------------------------------------------

# Create a dictionary representing a video game.

# It should contain:
#
# name
# genre
# rating
# characters
#
# "characters" should be a LIST.
#
# Example:
#
# game = {
#     "name": "Minecraft",
#     "genre": "Adventure",
#     "rating": 10,
#     "characters": ["Steve", "Alex"]
# }
#
# Use a FOR LOOP to print every character.


# ============================================================
#                    FINAL CHALLENGE
# ============================================================

# Create a dictionary for your own video game character.
#
# Include at least:
#
# name
# health
# level
# gold
# weapon
# inventory
#
# inventory should be a LIST.
#
# Example:
#
# character = {
#     "name": "Dragon Slayer",
#     "health": 100,
#     "level": 5,
#     "gold": 250,
#     "weapon": "Sword",
#     "inventory": ["Potion", "Shield", "Key"]
# }
#
# Then:
#
# 1. Print the character's information.
#
# 2. Use a FOR LOOP to print the inventory.
#
# 3. Change the character's health.
#
# 4. Add an item to the inventory.
#
# 5. Remove an item from the inventory.
#
# 6. Check whether the character has a Potion.
#
# 7. If health is 0 or less, print "GAME OVER!"
#
# 8. Otherwise, print "The adventure continues!"
#
# ============================================================
#                     BONUS
# ============================================================
#
# Find the highest grade from the grades dictionary
# WITHOUT using max().
#
# Hint:
# You will need a variable to keep track of the
# highest grade while using a FOR LOOP.
#
# ============================================================