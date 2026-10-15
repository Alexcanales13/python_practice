
# ==========================================
# SETS AND TUPLES PRACTICE
# ==========================================

# RULES:
# 1. Try every challenge yourself.
# 2. Use print() to check your work.
# 3. Do not skip straight to the final challenge.


# ------------------------------------------
# LEVEL 1: SET BASICS
# ------------------------------------------

# Challenge 1:
# Create a set containing five different numbers.
# Print the set.


# Challenge 2:
# Create a set containing these numbers:
# 1, 2, 2, 3, 4, 4, 5, 5, 5
# Print it and observe what happens to duplicates.


# Challenge 3:
# Create an empty set.
# Add "sword", "shield", and "potion".
# Print the set.


# Challenge 4:
# Create a set of three animals.
# Add a fourth animal.
# Remove one animal using discard().
# Print the final set.


# Challenge 5:
# Create a set of usernames:
# "Ben", "Alex", "Sam"
# Ask the user to enter a username.
# Print whether the username is in the set.


# ------------------------------------------
# LEVEL 2: LOOPS AND SETS
# ------------------------------------------

# Challenge 6:
# Create a set of five colors.
# Use a for loop to print every color.


# Challenge 7:
# Create a set of numbers.
# Use a loop to calculate their total.


# Challenge 8:
# Create a list containing duplicate names.
# Convert the list into a set.
# Print the unique names.


# Challenge 9:
# Given a list of scores, create a set of unique scores.
# Print how many unique scores there are.

scores = [10, 20, 10, 30, 20, 40, 40, 50]


# Challenge 10:
# Create a set of registered players.
# Ask the user for a new player's name.
# If the player is already registered, print a message.
# Otherwise, add the player and print a success message.


# ------------------------------------------
# LEVEL 3: SET OPERATIONS
# ------------------------------------------

# Challenge 11:
# Find everyone who belongs to either team.

team_a = {"Ben", "Alex", "Sam"}
team_b = {"Alex", "Jordan", "Taylor"}


# Challenge 12:
# Find the players who belong to BOTH teams.


# Challenge 13:
# Find the players who are in team_a but NOT team_b.


# Challenge 14:
# Find the players who are in exactly one team,
# but not both.


# Challenge 15:
# Two lists contain students who signed up
# for different clubs.
# Find students who signed up for both clubs.

coding_club = ["Ben", "Alex", "Sam", "Jordan"]
art_club = ["Sam", "Taylor", "Ben", "Casey"]


# ------------------------------------------
# LEVEL 4: TUPLE BASICS
# ------------------------------------------

# Challenge 16:
# Create a tuple containing your name, age, and
# favorite programming language.
# Print each item separately.


# Challenge 17:
# Create a tuple of five favorite games.
# Print the first, third, and last items.


# Challenge 18:
# Create a tuple containing four numbers.
# Use a loop to print each number.


# Challenge 19:
# Create a tuple containing:
# "Ben", 12, 95
# Unpack the tuple into name, age, and score.
# Print each variable.


# Challenge 20:
# Create a tuple with one item.
# Check its type using type().
# Make sure you include the comma!


# ------------------------------------------
# LEVEL 5: FUNCTIONS AND TUPLES
# ------------------------------------------

# Challenge 21:
# Write a function called get_coordinates().
# It should return two values: 10 and 20.
# Store the returned values in two variables.


# Challenge 22:
# Write a function called get_player_stats().
# Return a player's name, health, and level
# as a tuple.
# Unpack the result into three variables.


# Challenge 23:
# Write a function called calculate_stats(numbers).
# It should return the smallest number,
# largest number, and total as a tuple.
# Call it with a list of numbers and print the result.


# ------------------------------------------
# LEVEL 6: COMBINED CHALLENGES
# ------------------------------------------

# Challenge 24: Unique Word Collector
# Ask the user to enter five words.
# Store them in a list.
# Convert the list into a set.
# Print the unique words and how many there are.


# Challenge 25: Game Registration
# Create a set of registered players.
# Create a tuple for a new player containing:
# name, age, and favorite game.
# Unpack the tuple.
# Add the player's name to the registered set.
# Print both collections.


# Challenge 26: Visited Locations
# A game has a player exploring a map.
# Represent each location as a tuple (x, y).
# Store visited locations in a set.
# Add at least five locations.
# Ask the user for an x and y coordinate.
# Create a coordinate tuple.
# Check if that location has already been visited.


# Challenge 27: Shared Interests
# Create two sets of hobbies for two friends.
# Print:
# - All hobbies they enjoy
# - Hobbies they both enjoy
# - Hobbies only the first friend enjoys
# - Hobbies only one of them enjoys


# Challenge 28: Leaderboard
# Create a list of player scores with duplicates.
# Use a set to find unique scores.
# Convert the unique scores to a list.
# Sort them from highest to lowest.
# Print the top three unique scores.


# ==========================================
# FINAL PROJECT: GAME CLUB MANAGER
# ==========================================

# Build a program that manages a gaming club.
#
# Requirements:
#
# 1. Create a set of registered usernames.
#
# 2. Create a tuple for each player's profile:
#    (username, age, favorite_game)
#
# 3. Ask the user to register a new player.
#
# 4. Check the set to prevent duplicate usernames.
#
# 5. If the username is new:
#    - Add it to the registered usernames set.
#    - Create and display the player's profile tuple.
#
# 6. Store multiple player profiles in a list.
#
# 7. Use a loop to display all player profiles.
#
# 8. Display how many unique players are registered.
#
# BONUS:
# - Create a second set for a gaming tournament.
# - Find players who registered for the club and tournament.
# - Find club members who have not joined the tournament.
# - Put repeated logic into functions.
# ==========================================
