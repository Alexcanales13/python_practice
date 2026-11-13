# The Lost Kingdom 🏰
## Python RPG — Modular Game Development Project

**Developer:** Alex  
**Project:** The Lost Kingdom  
**Goal:** Build a complete text-based RPG using Python modules, classes, functions, and data structures.  
**Estimated time:** Multiple lessons  
**Important rule:** You are the developer! Your instructor can provide hints, but you are responsible for designing, writing, testing, and debugging your code.

---

## The Big Idea

You're building a text-based RPG called **The Lost Kingdom**.

Players will be able to:

- Create their own hero.
- Fight randomly generated enemies.
- Take damage and recover health.
- Collect gold after winning battles.
- Manage an inventory of items.
- Use health potions.
- Explore the kingdom.
- Eventually fight powerful bosses.

Instead of writing everything in one Python file, you will organize your game into **separate modules**.

Each module has its own responsibility.

By the end, your program should feel like a real game, not just a collection of disconnected exercises.

## Project Structure

Your project will contain five Python files:

```text
lost_kingdom/
│
├── main.py
├── player.py
├── enemy.py
├── combat.py
└── inventory.py
```

| File | Responsibility |
|---|---|
| `main.py` | Starts the game and manages the main menu |
| `player.py` | Defines the player and their abilities |
| `enemy.py` | Defines enemies and creates random encounters |
| `combat.py` | Controls turn-based battles |
| `inventory.py` | Manages items and potions |

**Think before coding:**

Why would keeping combat logic separate from the player class make the game easier to expand?

---

# Mission 1 — Build Your Hero

**Files:** `player.py` and `main.py`

**Concepts:** Classes, objects, attributes, methods, `self`, `__init__`, imports.

## Your Objective

Create a player character who can:

1. Remember their name, health, maximum health, attack power, and gold.
2. Display their statistics.
3. Take damage without health dropping below zero.
4. Heal without exceeding maximum health.
5. Be created and used from another Python file.

### Starting Statistics

| Attribute | Value |
|---|---:|
| Health | 100 |
| Maximum health | 100 |
| Attack | 15 |
| Gold | 10 |

### Example Output

```text
Welcome to The Lost Kingdom!

Enter your name: Alex

=== CHARACTER ===
Name: Alex
Health: 100/100
Attack: 15
Gold: 10

Alex takes 20 damage!
Health: 80/100

Alex heals 10 HP!
Health: 90/100
```

### Questions to Answer

- What is the purpose of `__init__`?
- Why do methods use `self`?
- What is the difference between a class and an object?
- How can one Python file import a class from another?
- How can you prevent health from becoming negative?

### Testing Checklist

- [ ] Player can display their statistics.
- [ ] Taking 20 damage reduces health to 80.
- [ ] Healing 10 points increases health to 90.
- [ ] Taking 500 damage does not produce negative health.
- [ ] Healing never exceeds maximum health.
- [ ] `main.py` successfully imports `Player`.

---

# Mission 2 — Create the Enemy System

**File:** `enemy.py`

**Concepts:** Classes, dictionaries, lists, random numbers, functions.

## Your Objective

Create enemies that your player can eventually fight.

Each enemy should have:

- A name.
- Health and maximum health.
- Attack power.
- A gold reward.

### Enemy Types

| Enemy | Health | Attack | Gold Reward |
|---|---:|---:|---:|
| Green Slime | 30 | 5 | 5 |
| Goblin | 50 | 10 | 12 |
| Skeleton Warrior | 75 | 14 | 20 |
| Ancient Dragon | 200 | 25 | 100 |

### Requirements

Your enemy system should:

1. Define an `Enemy` class.
2. Allow enemies to take damage.
3. Determine whether an enemy is alive.
4. Display enemy statistics.
5. Allow an enemy to attack a player.
6. Randomly create a Slime, Goblin, or Skeleton for ordinary encounters.
7. Provide a separate way to create the Ancient Dragon boss.

### Example Output

```text
A wild Goblin appears!

Enemy: Goblin
Health: 50/50
Attack: 10

Goblin attacks!
Alex takes 12 damage!
```

### Questions to Answer

- How is an enemy similar to a player?
- Should every enemy have its own class?
- How could a dictionary store different enemy statistics?
- How does `random.choice()` work?
- How can one object call a method belonging to another object?

### Testing Checklist

