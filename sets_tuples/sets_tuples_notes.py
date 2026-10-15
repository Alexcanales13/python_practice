
# ==========================================
# PYTHON LESSON: SETS AND TUPLES
# ==========================================

# ------------------------------------------
# PART 1: SETS
# ------------------------------------------

# A set stores unique values.
# Sets automatically remove duplicates.
# Sets are unordered, so they do not guarantee
# a particular display order.

numbers = {1, 2, 3, 4, 5}
print(numbers)

# Duplicate values are removed.
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# An empty set must be created with set().
empty_set = set()

# IMPORTANT:
# {} creates an empty dictionary, not an empty set.


# ------------------------------------------
# PART 2: ADDING AND REMOVING SET ITEMS
# ------------------------------------------

fruits = {"apple", "banana", "orange"}

# Add an item.
fruits.add("grape")
print(fruits)

# Adding an existing item changes nothing.
fruits.add("apple")
print(fruits)

# Remove an item if it exists.
fruits.discard("banana")
print(fruits)

# remove() raises a KeyError if the item is missing.
fruits.remove("orange")
print(fruits)

# Clear every item.
fruits.clear()
print(fruits)


# ------------------------------------------
# PART 3: CHECKING MEMBERSHIP
# ------------------------------------------

players = {"Ben", "Alex", "Sam"}

print("Ben" in players)       # True
print("Jordan" in players)    # False

if "Ben" in players:
    print("Ben is in the game!")


# ------------------------------------------
# PART 4: LOOPING THROUGH A SET
# ------------------------------------------

colors = {"red", "blue", "green"}

for color in colors:
    print(color)

# The order is not guaranteed.
# Use sorted() if you need a consistent sorted order.

for color in sorted(colors):
    print(color)


# ------------------------------------------
# PART 5: SET LENGTH
# ------------------------------------------

pets = {"dog", "cat", "fish"}

print(len(pets))  # 3

pets.add("dog")
print(len(pets))  # Still 3


# ------------------------------------------
# PART 6: CONVERTING A LIST TO A SET
# ------------------------------------------

scores = [10, 20, 10, 30, 20, 40]

unique_scores = set(scores)

print(unique_scores)
# Contains only 10, 20, 30, and 40.

# Convert a set back to a list.
score_list = list(unique_scores)
print(score_list)

# The original order is not preserved reliably.


# ------------------------------------------
# PART 7: SET OPERATIONS
# ------------------------------------------

# UNION: Items in either set.
team_a = {"Ben", "Alex", "Sam"}
team_b = {"Alex", "Jordan", "Taylor"}

everyone = team_a | team_b
print(everyone)

# INTERSECTION: Items in both sets.
both_teams = team_a & team_b
print(both_teams)  # {"Alex"}

# DIFFERENCE: Items in the first set
# that are NOT in the second set.
only_a = team_a - team_b
print(only_a)  # {"Ben", "Sam"}

# SYMMETRIC DIFFERENCE:
# Items in either set, but not both.
different = team_a ^ team_b
print(different)


# ------------------------------------------
# PART 8: TUPLES
# ------------------------------------------

# A tuple stores an ordered collection.
# Tuples cannot be changed after creation.

coordinates = (10, 20)
print(coordinates)

# Access items using indexes.
print(coordinates[0])  # 10
print(coordinates[1])  # 20

# Negative indexes count from the end.
print(coordinates[-1])  # 20

# Tuples support len().
print(len(coordinates))


# ------------------------------------------
# PART 9: TUPLES CANNOT BE CHANGED
# ------------------------------------------

colors = ("red", "green", "blue")

# This would cause a TypeError:
# colors[0] = "yellow"

# You can read tuple items, but you cannot
# replace, append, or remove tuple items.

# If you need to change the collection,
# use a list instead.


# ------------------------------------------
# PART 10: CREATING TUPLES
# ------------------------------------------

# A tuple with several items.
person = ("Ben", 12, "Python")

# A tuple with one item needs a comma.
single_item = ("apple",)

# Without the comma, this is just a string.
not_a_tuple = ("apple")

print(type(single_item))
print(type(not_a_tuple))


# ------------------------------------------
# PART 11: LOOPING THROUGH A TUPLE
# ------------------------------------------

animals = ("dog", "cat", "rabbit")

for animal in animals:
    print(animal)

# You can also use a while loop.
index = 0

while index < len(animals):
    print(animals[index])
    index += 1


# ------------------------------------------
# PART 12: TUPLE UNPACKING
# ------------------------------------------

player = ("Ben", 12, 100)

name, age, health = player

print(name)
print(age)
print(health)

# The number of variables must match
# the number of tuple items.


# ------------------------------------------
# PART 13: FUNCTIONS THAT RETURN TUPLES
# ------------------------------------------

def get_player():
    name = "Ben"
    health = 100
    level = 1

    return name, health, level


player_data = get_player()

print(player_data)

# Unpack the returned tuple.
name, health, level = get_player()

print(name)
print(health)
print(level)


# ------------------------------------------
# PART 14: SETS VS TUPLES
# ------------------------------------------

# SET:
# - Unique values
# - Unordered
# - Can add and remove items
# - Useful for removing duplicates

unique_numbers = {1, 2, 3}

# TUPLE:
# - Ordered
# - Allows duplicate values
# - Cannot be changed
# - Useful for fixed collections of values

player_position = (10, 20)


# ------------------------------------------
# PART 15: COMBINING SETS AND TUPLES
# ------------------------------------------

# A set can contain tuples because tuples
# containing hashable values can be used
# as set items.

visited_positions = {
    (0, 0),
    (1, 0),
    (1, 1)
}

new_position = (2, 1)

if new_position not in visited_positions:
    visited_positions.add(new_position)

print(visited_positions)


# ==========================================
# END OF LESSON
# ==========================================
