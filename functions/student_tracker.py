# ============================================================
#              STUDENT GRADE & STUDY TRACKER
# ============================================================

# Your goal:
# Build a program that lets a student manage their
# classes, grades, and homework.
#
# You will use:
# variables
# input
# if statements
# lists
# dictionaries
# loops
# while loops
# functions
# return
# list comprehensions
#
# Try to complete the project without looking at the solution.


# ============================================================
# STARTING DATA
# ============================================================

student = {
    "name": "Ben",
    "age": 12,
    "classes": {
        "Math": 85,
        "Science": 92,
        "Python": 100
    },
    "homework": [
        "Math worksheet",
        "Science project",
        "Python practice"
    ],
    "completed_homework": []
}


# ============================================================
# FUNCTION 1: SHOW STUDENT
# ============================================================

# Create a function called show_student(student).
#
# Print:
# - Name
# - Age
#
# Then print all classes and grades.
#
# Example:
#
# Name: Ben
# Age: 12
#
# Classes:
# Math: 85
# Science: 92
# Python: 100


# ============================================================
# FUNCTION 2: SHOW HOMEWORK
# ============================================================

# Create a function called show_homework(student).
#
# Loop through the homework list.
#
# Print each homework assignment.
#
# If an assignment has been completed,
# print "- DONE" next to it.
#
# Example:
#
# Math worksheet - DONE
# Science project
# Python practice


# ============================================================
# FUNCTION 3: ADD HOMEWORK
# ============================================================

# Create a function called add_homework(student).
#
# Ask the user:
# "Enter a homework assignment: "
#
# Add the homework to the homework list.
#
# Make sure the homework is not blank.
#
# Bonus:
# Don't allow duplicate homework.


# ============================================================
# FUNCTION 4: COMPLETE HOMEWORK
# ============================================================

# Create a function called complete_homework(student).
#
# Ask the user which homework they completed.
#
# If the homework exists:
#     Add it to completed_homework.
#
# Otherwise:
#     Print "Homework not found."
#
# Also make sure the homework isn't already completed.


# ============================================================
# FUNCTION 5: ADD A CLASS
# ============================================================

# Create a function called add_class(student).
#
# Ask the user for a class name.
#
# Ask for the grade.
#
# Convert the grade to an integer.
#
# Add the class and grade to the classes dictionary.
#
# Example:
#
# Class: History
# Grade: 88
#
# The dictionary should now contain:
#
# "History": 88


# ============================================================
# FUNCTION 6: SHOW GRADE STATUS
# ============================================================

# Create a function called grade_status(grade).
#
# If grade >= 90:
#     return "A"
#
# If grade >= 80:
#     return "B"
#
# If grade >= 70:
#     return "C"
#
# If grade >= 60:
#     return "D"
#
# Otherwise:
#     return "F"


# ============================================================
# FUNCTION 7: SHOW ALL GRADE LETTERS
# ============================================================

# Create a function called show_grades(student).
#
# Loop through the classes dictionary.
#
# Print:
#
# Math: 85 (B)
# Science: 92 (A)
# Python: 100 (A)
#
# Use the grade_status() function
# to determine the letter grade.


# ============================================================
# FUNCTION 8: FIND HIGHEST GRADE
# ============================================================

# Create a function called highest_grade(student).
#
# Find the highest grade in the classes dictionary.
#
# DO NOT use max().
#
# Hint:
#
# Start with:
#
# highest = 0
#
# Then loop through the grades.


# ============================================================
# FUNCTION 9: COUNT PASSING CLASSES
# ============================================================

# Create a function called count_passing_classes(student).
#
# A passing grade is 60 or higher.
#
# Loop through the classes.
#
# Count how many classes are passing.
#
# Return the number.


# ============================================================
# FUNCTION 10: SEARCH HOMEWORK
# ============================================================

# Create a function called search_homework(student).
#
# Ask the user for a search term.
#
# Search through the homework list.
#
# If the search term is found inside a homework assignment,
# print that assignment.
#
# Hint:
#
# if search_term.lower() in homework.lower():
#
# Example:
#
# Search: math
#
# Math worksheet


# ============================================================
# FUNCTION 11: SHOW COMPLETED HOMEWORK
# ============================================================

# Create a function called show_completed_homework(student).
#
# Loop through completed_homework.
#
# Print each completed assignment.
#
# If there are none, print:
#
# "No homework has been completed yet."


# ============================================================
# FUNCTION 12: CLEAR COMPLETED HOMEWORK
# ============================================================

# Create a function called clear_completed_homework(student).
#
# Remove completed assignments from the main homework list.
#
# Then clear the completed_homework list.
#
# You can use:
#
# list comprehensions
#
# Example:
#
# student["homework"] = [
#     homework
#     for homework in student["homework"]
#     if homework not in student["completed_homework"]
# ]
#
# Then clear the completed list.


# ============================================================
# MAIN PROGRAM
# ============================================================

# Create a while True loop.
#
# Display this menu:
#
# ==============================
#       STUDENT TRACKER
# ==============================
# 1. Show student
# 2. Show homework
# 3. Add homework
# 4. Complete homework
# 5. Add class
# 6. Show grades
# 7. Show highest grade
# 8. Count passing classes
# 9. Search homework
# 10. Show completed homework
# 11. Clear completed homework
# 12. Quit
# ==============================
#
# Ask:
#
# "Choose an option: "
#
# Use if / elif statements to call
# the appropriate function.
#
# If the user chooses 12:
#
# print("Goodbye!")
#
# Then use break.


# ============================================================
# BONUS CHALLENGES
# ============================================================

# BONUS 1
#
# Create a function called average_grade(student).
#
# Calculate the average grade.
#
# Return the average.


# BONUS 2
#
# Create a function called remove_class(student).
#
# Ask the user which class they want to remove.
#
# If it exists, remove it.
#
# Otherwise print:
# "Class not found."


# BONUS 3
#
# Create a function called find_failed_classes(student).
#
# Use a list comprehension to create a list
# containing classes with grades below 60.
#
# Example:
#
# failed_classes = [
#     class_name
#     for class_name in student["classes"]
#     if student["classes"][class_name] < 60
# ]


# BONUS 4
#
# Add a "study_points" value to the student dictionary.
#
# Example:
#
# "study_points": 0
#
# Every time homework is completed,
# add 10 study points.
#
# Create a function:
#
# add_study_points(student, amount)


# BONUS 5
#
# Create a function called level_check(student).
#
# If study_points >= 100:
#     return "Level 3"
#
# If study_points >= 50:
#     return "Level 2"
#
# Otherwise:
#     return "Level 1"