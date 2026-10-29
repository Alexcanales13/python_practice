# Python Problem-Solving Practice
# Beginner LeetCode-style problems
#
# Instructions:
# - Solve each problem by writing the requested function.
# - Test your function using the examples.
# - Try one extra example of your own for each problem.
# - Do not look up solutions before trying to solve the problem yourself.


# ==================================================
# LEVEL 1 — WARM-UP
# ==================================================

# Problem 1: Count Even Numbers
# Given a list of numbers, return how many numbers are even.
#
# Example:
# count_even([1, 2, 3, 4, 6]) -> 3
# count_even([1, 3, 5]) -> 0
#
# Hint: Use a loop and the remainder operator (%).

def count_even(numbers):
    # Your code here
    pass


# Problem 2: Find the Biggest Number
# Given a non-empty list of numbers, return the largest number.
# Do not use max().
#
# Example:
# find_biggest([4, 9, 2, 7]) -> 9
# find_biggest([15, 3, 8]) -> 15
#
# Hint: Remember the biggest number you've seen so far.

def find_biggest(numbers):
    # Your code here
    pass


# Problem 3: Count Matching Words
# Count how many times the target appears in a list.
# Ignore capitalization.
#
# Example:
# count_word(["Cat", "dog", "cat", "CAT"], "cat") -> 3
# count_word(["apple", "pear"], "banana") -> 0
#
# Hint: Convert both words to lowercase before comparing.

def count_word(words, target):
    # Your code here
    pass


# ==================================================
# LEVEL 2 — SEARCHING AND FILTERING
# ==================================================

# Problem 4: Find the Student
# Given a dictionary of student grades, return the grade for the
# requested student. If the student doesn't exist, return -1.
#
# Example:
# grades = {"Ben": 88, "Mia": 95, "Alex": 72}
# find_grade(grades, "Mia") -> 95
# find_grade(grades, "Noah") -> -1
#
# Hint: Check whether the name is a key in the dictionary.

def find_grade(grades, name):
    # Your code here
    pass


# Problem 5: Passing Students
# Return a new dictionary containing only students with a grade
# of 70 or higher.
#
# Example:
# grades = {"Ben": 88, "Mia": 65, "Alex": 72, "Noah": 54}
# passing_students(grades) -> {"Ben": 88, "Alex": 72}
#
# Hint: Loop through .items() and build a new dictionary.

def passing_students(grades):
    # Your code here
    pass


# Problem 6: Find the Most Expensive Item
# Return the name of the most expensive item.
# Do not use max() or sorted().
#
# Example:
# prices = {
#     "Pencil": 2,
#     "Backpack": 30,
#     "Notebook": 5,
#     "Calculator": 20
# }
# most_expensive(prices) -> "Backpack"
#
# Hint: Track both the highest price and its item name.

def most_expensive(prices):
    # Your code here
    pass


# ==================================================
# LEVEL 3 — PARSING DICTIONARIES
# ==================================================

# Problem 7: Count Products by Category
# Count how many products belong to each category.
#
# Example data:
products = {
    "Apple": {"category": "Fruit"},
    "Banana": {"category": "Fruit"},
    "Carrot": {"category": "Vegetable"},
    "Pear": {"category": "Fruit"},
    "Potato": {"category": "Vegetable"}
}
#
# Expected result:
# {"Fruit": 3, "Vegetable": 2}
#
# Hint: For each product, read its category. If the category isn't
# in your counting dictionary yet, start its count at zero.

def count_categories(products):
    # Your code here
    pass


# Problem 8: Find Players With Enough Points
# Return a list of names for players with at least 100 points.
#
# Example data:
players = {
    "Ben": {"points": 120},
    "Mia": {"points": 85},
    "Alex": {"points": 100},
    "Noah": {"points": 40}
}
#
# Expected result:
# ["Ben", "Alex"]
#
# Hint: Access the nested value with information["points"].

def strong_players(players):
    # Your code here
    pass


# Problem 9: Find the Highest-Scoring Player
# Return the name of the player with the most wins.
#
# Example data:
players_with_wins = {
    "Ben": {"wins": 5, "losses": 2},
    "Mia": {"wins": 8, "losses": 1},
    "Alex": {"wins": 3, "losses": 4}
}
#
# Expected result: "Mia"
#
# Hint: Compare the wins value for every player.

def best_player(players):
    # Your code here
    pass


# ==================================================
# LEVEL 4 — EASY CHALLENGES
# ==================================================

# Problem 10: Find Duplicate Numbers
# Return a list of numbers that appear more than once.
# Each duplicate should appear only once in the answer.
#
# Example:
# find_duplicates([1, 2, 3, 2, 4, 1, 5]) -> [1, 2]
# find_duplicates([1, 2, 3]) -> []
#
# Hint: Use one collection to remember numbers you've seen,
# and another to store duplicates. A set can help.

def find_duplicates(numbers):
    # Your code here
    pass


# Problem 11: Inventory Value
# Each item has a quantity and a price per item.
# Calculate the total value of the inventory.
#
# Example data:
inventory = {
    "Apples": {"quantity": 4, "price": 2},
    "Bread": {"quantity": 3, "price": 5},
    "Milk": {"quantity": 2, "price": 4}
}
#
# Expected result: 31
#
# Hint: Multiply each item's quantity by its price, then add
# those values together.

def inventory_value(inventory):
    # Your code here
    pass


# Problem 12: Group Students by Grade
# Group student names by their grade.
#
# Example:
# grades_to_group = {
#     "Ben": 90,
#     "Mia": 80,
#     "Alex": 90,
#     "Noah": 80,
#     "Emma": 90
# }
#
# Expected result:
# {
#     90: ["Ben", "Alex", "Emma"],
#     80: ["Mia", "Noah"]
# }
#
# Hint: The grade becomes the key, and each value is a list of names.

def group_by_grade(grades):
    # Your code here
    pass


# ==================================================
# TEST YOUR FUNCTIONS
# ==================================================
# After solving a problem, uncomment its tests and run the file.
# For example:
#
# print(count_even([1, 2, 3, 4, 6]))  # Expected: 3
# print(count_even([1, 3, 5]))        # Expected: 0
#
# print(find_biggest([4, 9, 2, 7]))   # Expected: 9
#
# print(count_word(["Cat", "dog", "cat", "CAT"], "cat"))  # Expected: 3
#
# print(find_grade({"Ben": 88, "Mia": 95}, "Mia"))   # Expected: 95
# print(find_grade({"Ben": 88, "Mia": 95}, "Noah"))  # Expected: -1
#
# print(passing_students({"Ben": 88, "Mia": 65, "Alex": 72}))
# Expected: {"Ben": 88, "Alex": 72}
#
# print(most_expensive({"Pencil": 2, "Backpack": 30, "Notebook": 5}))
# Expected: "Backpack"
#
# print(count_categories(products))  # Expected: {"Fruit": 3, "Vegetable": 2}
# print(strong_players(players))     # Expected: ["Ben", "Alex"]
# print(best_player(players_with_wins))  # Expected: "Mia"
#
# print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))  # Expected: [1, 2]
# print(inventory_value(inventory))               # Expected: 31
# print(group_by_grade(grades_to_group))
