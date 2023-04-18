import requests
import json

API_KEY = "1BE7CD78BC0E81FB9FF4B35A5D070429"

steamIDs = [
    76561198323251063, # Enyém
    76561199013264816 # Rolié
]

gameID = "730"

with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


for proxy in proxies:
    try:
        response = requests.get(f"http://steamcommunity.com/inventory/{steamIDs[0]}/{gameID}/2", proxies={"http": proxy, "https": proxy})
        print(proxy)
    except:
        continue

    if response.status_code == 200:
        print(response.status_code)


with open("data.txt", "w") as f:
    f.write(jprint(response.json()))
