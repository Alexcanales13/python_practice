# ============================================
#       GAME INVENTORY MANAGER
# ============================================

inventory = {
    "Potion": 3,
    "Sword": 1,
    "Shield": 1
}

while True:
    print("\n==============================")
    print("       INVENTORY MENU")
    print("==============================")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Check an item")
    print("4. Remove an item")
    print("5. Quit")
    print("==============================")

    choice = input("Choose an option: ")

    # VIEW INVENTORY
    if choice == "1":

        print("\nYour Inventory:")

        for item in inventory:
            print(item, ":", inventory[item])


    # ADD AN ITEM
    elif choice == "2":

        item = input("What item do you want to add? ")

        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

        print(item, "was added!")


    # CHECK AN ITEM
    elif choice == "3":

        item = input("What item do you want to check? ")

        if item in inventory:
            print("You have", inventory[item], item)
        else:
            print("You don't have that item.")


    # REMOVE AN ITEM
    elif choice == "4":

        item = input("What item do you want to remove? ")

        if item in inventory:
            inventory.pop(item)
            print(item, "was removed!")
        else:
            print("You don't have that item.")


    # QUIT
    elif choice == "5":

        print("Thanks for playing!")
        break


    # INVALID OPTION
    else:

        print("Invalid option.")