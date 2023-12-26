import requests, json, os

def finder(accountId):
  headers = {
    "accept": "application/vnd.api+json",
    "Authorization": os.environ['PUBG-API-KEY']
  }
  
  if accountId.find("account.") != 0:
    accountId = requests.get(f"https://api.pubg.com/shards/steam/players?filter[playerNames]={accountId}", headers=headers)
    if accountId.status_code != 200:
      return {"code":accountId.status_code}
    accountId = accountId.json()['data'][0]['id']
  weap = requests.get(f"https://prod-live-front.playbattlegrounds.com/").text.split('href="')[1].split("index-steam")[0]
  weap = requests.get(f"https://prod-live-front.playbattlegrounds.com{weap}app/_lib/Bro/translation/data/data_ko.json").json()
  
  survivalmastery = requests.get(f"https://api.pubg.com/shards/steam/players/{accountId}/survival_mastery", headers=headers)
  if survivalmastery.status_code != 200:
    return {"code":survivalmastery.status_code}
  survivalmastery = survivalmastery.json()

  weapmastery = requests.get(f"https://api.pubg.com/shards/steam/players/{accountId}/weapon_mastery", headers=headers)
  if weapmastery.status_code != 200:
    return {"code":weapmastery.status_code}
  weapmastery = weapmastery.json()
  weaps = list()
  for x in weapmastery['data']['attributes']['weaponSummaries'].keys():
    weaps.append({"WeapNm":weap["INGAME_ITEM:"+x]['name'],"Tier":weapmastery['data']['attributes']['weaponSummaries'][x]['TierCurrent'],"Level":weapmastery['data']['attributes']['weaponSummaries'][x]['LevelCurrent']})
  res = {"code":200,"data":{"accountId":accountId, "Survival":{"Tier":survivalmastery['data']['attributes']['tier'],"Level":survivalmastery['data']['attributes']['level']}, "Weapon":weaps}}
 
  return res
