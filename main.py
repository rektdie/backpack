import requests
import json
from steamid_converter import Converter
import re

API_KEY = "ea6b6952-e49d-43f4-887b-3a99da0fc452"

my_steam_id = "76561198323251063"

with open('results.txt', 'w'):
    pass

gameID1 = 440
gameID2 = 730

caseNames = [
    "End of the Line Community Crate Series",
    "End of the Line Community Crate Series #87",
    "Mann Co. Supply Crate Series #21",
    "Infernal Reward War Paint Case",
    "Mann Co. Supply Crate Series #31",
    "Mann Co. Supply Munition Series #83",
    "Pallet of Crates",
    "Unlocked Cosmetic Crate Demo",
    "Unlocked Creepy Scout Crate",
    "Unlocked Creepy Engineer Crate",
    "Unlocked Creepy Pyro Crate",
    "Unlocked Cosmetic Crate Pyro",
    "Mann Co. Supply Crate Series #14",
    "Mann Co. Supply Crate Series #1",
    "Mann Co. Supply Crate Series #5",
    "Mann Co. Supply Crate Series #11",
    "Mann Co. Supply Crate Series #13",
    "Mann Co. Supply Crate Series #2",
    "Mann Co. Supply Crate Series #1",
    "Mann Co. Supply Crate Series #5",
    "Mann Co. Supply Crate Series #10",
    "Mann Co. Supply Crate Series #14",
    "Mann Co. Supply Crate Series #19",
    "Mann Co. Supply Crate Series #20",
    "Mann Co. Supply Crate Series #4",
    "Mann Co. Supply Crate Series #21",
    "Mann Co. Supply Crate Series #12",
    "Mann Co. Supply Crate Series #8",
    "Mann Co. Supply Crate Series #8",
    "Mann Co. Supply Crate Series #25",
    "End of the Line Community Crate Series #87",
    "Mann Co. Director's Cut Reel",
    "Gargoyle Case",
    "Violet Vermin Case",
    "Creepy Crawly Case",
    "Confidential Collection Case",
    "Pyroland Weapons Case",
    "Quarantined Collection Case",
    "The Powerhouse Weapons Case",
    "Gun Mettle Cosmetic Case",
    "Tough Break Cosmetic Case",
    "The Concealed Killer Weapons Case",
    "Winter 2017 War Paint Case",
    "Mann Co. Supply Munition Series #83",
    "Mann Co. Audition Reel",
    "Mann Co. Director's Cut Reel",
    "Salvaged Mann Co. Supply Crate Series #40",
    "Salvaged Mann Co. Supply Crate Series #30",
    "Mann Co. Supply Crate Series #15",
    "Select Reserve Mann Co. Supply Crate Series #60",
    "Mann Co. Supply Crate Series #25",
    "Mann Co. Supply Crate Series #9",
    "Mann Co. Supply Crate Series #18",
    "Mann Co. Supply Crate Series #33",
    "Mann Co. Supply Crate Series #28",
    "Mann Co. Supply Crate Series #7",
    "Mann Co. Supply Crate Series #8",
]

excludedCases = [
    "Recoil Case",
    "Fracture Case",
    "Snakebite Case",
    "Revolution Case",
]

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

databaseContent = []

with open("database.txt", "r") as f:
    databaseContent = f.read().splitlines()

for steamID in steamIDs:
    if steamID != my_steam_id:
        if (steamID not in databaseContent):
            try:
                response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID1}/2", headers={"X-API-Key": API_KEY}, timeout=10)
                data = json.loads(response.text)
                print(response.elapsed.total_seconds())

                num_cases = 0

                foundCases = []

                for item in data['result']['inventory'].values():
                    if item['market_name'] in caseNames:
                        num_cases += item['amount']
                        if item['market_name'] not in foundCases:
                            foundCases.append(item['market_name'])

                if num_cases > 0:
                    with open("results.txt", "a") as e:
                        e.write("Tf2 items\n")
                        for case in foundCases:
                            e.write(f"{case}, ")
                        e.write('\n')
                        e.write(f"{num_cases} db: http://steamcommunity.com/profiles/{steamID}/inventory\n\n")
            except TimeoutError:
                print("Timed out")
            except:
                print("Private inventory")

            try:
                response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID2}/2", headers={"X-API-Key": API_KEY}, timeout=10)
                data = json.loads(response.text)
                print(response.elapsed.total_seconds())

                num_cases = 0
                try:
                    for item in data['result']['inventory'].values():
                        if 'CSGO_Type_WeaponCase' in [tag['internal_name'] for tag in item['tags']]:
                            if (item["market_name"] not in excludedCases):
                                num_cases += item['amount']
                except:
                    continue

                if num_cases > 0:
                    with open("results.txt", "a") as e:
                        e.write("CS2 items\n")
                        e.write(f"{num_cases} db: http://steamcommunity.com/profiles/{steamID}/inventory\n\n")
            except TimeoutError:
                print("Timed out")
                continue
            except:
                print("Private inventory")

            with open("database.txt", "a") as f:
                f.write(steamID + '\n')
        else:
            print(f"{steamID} already in database")