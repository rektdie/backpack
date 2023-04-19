import requests
import json
import time

API_KEY = "953d9838-b77a-4823-a99c-44e9de511138"

steamIDs = [
    76561198323251063, # Én
    76561199013264816, # Roli
    76561199067585535 # Peti
]

gameID = "730"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

session = requests.Session()

for steamID in steamIDs:
    response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID}/2", headers={"X-API-Key": API_KEY})

    with open("data.txt", "a") as f:
        f.write(jprint(response.json()) + "\n")
