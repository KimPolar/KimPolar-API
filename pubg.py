import requests, json

def finder(accountId):
  headers = {
    "accept": "application/vnd.api+json",
    "Authorization": os.environ['PUBG-API-KEY']
  }
  
  if accountId.find("account.") != 0:
    accountId = requests.get(f"https://api.pubg.com/shards/steam/players?filter[playerNames]={accountId}", headers=headers).json()['data'][0]['id']
  weap = requests.get(f"https://prod-live-front.playbattlegrounds.com/").text.split('href="')[1].split("index-steam")[0]
  weap = requests.get(f"https://prod-live-front.playbattlegrounds.com{weap}app/_lib/Bro/translation/data/data_ko.json").json()
  
  survivalmastery = requests.get(f"https://api.pubg.com/shards/steam/players/{accountId}/survival_mastery", headers=headers).json()
  
  weapmastery = requests.get(f"https://api.pubg.com/shards/steam/players/{accountId}/weapon_mastery", headers=headers).json()
  weaps = list()
  for x in req['data']['attributes']['weaponSummaries'].keys():
    weaps.append({"WeapNm":weap["INGAME_ITEM:"+x]['name'],"Tier":req['data']['attributes']['weaponSummaries'][x]['TierCurrent'],"Level":req['data']['attributes']['weaponSummaries'][x]['LevelCurrent']})
  res = {"accountId":accountId, "Survival":{"Tier":survivalmastery['data']['attributes']['tier'],"Level":survivalmastery['data']['attributes']['level']}, "Weapon":weap}
  
  return res
