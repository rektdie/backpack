import requests
import json

API_KEY = "0K3XC6K5VRGZ5XFI"

steamIDs = [
    76561198323251063, # Enyém
    76561199013264816 # Rolié
]

gameID = "csgo"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

parameters = {
    "steam_id": steamIDs[1],
    "game": gameID,
    "language": "english",
    "parse": 0,
}

response = requests.get(f"https://steamwebapi.com/steam/api/inventory?key={API_KEY}", params=parameters)

with open("data.txt", "w") as f:
    f.write(jprint(response.json()))

print(response.status_code)