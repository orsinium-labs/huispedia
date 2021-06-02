import json
import re
from typing import Dict, List

import requests


rex_url = re.compile(r'href\=\"[^"]+' + re.escape('" class="property-card-container"'))
rex_json = re.compile(r'window\.HuispediaData \= (.+)\;')
rex_csrf = re.compile(re.escape('<meta name="csrf-token" content="') + '([^"]+)')


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'referer': 'https://huispedia.nl/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',  # noqa
}


def get_houses(
    query: str = "heel nederland",
    fsa: bool = True,   # for sale
    fso: bool = True,   # for sale by owner
    fsr: bool = True,   # for sale by broker
    ofb: bool = True,   # open for bid
    aot: bool = True,   # for rent
    sold: bool = False,
    fre: bool = False,  # soon for sale
    fro: bool = False,  # soon for sale by owner
    frr: bool = False,  # soon for sale by broker

    price_min: int = 0,
    price_max: int = 999000,
    plot_min: int = 0,
    plot_max: int = 299000,
    con_year_min: int = 1600,
    con_year_max: int = 2040,
    energy_labels=("A", "B", "C", "D", "E", "F"),
    rooms: int = 0,
    bedrooms: int = 0,

    object_type: str = "woonhuis",
) -> List[Dict[str, str]]:
    s = requests.Session()
    r = s.get('https://huispedia.nl/')
    r.raise_for_status()

    match = rex_csrf.search(r.text)
    if not match:
        raise ValueError('cannot find CSRF token')
    headers['x-csrf-token'] = match.group(1)
    headers['x-xsrf-token'] = s.cookies['XSRF-TOKEN']
    url = 'https://huispedia.nl/api/listings'
    r = s.get(url, headers=headers, params=dict(
        searchQueryState=json.dumps({
            "searchQuery": query,
            "filter": {
                "status": {
                    "fsa": fsa,
                    "fso": fso,
                    "fsr": fsr,
                    "ofb": ofb,
                    "aot": aot,
                    "sol": sold,
                    "fre": fre,
                    "fro": fro,
                    "frr": frr,
                },
                "price": {
                    "min": price_min,
                    "max": price_max,
                },
                "plot": {
                    "min": plot_min,
                    "max": plot_max,
                },
                "object_type": object_type,
                "con_year": {
                    "min": str(con_year_min),
                    "max": str(con_year_max),
                },
                "energy_labels": list(energy_labels),
                "rooms": rooms,
                "sleeping_rooms": bedrooms,
                "sort": "created_at_desc",
            },
            "map": {
                "bounds": {
                    "sw_lon": 2.7127496464753165,
                    "sw_lat": 50.53753990824933,
                    "ne_lon": 7.876323865225032,
                    "ne_lat": 53.543261308213005,
                },
            },
            "options": {"view": "list"},
        }),
        locationData="true",
    ))
    r.raise_for_status()
    return r.json()['data']['properties']
