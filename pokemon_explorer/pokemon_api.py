
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(name):
    url = BASE_URL + name.lower().strip()

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()

    return None


def display_pokemon(data):
    print("\n===== POKEMON STATS =====")

    print("Name:", data["name"].title())
    print("Height:", data["height"] / 10, "meters")
    print("Weight:", data["weight"] / 10, "kg")
    print("Base Experience:", data["base_experience"])

    print("\nTypes:")

    for item in data["types"]:
        print("-", item["type"]["name"].title())

    print("\nAbilities:")

    for item in data["abilities"]:
        print("-", item["ability"]["name"].title())

    print("\nBattle Stats:")

    for stat in data["stats"]:
        print(stat["stat"]["name"], ":", stat["base_stat"])
