
# ==========================================
# GAME CLUB MANAGER - PRACTICE PROJECT
# ==========================================
#
# Concepts:
# - Sets
# - Tuples
# - Lists
# - Functions
# - Loops
# - If / elif / else
# - User input
#
# Complete every TODO!
# ==========================================


# Store unique usernames in a set.
registered_users = set()

# Store player profiles in a list.
# Each profile should be a tuple:
# (username, age, favorite_game)
player_profiles = []

# Store tournament participants in a set.
tournament_players = set()


# ------------------------------------------
# TASK 1: REGISTER A NEW PLAYER
# ------------------------------------------

def register_player():
    print("\n--- Register a New Player ---")

    # TODO 1:
    # Ask the user for a username.
    # Remove extra spaces using .strip().


    # TODO 2:
    # Check if the username is already in registered_users.
    # If it is, print an error message and return.


    # TODO 3:
    # Ask the user for their age.
    # Convert the answer into an integer.


    # TODO 4:
    # Ask the user for their favorite game.


    # TODO 5:
    # Create a tuple containing:
    # username, age, and favorite_game.


    # TODO 6:
    # Add the username to registered_users.


    # TODO 7:
    # Add the profile tuple to player_profiles.


    # TODO 8:
    # Print a success message.

    pass


# ------------------------------------------
# TASK 2: DISPLAY ALL PLAYERS
# ------------------------------------------

def show_players():
    print("\n--- Registered Players ---")

    # TODO 9:
    # If player_profiles is empty, print a message
    # and return.


    # TODO 10:
    # Use a for loop to go through player_profiles.


    # TODO 11:
    # Unpack each tuple into:
    # username, age, favorite_game


    # TODO 12:
    # Print each player's information.

    pass


# ------------------------------------------
# TASK 3: JOIN THE TOURNAMENT
# ------------------------------------------

def register_for_tournament():
    print("\n--- Tournament Registration ---")

    # TODO 13:
    # Ask the user for their username.


    # TODO 14:
    # Check if the username is in registered_users.
    # If not, print a message and return.


    # TODO 15:
    # Check if the username is already in tournament_players.
    # If so, print a message and return.


    # TODO 16:
    # Add the username to tournament_players.


    # TODO 17:
    # Print a success message.

    pass


# ------------------------------------------
# TASK 4: DISPLAY TOURNAMENT PLAYERS
# ------------------------------------------

def show_tournament():
    print("\n--- Tournament Players ---")

    # TODO 18:
    # Check whether tournament_players is empty.


    # TODO 19:
    # If it is not empty, loop through the set
    # and print every username.


    # TODO 20:
    # Print the total number of tournament players
    # using len().

    pass


# ------------------------------------------
# TASK 5: COMPARE CLUB AND TOURNAMENT MEMBERS
# ------------------------------------------

def compare_members():
    print("\n--- Club and Tournament Report ---")

    # TODO 21:
    # Use set intersection (&) to find players
    # who are in BOTH sets.


    # TODO 22:
    # Use set difference (-) to find club members
    # who are NOT in the tournament.


    # TODO 23:
    # Print both results.

    pass


# ------------------------------------------
# TASK 6: MAIN MENU
# ------------------------------------------

def main():
    while True:
        print("\n==============================")
        print("       GAME CLUB MANAGER")
        print("==============================")
        print("1. Register a new player")
        print("2. Show all players")
        print("3. Join the tournament")
        print("4. Show tournament players")
        print("5. Compare club and tournament")
        print("6. Show total club members")
        print("7. Quit")

        # TODO 24:
        # Ask the user to choose an option.


        # TODO 25:
        # If the choice is "1", call register_player().


        # TODO 26:
        # If the choice is "2", call show_players().


        # TODO 27:
        # If the choice is "3", call register_for_tournament().


        # TODO 28:
        # If the choice is "4", call show_tournament().


        # TODO 29:
        # If the choice is "5", call compare_members().


        # TODO 30:
        # If the choice is "6", print the number
        # of registered club members.


        # TODO 31:
        # If the choice is "7", print a goodbye message
        # and use break to exit the loop.


        # TODO 32:
        # If the user enters anything else,
        # print an invalid-choice message.

        pass


# ------------------------------------------
# START THE PROGRAM
# ------------------------------------------

# TODO 33:
# Call main() to start the program.
