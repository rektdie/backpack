import requests
import json

API_KEY = "953d9838-b77a-4823-a99c-44e9de511138"
STEAM_KEY = "1BE7CD78BC0E81FB9FF4B35A5D070429"

gameID = 730

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

steamIDs = []

response = requests.get(f"https://api.steampowered.com/ISteamApps/GetServerPlayers/v1/?key={STEAM_KEY}&format=json&filter=ip:169.254.162.5:4984")
print(response.content)
"""
try:
    players = response.json()["response"]["players"]
    for player in players:
        steamIDs.append(player["steamid"])
except json.decoder.JSONDecodeError:
    print("Error: Response was not valid JSON.")
    print("Response status code:", response.status_code)
    print("Response content:", response.content)

session = requests.Session()

# Get inventory for each player
for steamID in steamIDs:
    response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID}/2", headers={"X-API-Key": API_KEY})
    with open("data.txt", "a") as f:
        f.write(jprint(response.json()) + "\n")
"""
