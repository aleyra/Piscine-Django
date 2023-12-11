import requests
import json
import dewiki
import sys


def print_rouge(s):
    print("\033[91m" + s + "\033[00m")


def request_wikipedia(to_search):

    s = requests.Session()

    url_api = "https://en.wikipedia.org/w/api.php"

    # check if we can have a result
    params1 = {
        "action": "opensearch",
        "format": "json",
        "search": to_search
    }

    try:
        r = s.get(url=url_api, params=params1)
        js = r.json()
        if len(js) == 0:
            raise Exception(f"no results found for {to_search}")
    except Exception as err:
        raise Exception(err)
    
    # print_rouge("we can have a result")  #

    params2 = {
        "action": "parse",
        "page": to_search,
        "format": "json",
        "prop": "wikitext",  # to get the text of the search
        "redirects": "true"  # to get the redirection
    }
    
    try:
        r = s.get(url=url_api, params=params2)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    # print_rouge("2st try ok")  #
    
    try:
        data : dict = json.loads(r.text)
        if "parse" not in data.keys():
            raise Exception("issue while converting JSON")
        data_parse = data["parse"]
        data_wikitext = data_parse["wikitext"]
        wikitext = data_wikitext["*"]
        return dewiki.from_string(wikitext)  # ici ça boude
    except Exception as err:
        raise Exception(err)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        # print_rouge("let's go")  #
        print(request_wikipedia(sys.argv[1]))