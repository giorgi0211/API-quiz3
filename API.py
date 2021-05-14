import requests
import json
import sqlite3
conn = sqlite3.connect('NBA_db.sqlite')
cursor = conn.cursor()

url = "https://www.balldontlie.io/api/v1/players"
req = requests.get(url)
print(req.status_code)
print(req.headers)
result_json = req.text
res = json.loads(result_json)
nba_json = json.dumps(res, indent=4)
print(nba_json)
with open ('nba_json', 'w') as f:
    json.dump(res, f, indent=4)
list1 = []
for each in range(0,25):
    list1.append(res['data'][each]['team']['name'])
    team = each['team']['name']
    cursor.execute("INSERT INTO NBATeams team VALUES team ")
print(list1)

a = res['data'][1]['id']
print(a)

nba = conn.execute('''CREATE TABLE NBATeams
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    teams VARCHAR(30))''')
conn.commit()           # mocemul savarjishoshi shevqmeni baza sadac gamovsaxe gundebi, kerdzod mati saxelebi, ufro sworad mindoda gamomesaxa tumca errors migdebs, kerdzod, line 20 TypeError: 'int' object is not subscriptable da ver mivxvdi samwuxarod rato mierorebda.