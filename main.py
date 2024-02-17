import requests
import json
from steamid_converter import Converter
import re

API_KEY = "ea6b6952-e49d-43f4-887b-3a99da0fc452"

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
        with open("database.txt", "a+") as f:
            if (steamID not in f):
                f.write(steamID + '\n')
                try:
                    response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID}/2", headers={"X-API-Key": API_KEY}, timeout=10)
                    data = json.loads(response.text)
                    print(response.elapsed.total_seconds())

                    num_cases = 0
                    try:
                        for item in data['result']['inventory'].values():
                            if 'CSGO_Type_WeaponCase' in [tag['internal_name'] for tag in item['tags']]:
                                num_cases += item['amount']
                    except:
                        continue

                    if num_cases > 0:
                        with open("results.txt", "a") as f:
                                f.write(f"{num_cases} db: http://steamcommunity.com/profiles/{steamID}\n")
                except requests.exceptions.Timeout:
                    print("Timed out")
                    continue
            else:
                print(f"{steamID} already in database")