- [ ] Enemies are created with the correct attributes.
- [ ] Enemies can take damage.
- [ ] Enemy health cannot become negative.
- [ ] Enemy attacks affect the player's health.
- [ ] Random encounters produce different enemies.
- [ ] The Ancient Dragon is excluded from ordinary encounters.

---

# Mission 3 — Build the Combat System

**File:** `combat.py`

**Concepts:** Functions, `while` loops, conditionals, randomness, imports, object interactions.

## Your Objective

Create a turn-based battle system where the player fights an enemy until someone wins or the player escapes.

### Combat Menu

```text
===== BATTLE =====

Alex: 100 HP
Goblin: 50 HP

1. Attack
2. Heal
3. Run

Choose an action:
```

### Requirements

1. Display the player's and enemy's current health.
2. Let the player choose an action.
3. Generate random attack damage.
4. Give the player a 15% chance to land a critical hit that deals double damage.
5. Allow the player to heal during battle.
6. Give the player a 50% chance to escape.
7. Allow the enemy to attack after the player's turn.
8. Stop combat when the enemy or player reaches zero health.
9. Reward the player with gold after defeating an enemy.
10. Prevent defeated enemies from attacking.

### Example Battle

```text
A wild Green Slime appears!

===== BATTLE =====
Alex: 100 HP
Green Slime: 30 HP

1. Attack
2. Heal
3. Run

Choose an action: 1

CRITICAL HIT!
Green Slime takes 28 damage!

Green Slime attacks!
Alex takes 4 damage!

===== BATTLE =====
Alex: 96 HP
Green Slime: 2 HP

Choose an action: 1

Green Slime takes 14 damage!

You defeated Green Slime!
You earned 5 gold!
```

### Design Questions

- Why should combat have its own module?
- What kind of loop keeps a battle running?
- How do you determine whose turn it is?
- How can you prevent an enemy from attacking after being defeated?
- How could combat return information to `main.py` about the battle result?

### Testing Checklist

- [ ] Player can attack enemies.
- [ ] Enemy can attack the player.
- [ ] Critical hits sometimes occur.
- [ ] Combat ends when an enemy is defeated.
- [ ] Combat ends when the player is defeated.
- [ ] Successful escape ends combat.
- [ ] Invalid menu choices do not cause crashes.
- [ ] Gold rewards are only given for victories.

---

# Mission 4 — Create the Inventory System

**File:** `inventory.py`

**Concepts:** Dictionaries, loops, methods, conditional logic, validation.

## Your Objective

Create an inventory system that tracks the items a player owns.

Your inventory must support:

1. Adding items.
2. Removing items.
3. Checking whether an item exists.
4. Tracking quantities.
5. Displaying all items.
6. Using health potions.

### Starting Inventory

| Item | Quantity | Effect |
|---|---:|---|
| Health Potion | 3 | Restores up to 25 HP |

### Example Output

```text
===== INVENTORY =====

Health Potion: 3

You used a Health Potion!
Alex heals 25 HP!

===== INVENTORY =====

Health Potion: 2
```

### Requirements

- Items must have quantities.
- Adding an existing item should increase its quantity.
- Removing an item should decrease its quantity.
- An item should disappear when its quantity reaches zero.
- The player cannot use an item they don't own.
- The player cannot consume a potion when their health is already full.
- Health cannot exceed maximum health.

### Design Questions

- Would a list or dictionary be better for storing item quantities?
- How can you check whether an item exists?
- What should happen if a player tries to remove five potions but owns only two?
- Why should inventory logic be separate from combat logic?

### Testing Checklist

- [ ] Adding items works.
- [ ] Adding the same item increases its quantity.
- [ ] Removing items decreases their quantity.
- [ ] Removing the final item deletes its entry.
- [ ] The player cannot remove more items than they own.
- [ ] Potions restore health.
- [ ] Potions are consumed when used successfully.

---

# Mission 5 — Connect Everything

**File:** `main.py`

**Concepts:** Imports, loops, functions, conditionals, modular architecture.

## Your Objective

Connect all your modules into one playable game.

Your main menu should look similar to this:

```text
===== THE LOST KINGDOM =====

1. View Character
2. Explore / Fight Enemy
3. View Inventory
4. Use Health Potion
5. Rest
6. Quit

Choose an option:
```

### Menu Requirements

**Option 1 — View Character**

Display the player's name, health, attack, and gold.

**Option 2 — Explore**

Generate a random enemy and start a battle.

**Option 3 — View Inventory**

Display the player's items and quantities.

