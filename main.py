import requests
import json
from a2s import A2SInfo, A2SPlayer

API_KEY = "953d9838-b77a-4823-a99c-44e9de511138"
gameID = "440"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

session = requests.Session()

# Get server address from the game client
server_address = None
with A2SInfo("hl2master.steampowered.com", 27011) as server:
    try:
        for info in server.filter(gamedir="tf"):
            if info.server_name == "Team Fortress":
                server_address = (info.server_address, info.server_port)
                break
        if not server_address:
            print("No TF2 server found.")
            exit(1)
    except:
        print("Master server query failed.")
        exit(1)

# Get list of players on the server
with A2SPlayer(server_address) as server:
    players = server.get_players()
steamIDs = [str(player.steamid) for player in players]

# Get inventory for each player
for steamID in steamIDs:
    response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID}/2", headers={"X-API-Key": API_KEY})

    with open("data.txt", "a") as f:
        f.write(jprint(response.json()) + "\n")