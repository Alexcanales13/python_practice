inventory = []
item = ""
while item != "done" :
    item = input("Enter an item")
    if item != "done" :
        inventory.append(item)
    
print(inventory)