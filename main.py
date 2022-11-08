import requests
from typing import Any

known_presidents = [
    'washington',
    'adams',
    'jefferson',
    'madison',
    'monroe',
    'adams',
    'jackson',
    'buren',
    'harrison',
    'tyler',
    'polk',
    'taylor',
    'fillmore',
    'pierce',
    'buchanan',
    'lincoln',
    'johnson',
    'grant',
    'hayes',
    'garfield',
    'arthur',
    'cleveland',
    'harrison',
    'cleveland',
    'mckinley',
    'roosevelt',
    'taft',
    'wilson',
    'harding',
    'coolidge',
    'hoover',
    'roosevelt',
    'truman',
    'eisenhower',
    'kennedy',
    'johnson',
    'nixon',
    'ford',
    'carter',
    'reagan',
    'bush',
    'clinton',
    'bush',
    'obama',
    'trump',
    'biden',
]


def query_ddg(query: str) -> dict[str, Any]:
    # queries duckduckgo for specified string
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error querying DuckDuckGo for {query}")
    return response.json()


def query_presidents() -> list[str]:
    # queries duckduckgo for presidents and filters the results based on known last names
    presidents_json = query_ddg("presidents+of+the+united+states")
    unfiltered = [key for key in presidents_json["RelatedTopics"]]
    presidents = []
    for president in unfiltered:
        last_name = president["Text"].split(" - ")[0].lower().split(" ")[-1]
        if last_name in known_presidents:
            presidents.append(president)

    return presidents
