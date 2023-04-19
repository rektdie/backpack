import requests
import json
import valve.source.a2s

API_KEY = "953d9838-b77a-4823-a99c-44e9de511138"
gameID = "440"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

session = requests.Session()

# Get server address from the game client
server_address = None
with valve.source.a2s.MasterServerQuerier(region="all", timeout=5) as msq:
    try:
        for address in msq.find(region="all", gamedir="tf"):
            with valve.source.a2s.ServerQuerier(address) as server:
                if server.info()["server_name"] == "Team Fortress":
                    server_address = address
                    break
        if not server_address:
            print("No TF2 server found.")
            exit(1)
    except valve.source.NoResponseError:
        print("Master server query timed out.")
        exit(1)

# Get list of players on the server
with valve.source.a2s.ServerQuerier(server_address) as server:
    players = server.players()
steamIDs = [str(player["steamid"]) for player in players]

# Get inventory for each player
for steamID in steamIDs:
    response = session.get(f"https://hexa.one/api/v1/user/inventory/{steamID}/{gameID}/2", headers={"X-API-Key": API_KEY})

    with open("data.txt", "a") as f:
        f.write(jprint(response.json()) + "\n")
