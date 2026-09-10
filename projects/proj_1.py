# ============================================================
#              STUDENT TO-DO LIST PROJECT
# ============================================================
#
# Your mission:
#
# Build a working To-Do List program from scratch!
#
# This is a project to test the Python skills you have learned.
#
# You should use:
#   - Variables
#   - input()
#   - Lists
#   - append()
#   - remove()
#   - len()
#   - if / elif / else
#   - for loops
#   - while loops
#   - break
#   - List comprehensions
#
# IMPORTANT:
# Do NOT copy a completed solution.
#
# You are supposed to figure out how to build the program.
# You can ask for help understanding an error or concept,
# but try to solve the problem yourself first!
#
# ============================================================
#                     THE GOAL
# ============================================================
#
# Create a program that allows a student to manage their
# homework and other tasks.
#
# The program should keep running until the user chooses
# to quit.
#
# ============================================================
#                 PART 1 - STARTING LIST
# ============================================================
#
# Create a list called tasks.
#
# Start with at least 3 tasks.
#
# Example:
#
# tasks = ["Math homework", "Walk the dog", "Study Python"]
#
# You can choose your own tasks!
#
#
# ============================================================
#                 PART 2 - MAIN MENU
# ============================================================
#
# Your program needs a menu.
#
# It should look something like:
#
# =================================
#          MY TO-DO LIST
# =================================
#
# 1. Add a task
# 2. View tasks
# 3. Remove a task
# 4. Complete a task
# 5. Search for a task
# 6. Count tasks
# 7. Quit
#
# Choose an option:
#
# The menu should keep appearing until the user chooses
# option 7.
#
# HINT:
# A while loop will be useful here.
#
#
# ============================================================
#                 PART 3 - ADD A TASK
# ============================================================
#
# If the user chooses option 1:
#
# Ask:
#
# What task do you want to add?
#
# Add the task to the tasks list.
#
# Then tell the user that the task was added.
#
# Example:
#
# What task do you want to add? Finish science project
#
# Task added!
#
# HINT:
# You learned a list method that adds something to the
# end of a list.
#
#
# ============================================================
#                 PART 4 - VIEW TASKS
# ============================================================
#
# If the user chooses option 2:
#
# Display every task in the list.
#
# Example:
#
# =================================
#             TASKS
# =================================
#
# 1. Math homework
# 2. Walk the dog
# 3. Study Python
#
# You MUST use a FOR LOOP for this.
#
# BONUS:
# Figure out how to display the task number next to each task.
#
#
# ============================================================
#                 PART 5 - REMOVE A TASK
# ============================================================
#
# If the user chooses option 3:
#
# Ask the user which task they want to remove.
#
# Then remove that task from the list.
#
# Example:
#
# Which task do you want to remove?
#
# If the task exists:
#
# Task removed!
#
# If it doesn't exist:
#
# That task isn't on your list.
#
# You will need to use:
#
#     if
#
# and:
#
#     remove()
#
#``
# ============================================================
#                 PART 6 - COMPLETE A TASK
# ============================================================
#
# If the user chooses option 4:
#
# Ask which task they completed.
#
# You need to figure out a way to show that the task
# is completed.
#
# Example:
#
# Before:
#
# Math homework
#
# After:
#
# Math homework - DONE
#
# You decide exactly how to implement this.
#
# IMPORTANT:
# Think about how changing an item in a list works.
#
#
# ============================================================
#                 PART 7 - SEARCH
# ============================================================
#
# If the user chooses option 5:
#
# Ask the user what task they want to search for.
#
# Use a FOR LOOP to search through the list.
#
# If the task is found:
#
# Task found!
#
# Otherwise:
#
# Task not found.
#
# HINT:
# You will probably need:
#
#     for
#
#     if
#
#
# ============================================================
#                 PART 8 - COUNT TASKS
# ============================================================
#
# If the user chooses option 6:
#
# Tell the user how many tasks they currently have.
#
# Example:
#
# You currently have 5 tasks.
#
# You MUST use len().
#
#
# ============================================================
#                 PART 9 - QUIT
# ============================================================
#
# If the user chooses option 7:
#
# Display something like:
#
# Thanks for using the To-Do List!
#
# Then stop the program.
#
# HINT:
# You have learned a way to stop a loop.
#
#
# ============================================================
#                 PART 10 - INVALID INPUT
# ============================================================
#
# What happens if the user enters:
#
# 99
#
# or:
#
# banana
#
# or another option that isn't on the menu?
#
# Your program should NOT crash.
#
# Display:
#
# Invalid option. Please try again.
#
#
# ============================================================
#              LIST COMPREHENSION CHALLENGE
# ============================================================
#
# Your program MUST contain at least ONE list comprehension.
#
# YOU decide where to use it.
#
# Don't replace all your loops with list comprehensions.
#
# The goal is to demonstrate that you understand BOTH
# regular loops and list comprehensions.
#
#
# ============================================================
#                    BONUS 1
# ============================================================
#
# Add task priorities.
#
# For example:
#
# High
# Medium
# Low
#
# Let the user choose a priority when adding a task.
#
#
# ============================================================
#                    BONUS 2
# ============================================================
#
# Add a feature that displays ONLY completed tasks.
#
#
# ============================================================
#                    BONUS 3
# ============================================================
#
# Add a feature that displays ONLY unfinished tasks.
#
#
# ============================================================
#                    BONUS 4
# ============================================================
#
# Prevent the user from adding the exact same task twice.
#
#
# ============================================================
#                    BONUS 5
# ============================================================
#
# Add a "Clear Completed Tasks" option.
#
# This should remove all completed tasks from the list.
#
#
# ============================================================
#                 FINAL CHALLENGE
# ============================================================
#
# Make the program look professional!
#
# Add:
#
# - Nice headings
# - Helpful messages
# - Good variable names
# - Comments explaining difficult parts
# - Error handling for bad choices
#
# Try to make the program feel like a real application.
#
#
# ============================================================
#                    RULES
# ============================================================
#
# 1. Write the program yourself.
#
# 2. Don't copy a solution.
#
# 3. Test your program frequently.
#
# 4. When you get an error, read the error message.
#
# 5. Try to fix the problem yourself before asking for help.
#
# 6. You can change the design and make the program your own.
#
# 7. Have fun!
#
#
# ============================================================
#                    SKILL TEST
# ============================================================
#
# Can you build the entire program without being shown
# the solution?
#
# If YES:
#
# You are ready for the next level of Python.
#
# GOOD LUCK!
# ============================================================
task = ["Clean your room", "Do your homework","Put away the cloths ", "Finsih your project"]
print (1. Add task
    2. View task
    3. Remove task
    4. Complete a task
    5. Search to find a task
    6. Count task
    7. Quit)

action = input( "Enter actions 1 to 7")
if action == "1":
    new_task = input("What task woud you like to add?")
    task.append(new_task)
elif action == "2":
    print(task)
elif action == "3":
    remove_task = input ("Which task would you like removed?")
    if remove_task == ("Clean your room") ("Do your homework") ("Put away the cloths ") ("Finsih your project") :
        task.remove(remove_task)
elif action == "4":
    finish_task = input("Which task have you finished")
    if finish_task in task
    task.append("Done")
elif action == "5":
    find_task = input("Which task would you like to find?")
    if find_task in task:
        print("Task found")
    else:
        print("Task not found")
elif action == "6":
    print(len(task))
elif action == "7":
    print("Go complete your tasks")
else :
    print("Action not an option" )    