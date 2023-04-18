import requests
import json
import time

API_KEY = "1BE7CD78BC0E81FB9FF4B35A5D070429"

steamIDs = [
    76561198323251063, # Én
    76561199013264816, # Roli
    76561199067585535 # Peti
]

gameID = "730"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

for steamID in steamIDs:
    response = requests.get(f"http://steamcommunity.com/inventory/{steamID}/{gameID}/2")
    
    print(response.status_code)

    with open("data.txt", "a") as f:
        f.write(jprint(response.json()) + "\n")
    time.sleep(1)
