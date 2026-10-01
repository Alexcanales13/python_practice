# ============================================================
#                  RANDOM RPG ADVENTURE
# ============================================================

import random


# ============================================================
# STARTING DATA
# ============================================================

player = {
    "name": "",
    "health": 100,
    "gold": 50,
    "level": 1,
    "xp": 0,
    "inventory": []
}

enemies = [
    "Goblin",
    "Skeleton",
    "Wolf",
    "Orc",
    "Dragon"
]

items = [
    "Potion",
    "Sword",
    "Shield",
    "Magic Stone"
]


# ============================================================
# CREATE PLAYER
# ============================================================

def create_player():

    name = input("What is your name? ")

    player["name"] = name

    return player


# ============================================================
# SHOW PLAYER
# ============================================================

def show_player(player):

    print("\n===== PLAYER =====")
    print("Name:", player["name"])
    print("Health:", player["health"])
    print("Gold:", player["gold"])
    print("Level:", player["level"])
    print("XP:", player["xp"])

    print("Inventory:")

    if len(player["inventory"]) == 0:
        print("Empty")

    else:
        for item in player["inventory"]:
            print("-", item)


# ============================================================
# FIND ITEM
# ============================================================

def find_item(player):

    item = random.choice(items)

    print("\nYou found a", item + "!")

    player["inventory"].append(item)


# ============================================================
# FIND GOLD
# ============================================================

def find_gold(player):

    gold = random.randint(10, 50)

    player["gold"] = player["gold"] + gold

    print("\nYou found", gold, "gold!")


# ============================================================
# FIGHT ENEMY
# ============================================================

def fight_enemy(player):

    enemy = random.choice(enemies)

    enemy_health = random.randint(20, 80)

    print("\nA", enemy, "appeared!")
    print("Enemy health:", enemy_health)

    while enemy_health > 0 and player["health"] > 0:

        print("\nYour health:", player["health"])
        print(enemy, "health:", enemy_health)

        damage = random.randint(10, 30)

        # Critical hit
        critical = random.randint(1, 10)

        if critical == 10:
            damage = damage * 2
            print("CRITICAL HIT!")

        enemy_health = enemy_health - damage

        print("You attacked for", damage, "damage!")

        if enemy_health <= 0:
            break

        enemy_damage = random.randint(5, 20)

        player["health"] = player["health"] - enemy_damage

        print(enemy, "attacked you for", enemy_damage, "damage!")

    # Player won
    if player["health"] > 0:

        print("\nYou defeated the", enemy + "!")

        player["gold"] = player["gold"] + 20
        player["xp"] = player["xp"] + 1

        print("You gained 20 gold!")
        print("You gained 1 XP!")

        # Level up
        if player["xp"] >= 3:

            player["level"] = player["level"] + 1
            player["xp"] = 0

            print("\n===== LEVEL UP! =====")
            print("You are now level", player["level"])

    # Player lost
    else:

        print("\nYou were defeated!")
        print("Game over!")


# ============================================================
# USE POTION
# ============================================================

def use_potion(player):

    if "Potion" in player["inventory"]:

        player["inventory"].remove("Potion")

        player["health"] = player["health"] + 25

        if player["health"] > 100:
            player["health"] = 100

        print("\nYou used a Potion!")
        print("Health:", player["health"])

    else:

        print("\nYou don't have a Potion!")


# ============================================================
# EXPLORE
# ============================================================

def explore(player):

    events = [
        "item",
        "enemy",
        "gold",
        "nothing"
    ]

    event = random.choice(events)

    print("\nYou explore the area...")

    if event == "item":

        find_item(player)

    elif event == "enemy":

        fight_enemy(player)

    elif event == "gold":

        find_gold(player)

    else:

        print("You found nothing.")


# ============================================================
# SHOW INVENTORY
# ============================================================

def show_inventory(player):

    print("\n===== INVENTORY =====")

    if len(player["inventory"]) == 0:

        print("Your inventory is empty.")

    else:

        for item in player["inventory"]:
            print("-", item)


# ============================================================
# CREATE THE PLAYER
# ============================================================

player = create_player()


# ============================================================
# MAIN GAME LOOP
# ============================================================

while True:

    print("\n==============================")
    print("       RPG ADVENTURE")
    print("==============================")

    print("1. Show Player")
    print("2. Explore")
    print("3. Use Potion")
    print("4. View Inventory")
    print("5. Quit")

    choice = input("\nChoose an option: ")

    # --------------------------------------------------------
    # SHOW PLAYER
    # --------------------------------------------------------

    if choice == "1":

        show_player(player)

    # --------------------------------------------------------
    # EXPLORE
    # --------------------------------------------------------

    elif choice == "2":

        if player["health"] > 0:
            explore(player)

        else:
            print("\nYou cannot explore because you are defeated.")

    # --------------------------------------------------------
    # USE POTION
    # --------------------------------------------------------

    elif choice == "3":

        use_potion(player)

    # --------------------------------------------------------
    # INVENTORY
    # --------------------------------------------------------

    elif choice == "4":

        show_inventory(player)

    # --------------------------------------------------------
    # QUIT
    # --------------------------------------------------------

    elif choice == "5":

        print("\nThanks for playing!")
        break

    # --------------------------------------------------------
    # INVALID OPTION
    # --------------------------------------------------------

    else:

        print("\nInvalid option.")