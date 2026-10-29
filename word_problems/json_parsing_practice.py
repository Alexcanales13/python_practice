# JSON Parsing Practice
# Beginner LeetCode-style problems using Python's json module.
#
# Goal:
# Learn how to parse JSON data, access nested dictionaries and lists,
# search records, filter results, and calculate information.
#
# Important:
# - JSON text becomes Python dictionaries, lists, strings, numbers,
#   booleans, and None after json.loads().
# - JSON uses true/false/null. Python uses True/False/None.
# - Start by solving each problem with the provided data.
# - Write the requested functions in the TODO sections.
#
# You do NOT need to install anything. The json module is built into Python.

import json


# ==================================================
# STARTER DATA
# ==================================================

students_json = """
{
    "students": [
        {"name": "Ben", "age": 12, "grade": 88, "subject": "Python"},
        {"name": "Mia", "age": 12, "grade": 95, "subject": "Science"},
        {"name": "Alex", "age": 13, "grade": 72, "subject": "Math"},
        {"name": "Noah", "age": 14, "grade": 64, "subject": "Python"},
        {"name": "Emma", "age": 13, "grade": 81, "subject": "Math"}
    ]
}
"""

# Convert the JSON text into a Python dictionary.
student_data = json.loads(students_json)


games_json = """
{
    "games": [
        {"name": "Minecraft", "genre": "Sandbox", "price": 20, "players": 5},
        {"name": "Fortnite", "genre": "Battle Royale", "price": 0, "players": 8},
        {"name": "Roblox", "genre": "Sandbox", "price": 0, "players": 12},
        {"name": "Terraria", "genre": "Adventure", "price": 10, "players": 4},
        {"name": "Stardew Valley", "genre": "Simulation", "price": 15, "players": 2}
    ]
}
"""

game_data = json.loads(games_json)


# ==================================================
# LEVEL 1 — READ JSON
# ==================================================

# Problem 1: Print Student Names
# Print the name of every student.
#
# Expected names: Ben, Mia, Alex, Noah, Emma
#
# Hint:
# student_data is a dictionary.
# The list of students is inside student_data["students"].
# Loop through that list.


def print_student_names(data):
    # Your code here
    pass


# Problem 2: Print Student Details
# Print each student's name and grade.
#
# Example output:
# Ben: 88
# Mia: 95
# ...


def print_student_grades(data):
    # Your code here
    pass


# Problem 3: Count Students
# Return the number of students in the JSON data.
#
# Expected result: 5
#
# Try using a loop rather than len().


def count_students(data):
    # Your code here
    pass


# ==================================================
# LEVEL 2 — SEARCH AND FILTER JSON
# ==================================================

# Problem 4: Find a Student
# Search for a student by name and return their complete dictionary.
# If the student isn't found, return None.
#
# Example:
# find_student(student_data, "Mia")
# Expected: {"name": "Mia", "age": 12, "grade": 95, "subject": "Science"}
#
# Hint: Loop through data["students"] and compare each student's name.


def find_student(data, search_name):
    # Your code here
    pass


# Problem 5: Find Passing Students
# Return a list of student names whose grade is at least 70.
#
# Expected: ["Ben", "Mia", "Alex", "Emma"]


def passing_students(data):
    # Your code here
    pass


# Problem 6: Search by Favorite Subject
# Given a subject, return a list of student names who chose it.
# Ignore capitalization.
#
# Example:
# students_by_subject(student_data, "python")
# Expected: ["Ben", "Noah"]


def students_by_subject(data, subject):
    # Your code here
    pass


# Problem 7: Filter Games by Price
# Return a list of game names that cost less than or equal to a maximum price.
#
# Example:
# games_at_or_below(game_data, 10)
# Expected: ["Fortnite", "Roblox", "Terraria"]


def games_at_or_below(data, maximum_price):
    # Your code here
    pass


# ==================================================
# LEVEL 3 — CALCULATE FROM JSON
# ==================================================

# Problem 8: Average Grade
# Calculate and return the average student grade.
# Do not use sum().
#
# Expected result: 80.0
#
# Hint: Keep track of a total and a count.


def average_grade(data):
    # Your code here
    pass


# Problem 9: Most Expensive Game
# Return the name of the most expensive game.
# Do not use max() or sorted().
#
# Expected result: "Minecraft"


def most_expensive_game(data):
    # Your code here
    pass


# Problem 10: Count Games by Genre
# Return a dictionary counting how many games belong to each genre.
#
# Expected result:
# {
#     "Sandbox": 2,
#     "Battle Royale": 1,
#     "Adventure": 1,
#     "Simulation": 1
# }
#
# Hint: Create a dictionary to store counts.


def count_games_by_genre(data):
    # Your code here
    pass


# ==================================================
# LEVEL 4 — NESTED JSON
# ==================================================

