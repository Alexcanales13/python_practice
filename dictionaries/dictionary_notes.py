# ============================================================
#                 PYTHON DICTIONARIES
# ============================================================

# A dictionary stores information using:
#
#       KEY : VALUE
#
# Think of it like a real dictionary:
#
#       WORD -> DEFINITION
#
# Example:

person = {
    "name": "Alex",
    "age": 12,
    "favorite_food": "Pizza"
}

print(person)


# ============================================================
# 1. ACCESSING VALUES
# ============================================================

# You can get a value by using its key.

print(person["name"])
print(person["age"])
print(person["favorite_food"])


# The key goes inside the brackets.
#
# person["name"]
#
# gives us:
#
# Alex


# ============================================================
# 2. CHANGING A VALUE
# ============================================================

person["age"] = 13

print(person["age"])


# You can change an existing value by using its key.


# ============================================================
# 3. ADDING A NEW VALUE
# ============================================================

person["favorite_color"] = "Blue"

print(person)


# If the key doesn't exist, Python creates it.


# ============================================================
# 4. REMOVING SOMETHING
# ============================================================

person.pop("favorite_color")

print(person)


# pop() removes a key and its value.


# ============================================================
# 5. CHECKING IF A KEY EXISTS
# ============================================================

if "name" in person:
    print("The person has a name.")


if "height" not in person:
    print("Height isn't stored.")


# ============================================================
# 6. DICTIONARIES AND FOR LOOPS
# ============================================================

# You can loop through the keys.

for key in person:
    print(key)


# You can use the key to get the value.

for key in person:
    print(key, ":", person[key])


# ============================================================
# 7. KEYS AND VALUES
# ============================================================

print(person.keys())
print(person.values())


# keys() gives you all the keys.
#
# values() gives you all the values.


# ============================================================
# 8. DICTIONARY OF A GAME CHARACTER
# ============================================================

player = {
    "name": "Hero",
    "health": 100,
    "gold": 50,
    "weapon": "Sword"
}

print(player["name"])
print(player["health"])
print(player["gold"])
print(player["weapon"])


# We can change information.

player["health"] = 80
player["gold"] = 75

print(player)


# ============================================================
# 9. DICTIONARIES WITH IF STATEMENTS
# ============================================================

if player["health"] <= 0:
    print("Game Over!")
else:
    print("You are still alive!")


# ============================================================
# 10. DICTIONARIES WITH LOOPS
# ============================================================

scores = {
    "Alex": 90,
    "Sarah": 85,
    "Mike": 72,
    "Jordan": 100
}

for name in scores:
    print(name, "scored", scores[name])


# ============================================================
# 11. DICTIONARIES + INPUT
# ============================================================

favorite_foods = {}

name = input("What is your name? ")
food = input("What is your favorite food? ")

favorite_foods[name] = food

print(favorite_foods)


# ============================================================
# 12. LISTS VS DICTIONARIES
# ============================================================

# LIST:
#
# Lists use positions/indexes.

foods = ["Pizza", "Tacos", "Burger"]

print(foods[0])


# DICTIONARY:
#
# Dictionaries use keys.

foods = {
    "breakfast": "Pancakes",
    "lunch": "Pizza",
    "dinner": "Tacos"
}

print(foods["lunch"])


# ============================================================
# 13. IMPORTANT DICTIONARY PATTERN
# ============================================================

# Remember:

dictionary = {
    "key": "value"
}

# Access:

dictionary["key"]

# Change:

dictionary["key"] = "new value"

# Add:

dictionary["new_key"] = "new value"

# Remove:

dictionary.pop("key")

# Check:

if "key" in dictionary:
    print("It exists")


# ============================================================
# SUMMARY
# ============================================================

# Dictionaries store information as KEY : VALUE pairs.
#
# Create:
#
# person = {"name": "Alex", "age": 12}
#
# Get:
#
# person["name"]
#
# Change:
#
# person["age"] = 13
#
# Add:
#
# person["color"] = "Blue"
#
# Remove:
#
# person.pop("color")
#
# Loop:
#
# for key in person:
#     print(key, person[key])
#
# ============================================================