
from pokemon_api import get_pokemon, display_pokemon


def main():
    search_history = []

    print("Welcome to Pokemon Explorer!")
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Search Pokemon")
        print("2. View Search History")
        print("3. Clear Search History")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Pokemon name: ")

            data = get_pokemon(name)

            if data is not None:
                display_pokemon(data)
                search_history.append(data["name"])

            else:
                print("Pokemon could not be retrieved!")

        elif choice == "2":
            if len(search_history) == 0:
                print("No searches yet!")

            else:
                print("\n===== SEARCH HISTORY =====")

                for name in search_history:
                    print("-", name.title())

        elif choice == "3":
            search_history.clear()
            print("Search history cleared!")

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
