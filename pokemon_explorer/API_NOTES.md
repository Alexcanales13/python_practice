# Understanding APIs with Python

**Student:** Alex  
**Project:** Pokémon Explorer  
**Lesson goal:** Learn how Python programs request and process information from other services.

## 1. What is an API?

API stands for **Application Programming Interface**. An API defines how software can interact with other software. A web API allows programs to communicate over a network.

Think of a restaurant: you order food from a menu, the kitchen prepares it, and you receive your meal. Similarly, your Python program sends a request to a web API and receives a response.

| Term | Meaning |
|---|---|
| Client | The program making a request |
| Server | The service processing the request |
| Request | A message asking for information or an action |
| Response | The message returned by the server |
| Endpoint | An address where an API exposes a resource or operation |

Examples of applications that use APIs include weather apps, games, maps and online stores.

## 2. How does a web API work?

```text
Python program ---- HTTP request ----> API server
Python program <--- HTTP response ---- API server
```

Our Pokémon Explorer does not need to store every Pokémon. It asks PokéAPI for information when the user searches.

## 3. Understanding URLs and endpoints

Open this address in your browser:

https://pokeapi.co/api/v2/pokemon/pikachu

| URL part | Purpose |
|---|---|
| `https://` | Secure HTTP communication |
| `pokeapi.co` | Server hostname |
| `/api/v2` | API version path |
| `/pokemon` | Resource collection |
| `/pikachu` | Specific Pokémon |

**Try it:** Change the final part to `charizard`, `bulbasaur`, or `venusaur`. What changes in the response?

## 4. Making an API call in Python

Install the requests library in your terminal:

```bash
python -m pip install requests
```

Create a temporary file named `api_practice.py`:

```python
import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url, timeout=10)

print(response.status_code)
```

- `import requests` gives us tools for HTTP requests.
- `requests.get()` sends a GET request.
- `timeout=10` prevents an indefinite wait for network activity.
- `response` contains the server's response.
- `response.status_code` tells us the HTTP result.

Expected result for a successful request: `200`.

## 5. HTTP methods

| Method | Common purpose |
|---|---|
| GET | Retrieve information |
| POST | Submit information or create a resource |
| PUT | Replace a resource |
| PATCH | Update part of a resource |
| DELETE | Remove a resource |

Today we focus on GET. PokéAPI provides public read-only data without requiring an API key for these requests.

## 6. HTTP status codes

| Code | Meaning |
|---|---|
| 200 | OK — successful request |
| 400 | Bad request |
| 401 | Authentication required or invalid |
| 403 | Access forbidden |
| 404 | Resource not found |
| 429 | Too many requests |
| 500 | Internal server error |

Try requesting `pikachu` and then `pikahu`. Predict the status codes before running the program. A successful request normally returns 200; a nonexistent Pokémon normally returns 404.

## 7. What is JSON?

JSON stands for **JavaScript Object Notation**. It is a text format used to exchange structured data.

Simplified example:

```json
{
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "abilities": [
        {"ability": {"name": "static"}},
        {"ability": {"name": "lightning-rod"}}
    ]
}
```

JSON objects become Python dictionaries, arrays become lists, and JSON null becomes Python None when parsed.

```python
if response.status_code == 200:
    data = response.json()
    print(type(data))
    print(data["name"])
else:
    print("Request failed:", response.status_code)
```

`response.json()` parses the response body into Python data. It does not send another request. Not every response contains valid JSON.

PokéAPI reports height in decimeters and weight in hectograms. Divide each by 10 to display meters and kilograms.

## 8. Nested dictionaries and lists

Using the simplified JSON above:

```python
print(data["abilities"][0]["ability"]["name"])
```

Expected output: `static`.

Read the expression from left to right: select the abilities list, select its first dictionary, select the ability dictionary, then select its name.

## 9. Modular project structure

```text
pokemon_explorer/
├── main.py
└── pokemon_api.py
```

`main.py` handles user input, menus and search history. `pokemon_api.py` handles requests and processing Pokémon data. Keeping responsibilities separate makes the program easier to test and reuse.

## 10. Practice challenges

Complete these independently using your existing project:

- [ ] Ask the user for a Pokémon name and construct a URL dynamically.
- [ ] Normalize input so capital letters and surrounding spaces work.
- [ ] Display the HTTP status code.
- [ ] Display the Pokémon's name, height and weight.
- [ ] Use a for loop to display every ability and type.
- [ ] Find the highest battle statistic.
- [ ] Handle an unsuccessful request without trying to parse it as Pokémon data.
- [ ] Allow repeated searches and store successful searches in a list.
- [ ] Bonus: use a set to track unique searches.
- [ ] Bonus: handle connection errors and timeouts using try and except.

## 11. Debugging tips

If a search fails, check the spelling, URL and status code. Remember to select option 1 in the main menu before entering a Pokémon name. A network failure may raise an exception rather than return a status code.

## 12. Review questions

1. What does API stand for?
2. What is the difference between a client and a server?
3. What does a GET request do?
4. What is an endpoint?
5. What is the difference between status codes 200 and 404?
6. What is JSON, and how do we convert it into Python data?
7. Why do we need a loop to display all abilities?
8. Why do we separate the API module from the main program?
9. What happens if the internet connection fails?
10. Name another application you could build using an API.

**Remember:** You do not need to memorize every API. Learn to read documentation, inspect responses, and use the Python concepts you already know.

Reference: https://pokeapi.co/docs/v2
