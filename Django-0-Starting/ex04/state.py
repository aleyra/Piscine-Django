import sys


def state(city: str):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if city in capital_cities.values():
        for key, value in capital_cities.items():
            if value == city:
                t = key
                break
        for key, value in states.items():
            if value == t:
                print(f"{city} is the capital of {key}")
                return
    else:
        print("Unknown capital city")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        state(sys.argv[1])
