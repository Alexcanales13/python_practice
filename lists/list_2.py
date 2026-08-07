# === EXERCISE 2: List Methods ===

# 1. Create a list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 2. Add 7 to the end of the list

# 3. Insert 0 at the beginning of the list

# 4. Count how many times 5 appears in the list

# 5. Sort the list in ascending order

# 6. Reverse the list

# Your code here:
numbers=[3,1,4,1,5,9,2,6,5,3,5]
numbers.append(7)
numbers.insert(0,0)
print(numbers.count(5))
counter=0 
for number in numbers:
    if number == 5:
        counter+=1
print(counter)


numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)