**Option 4 — Use Health Potion**

Use a potion from the player's inventory to restore health.

**Option 5 — Rest**

Restore the player's health to its maximum value.

**Option 6 — Quit**

End the game gracefully.

### Important Rules

- The menu should continue running until the player quits or is defeated.
- Invalid input should not crash the program.
- The player's statistics should persist between menu actions.
- Gold earned from battles should remain available.
- Items consumed from inventory should not reappear automatically.
- The game should not create a new player every time the menu repeats.

### Final Integration Test

- [ ] The game starts using `python main.py`.
- [ ] The player can view their statistics.
- [ ] Random enemies appear.
- [ ] Battles work correctly.
- [ ] Gold increases after winning.
- [ ] Inventory quantities are updated.
- [ ] Health potions work.
- [ ] Rest restores health.
- [ ] The game exits properly.

---

# Advanced Challenges

Complete these after your five modules work.

## Challenge A — Experience and Leveling

Add an experience system.

- Players earn XP from defeating enemies.
- Every 100 XP, the player levels up.
- Leveling up increases maximum health and attack power.
- Extra XP should carry over toward the next level.

**Question:** Which module should control leveling up?

## Challenge B — Smarter Enemies

Give enemies different behaviors.

- Slimes attack normally.
- Goblins occasionally dodge attacks.
- Skeletons sometimes deal bonus damage.
- Dragons have powerful special attacks.

**Question:** How can you support different enemy behaviors without rewriting the entire combat system?

## Challenge C — Better Inventory

Add new items:

- Strong Health Potion
- Iron Sword
- Wooden Shield
- Magic Scroll

Make different items have different effects.

**Question:** How could you represent item effects using dictionaries or classes?

## Challenge D — Combat Improvements

Add:

- Defense.
- Critical hit messages.
- Limited healing during battle.
- Enemy difficulty scaling.
- Special attacks.

**Question:** How can you prevent combat rules from becoming too complicated to maintain?

## Challenge E — Boss Battle

The Ancient Dragon becomes available after the player defeats five enemies.

Requirements:

- Track victories.
- Unlock the boss after five victories.
- Give the boss special abilities.
- Display a victory message when the dragon is defeated.

## Challenge F — Save and Load

Create an additional module called `save_load.py`.

Save the player's:

- Name.
- Health.
- Level and XP.
- Gold.
- Inventory.
- Number of victories.

Use JSON to save progress to a file.

**Question:** How can you turn an object's information into data that can be saved and reconstructed later?

## Challenge G — Automated Testing

Create a `test_game.py` file using Python's `unittest` module.

Write tests for:

- Damage calculations.
- Healing limits.
- Item quantities.
- Gold rewards.
- Leveling behavior.

**Question:** Why are automated tests useful when your project becomes larger?

---

# Concepts You'll Practice

| Python Concept | Where You'll Use It |
|---|---|
| Variables and data types | Player and enemy statistics |
| Input and output | Menus and player choices |
| Conditional statements | Combat decisions and validation |
| `for` and `while` loops | Inventory display and battles |
| Lists | Enemy choices and item collections |
| Dictionaries | Enemy statistics and inventory |
| Functions | Game actions and combat |
| Classes and objects | Player, Enemy, Inventory |
| `__init__` and `self` | Object initialization and methods |
| Modules and imports | Connecting the game files |
| Random numbers | Encounters, damage, critical hits |
| List comprehensions | Filtering available enemy types |
| Sets and tuples | Future exploration and map features |
| File handling | Future save/load system |
| Testing and debugging | Checking that each module works |

---

# Definition of Done

Your game is complete when:

1. All five Python files work together.
2. You can create a player and interact with the game menu.
3. Enemies appear and can fight the player.
4. The player can win battles and earn gold.
5. The inventory tracks items correctly.
6. Potions restore health and are consumed.
7. Invalid input is handled appropriately.
8. The game runs without import errors.
9. You can explain what each module is responsible for.
10. You can explain how information moves between the modules.

---

# Final Reflection

Answer these questions:

1. Which module was the hardest to build?
2. What was the most difficult bug you fixed?
3. Why did we separate the game into five Python files?
4. How does `combat.py` interact with `player.py` and `enemy.py`?
5. Why is a dictionary useful for an inventory?
6. What would happen if we tried to put all this code inside `main.py`?
7. What feature would you like to add next?

**Remember: You're not just learning Python syntax anymore. You're learning how to design and build software.**

Make the game your own!