teams_json = """
{
    "teams": [
        {
            "name": "Dragons",
            "players": [
                {"name": "Ben", "points": 120},
                {"name": "Mia", "points": 85}
            ]
        },
        {
            "name": "Tigers",
            "players": [
                {"name": "Alex", "points": 100},
                {"name": "Noah", "points": 40}
            ]
        }
    ]
}
"""

team_data = json.loads(teams_json)


# Problem 11: Print Every Player
# Print each player's name and team.
#
# Expected examples:
# Ben is on the Dragons
# Mia is on the Dragons
# Alex is on the Tigers
# Noah is on the Tigers
#
# Hint: You need one loop for teams and another loop for each team's players.


def print_team_players(data):
    # Your code here
    pass


# Problem 12: Find a Player
# Search every team and return the player's points.
# If the player isn't found, return -1.
#
# Example:
# find_player_points(team_data, "Alex") -> 100
# find_player_points(team_data, "Sam") -> -1


def find_player_points(data, search_name):
    # Your code here
    pass


# Problem 13: Team Total
# Return a dictionary containing each team's total points.
#
# Expected:
# {"Dragons": 205, "Tigers": 140}


def team_total_points(data):
    # Your code here
    pass


# ==================================================
# LEVEL 5 — CHANGE JSON DATA
# ==================================================

# Problem 14: Add a New Student
# Write a function that adds a new student dictionary to data["students"].
# The function receives data, name, age, grade, and subject.
# If a student with that name already exists (ignore capitalization),
# do not add the student. Return True if added, otherwise False.
#
# Example:
# add_student(student_data, "Sam", 12, 90, "Python") -> True
#
# Note: This changes the supplied Python dictionary in place.
# Do not convert it back to JSON inside this function.


def add_student(data, name, age, grade, subject):
    # Your code here
    pass


# Problem 15: Update a Student's Grade
# Find a student by name and update their grade.
# Ignore capitalization.
# Return True if the student was found and updated; otherwise False.
#
# Example:
# update_grade(student_data, "Ben", 91) -> True


def update_grade(data, search_name, new_grade):
    # Your code here
    pass


# Problem 16: Convert Back to JSON
# Write a function that converts a Python dictionary back into a JSON string.
# The JSON should be nicely indented.
#
# Hint: json.dumps(data, indent=2)


def to_json_string(data):
    # Your code here
    pass


# ==================================================
# LEVEL 6 — VALIDATE AND HANDLE JSON
# ==================================================

# Problem 17: Safely Read a JSON String
# Write a function that takes a JSON string and returns the parsed Python
# value. If the string contains invalid JSON, return None.
#
# Hint:
# try:
#     ...
# except json.JSONDecodeError:
#     ...


def safe_parse_json(json_text):
    # Your code here
    pass


# Problem 18: Get a Value Safely
# The input is a dictionary that might or might not contain a key.
# Return the value for the requested key, or the supplied default if missing.
#
# Example:
# get_value({"name": "Ben"}, "age", 0) -> 0
# get_value({"name": "Ben"}, "name", "Unknown") -> "Ben"
#
# Hint: Dictionaries have a .get() method.


def get_value(record, key, default_value):
    # Your code here
    pass


# ==================================================
# TEST YOUR FUNCTIONS
# ==================================================
# Uncomment tests as you complete each problem.
#
# print_student_names(student_data)
# print_student_grades(student_data)
# print(count_students(student_data))  # Expected: 5
# print(find_student(student_data, "Mia"))
# print(passing_students(student_data))
# print(students_by_subject(student_data, "python"))
# print(games_at_or_below(game_data, 10))
# print(average_grade(student_data))  # Expected: 80.0
# print(most_expensive_game(game_data))  # Expected: Minecraft
# print(count_games_by_genre(game_data))
# print_team_players(team_data)
# print(find_player_points(team_data, "Alex"))  # Expected: 100
# print(team_total_points(team_data))
# print(add_student(student_data, "Sam", 12, 90, "Python"))
# print(update_grade(student_data, "Ben", 91))
# print(to_json_string(student_data))
# print(safe_parse_json('{"name": "Ben"}'))
# print(safe_parse_json('{"name": }'))  # Expected: None
# print(get_value({"name": "Ben"}, "age", 0))  # Expected: 0


# ==================================================
# FINAL CHALLENGE — GAME CLUB JSON REPORT
# ==================================================
# Use game_data to create a report that shows:
#
# 1. Every game and its price.
# 2. All free games.
# 3. The average game price.
# 4. The game with the most players.
# 5. The number of games in each genre.
# 6. A new JSON string containing only free games.
#
# Try to write a separate function for each task.
# Bonus: Save the new JSON string to a file with open(..., "w")
# and load it again with open(..., "r").
