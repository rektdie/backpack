import requests
import json

API_KEY = "1BE7CD78BC0E81FB9FF4B35A5D070429"

steamIDs = [
    76561198323251063, # Enyém
    76561199013264816 # Rolié
]

gameID = "730"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

response = requests.get(f"http://steamcommunity.com/inventory/{steamIDs[1]}/{gameID}/2")
print(response.status_code)

with open("data.txt", "w") as f:
    f.write(jprint(response.json()))
