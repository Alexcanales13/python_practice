# ============================================================
#                  DICTIONARY HOMEWORK
# ============================================================

# RULES:
# - Try to solve each problem yourself.
# - Use dictionaries, for loops, and if statements.
# - Don't use functions yet.
# - Test your code after each challenge.
# ============================================================


# ------------------------------------------------------------
# CHALLENGE 1 - MY FAVORITE THINGS
# ------------------------------------------------------------

# Create a dictionary called favorites with:
#
# name
# favorite_food
# favorite_game
# favorite_movie
# favorite_color
#
# Print the dictionary.


# ------------------------------------------------------------
# CHALLENGE 2 - ACCESS THE INFORMATION
# ------------------------------------------------------------

# Using your favorites dictionary:
#
# Print each value separately.
#
# Example:
# Name: Ben
# Favorite Food: Pizza
# Favorite Game: Minecraft


# ------------------------------------------------------------
# CHALLENGE 3 - UPDATE INFORMATION
# ------------------------------------------------------------

# Change the favorite food.
# Change the favorite color.
#
# Print the updated dictionary.


# ------------------------------------------------------------
# CHALLENGE 4 - ADD INFORMATION
# ------------------------------------------------------------

# Add:
#
# favorite_sport
# favorite_animal
#
# Print the dictionary again.


# ------------------------------------------------------------
# CHALLENGE 5 - CHECK FOR INFORMATION
# ------------------------------------------------------------

# Ask the user:
#
# "What information do you want to check? "
#
# Check if that key exists in your dictionary.
#
# If it exists:
#     print the key and its value
#
# Otherwise:
#     print "That information does not exist."


# ------------------------------------------------------------
# CHALLENGE 6 - GAME CHARACTER
# ------------------------------------------------------------

# Create this dictionary:

player = {
    "name": "Hero",
    "health": 100,
    "level": 5,
    "gold": 150,
    "weapon": "Sword"
}

# Do the following:
#
# 1. Print the player's name.
# 2. Print the player's health.
# 3. Increase the level by 1.
# 4. Add 50 gold.
# 5. Change the weapon to "Bow".
# 6. Print the final player dictionary.


# ------------------------------------------------------------
# CHALLENGE 7 - PLAYER HEALTH
# ------------------------------------------------------------

# Using the player dictionary:
#
# If health is 50 or higher:
#     print "You are healthy!"
#
# Otherwise:
#     print "You need to heal!"


# ------------------------------------------------------------
# CHALLENGE 8 - GRADES
# ------------------------------------------------------------

grades = {
    "Math": 90,
    "Science": 85,
    "English": 72,
    "History": 58,
    "Art": 95
}

# Use a for loop to print every subject and grade.
#
# Example:
# Math: 90
# Science: 85


# ------------------------------------------------------------
# CHALLENGE 9 - PASS OR FAIL
# ------------------------------------------------------------

# Using the grades dictionary:
#
# Loop through every subject.
#
# If the grade is 60 or higher:
#     print the subject and "PASS"
#
# Otherwise:
#     print the subject and "FAIL"


# ------------------------------------------------------------
# CHALLENGE 10 - FIND THE HIGHEST GRADE
# ------------------------------------------------------------

# Find the highest grade in the grades dictionary.
#
# DO NOT use max().
#
# Hint:
# Start with:
#
# highest_grade = 0
#
# Then use a for loop and an if statement.


# ------------------------------------------------------------
# CHALLENGE 11 - INVENTORY
# ------------------------------------------------------------

inventory = {
    "Potion": 3,
    "Sword": 1,
    "Shield": 1,
    "Arrow": 20
}

# Ask the user:
#
# "What item do you want to check? "
#
# If the item exists:
#     print how many they have
#
# Otherwise:
#     print "You don't have that item."


# ------------------------------------------------------------
# CHALLENGE 12 - MINI SHOP
# ------------------------------------------------------------

shop = {
    "Potion": 10,
    "Sword": 50,
    "Shield": 30,
    "Bow": 40
}

# Ask the user which item they want to buy.
#
# If the item exists:
#     print its price
#
# Otherwise:
#     print "That item is not in the shop."


# ============================================================
# FINAL HOMEWORK CHALLENGE
# ============================================================

# Create a dictionary called student with:
#
# name
# age
# grade
# favorite_subject
# favorite_game
# completed_homework
#
# Example:
#
# student = {
#     "name": "Ben",
#     "age": 12,
#     "grade": 7,
#     "favorite_subject": "Computer Science",
#     "favorite_game": "Minecraft",
#     "completed_homework": 4
# }


# Your program should:
#
# 1. Print the student's information.
#
# 2. Use a for loop to print every key and value.
#
# 3. Ask how many homework assignments they completed.
#
# 4. Update "completed_homework" with the new number.
#
# 5. If they completed 5 or more:
#       print "Great job!"
#
#    Otherwise:
#       print "Keep working!"
#
# 6. Ask the user for a new favorite game.
#
# 7. Update the dictionary.
#
# 8. Print the final student dictionary.


# ============================================================
# BONUS
# ============================================================

# Create a dictionary containing 5 students and their grades.
#
# Find:
# - Highest grade
# - Lowest grade
# - Number of students who passed
#
# DO NOT use:
# max()
# min()
#
# Use:
# - dictionaries
# - for loops
# - if statements
# - variables