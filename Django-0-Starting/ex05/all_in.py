import sys


def capital_city(s: str):
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

    if s in states.keys():
        print(f"{capital_cities[states[s]]} is the capital of {s}")
    elif s in capital_cities.values():
        for key, value in capital_cities.items():
            if value == s:
                t = key
                break
        for key, value in states.items():
            if value == t:
                print(f"{s} is the capital of {key}")
                break
    else:
        print(f"{s} is neither a capital city nor a state")


def my_capitalize(s):
    split = s.split()
    ret = str()
    for i in range(len(split)):
        t = split[i]
        ret = ret + t.capitalize()
        ret = ret + (" ")
    ret = ret.rstrip()
    # print(f"ret = [{ret}]")
    return ret

def my_main(l):
    for l in lst:
        t = l.lstrip().rstrip()
        if t != "":
            capital_city(my_capitalize(t))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lst = sys.argv[1].split(',')
        my_main(lst)
