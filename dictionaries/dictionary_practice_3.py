# DICTIONARY PARSING PRACTICE
#
# Goal:
# Learn how to search through dictionaries,
# inspect their contents, and find specific information.
#
# Rules:
# 1. Try to solve each challenge yourself.
# 2. Use loops to inspect dictionary contents.
# 3. Don't just print the entire dictionary as your answer.
# 4. Print the specific information requested.

students = {
    "Ben": {"age": 12, "grade": 88, "favorite_subject": "Python"},
    "Alex": {"age": 13, "grade": 72, "favorite_subject": "Math"},
    "Mia": {"age": 12, "grade": 95, "favorite_subject": "Science"},
    "Noah": {"age": 14, "grade": 64, "favorite_subject": "Python"},
    "Emma": {"age": 13, "grade": 81, "favorite_subject": "Math"},
    "Liam": {"age": 12, "grade": 88, "favorite_subject": "Python"}
}


# --------------------------------------------------
# LEVEL 1: LOOK THROUGH A DICTIONARY
# --------------------------------------------------

# Challenge 1:
# Print every student's name.

# Challenge 2:
# Print every student's name and grade.

# Challenge 3:
# Print the names of students whose grade is above 80.

# Challenge 4:
# Print the names of students who like Python.

# Challenge 5:
# Count how many students are in the dictionary.
# Do this by looping through the dictionary instead of using len().


# --------------------------------------------------
# LEVEL 2: SEARCH FOR SPECIFIC INFORMATION
# --------------------------------------------------

# Challenge 6:
# Ask the user for a subject.
# Print every student who likes that subject.

# Challenge 7:
# Ask the user for a name.
# Search through the dictionary to find that student.
# Print their age, grade, and favorite subject.
# If the student doesn't exist, print "Student not found."

# Challenge 8:
# Find and print the student with the highest grade.
# Do not use max() or sorted().

# Challenge 9:
# Find and print the student with the lowest grade.
# Do not use min() or sorted().

# Challenge 10:
# Count how many students have a grade of 80 or higher.


# --------------------------------------------------
# LEVEL 3: BUILD A NEW DICTIONARY
# --------------------------------------------------

# Challenge 11:
# Create a new dictionary called passing_students.
# Include only students whose grade is at least 70.
# Keep their original student records.

# Challenge 12:
# Create a dictionary containing only students who like Python.

# Challenge 13:
# Create a dictionary containing students who are 12 years old.

# Challenge 14:
# Create a dictionary of students who scored 85 or higher.
# Print the new dictionary after building it.

# Challenge 15:
# Ask the user for a minimum grade.
# Build a new dictionary containing every student who
# scored at least that grade.


# --------------------------------------------------
# LEVEL 4: PARSE NESTED DICTIONARIES
# --------------------------------------------------

# Challenge 16:
# For every student, print:
# Name, age, grade, and favorite subject.
#
# Use a loop and access the inner dictionary.

# Challenge 17:
# Find every student who:
# - Is at least 13 years old
# - Has a grade above 75

# Challenge 18:
# Count how many students like each subject.
#
# Expected result:
# {
#     "Python": 3,
#     "Math": 2,
#     "Science": 1
# }
#
# Hint: Make a new dictionary to track the counts.

# Challenge 19:
# Find all students who have the same grade.
#
# Hint:
# Loop through the students and compare their grades.
# You may need two loops.
#
# Example:
# Ben and Liam both scored 88.

# Challenge 20:
# Find the average grade of all students.
#
# Do not use sum() or calculate it from a hardcoded list.
# Loop through the dictionary and add the grades yourself.


# --------------------------------------------------
# LEVEL 5: MORE CHALLENGING
# --------------------------------------------------

# Challenge 21:
# Find the subject with the most students.
#
# First, count how many students like each subject.
# Then search through the count dictionary to find
# the subject with the highest count.
#
# Do not use max() or sorted().

# Challenge 22:
# Find students whose grades are above the class average.
#
# First, calculate the average.
# Then loop through the dictionary again.

# Challenge 23:
# Ask the user for a subject.
# Print the average grade of students who like that subject.
#
# If no students like that subject, print a helpful message.

# Challenge 24:
# Build a dictionary grouping student names by subject.
#
# Expected structure:
# {
#     "Python": ["Ben", "Noah", "Liam"],
#     "Math": ["Alex", "Emma"],
#     "Science": ["Mia"]
# }
#
# Hint:
# If a subject isn't in your new dictionary yet,
# create an empty list for it.
# Then append the student's name.


# --------------------------------------------------
# FINAL CHALLENGE: STUDENT REPORT
# --------------------------------------------------

# Create a report that displays:
#
# 1. Every student's name and grade
# 2. The class average
# 3. The highest-scoring student
# 4. The lowest-scoring student
# 5. All students who are passing (70 or higher)
# 6. The number of students who like each subject
# 7. All students who scored above the class average
#
# Try to use functions so each part of the report
# has its own job.