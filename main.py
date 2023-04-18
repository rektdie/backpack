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

session = requests.Session()

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
}

for steamID in steamIDs:
    response = session.get(f"http://steamcommunity.com/inventory/{steamID}/{gameID}/2/?key={API_KEY}")

    print(response.status_code)

    with open("data.txt", "a") as f:
        f.write(jprint(response.json()) + "\n")
    time.sleep(30)
