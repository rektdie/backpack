import requests
import json
from steamid_converter import Converter
import re

API_KEY = "953d9838-b77a-4823-a99c-44e9de511138"

my_steam_id = "76561198323251063"

with open('results.txt', 'w'):
    pass

gameID = 730

steam3IDs = []
steamIDs = []

with open('input.txt', 'r', encoding="utf8") as f:
    content = f.read()

    steamids = re.findall(r'\[U:1:\d+\]', content)

    for steamid in steamids:
        steam3IDs.append(steamid)

for id in steam3IDs:
    steamIDs.append(Converter.to_steamID64(id, as_int=False))

session = requests.Session()

for steamID in steamIDs:
    if steamID != my_steam_id:
        response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID}/2", headers={"X-API-Key": API_KEY})
        data = json.loads(response.text)

        num_cases = 0
        try:
            for item in data['result']['inventory'].values():
                if 'CSGO_Type_WeaponCase' in [tag['internal_name'] for tag in item['tags']]:
                    num_cases += item['amount']
        except:
            continue

        with open("results.txt", "a") as f:
            if num_cases > 0:
                f.write(f"{num_cases} db: http://steamcommunity.com/profiles/{steamID}\n")