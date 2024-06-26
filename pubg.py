import requests, json, os

def userinfo(playerNm):
  headers = {
    "accept": "application/vnd.api+json",
    "Authorization": os.environ['PUBG-API-KEY']
  }
  player = requests.get(f"https://api.pubg.com/shards/steam/players?filter[playerNames]={playerNm}", headers=headers).json()['data'][0]
  res = dict()
  res['accountId'] = player['id']
  res['accountNm'] = player['attributes']['name']
  res['shardId'] = player['attributes']['shardId']
  res['banType'] = player['attributes']['banType']
  mastery = requests.get("https://api.pubg.com/shards/steam/players/"+res['accountId']+"/survival_mastery", headers=headers).json()['data']['attributes']
  res['matchPlayed'] = mastery['totalMatchesPlayed']
  res['levelTier'] = mastery['tier']
  res['level'] = mastery['level']
  res['totalLevel'] = mastery['level'] + ((mastery['tier']-1)*500)
  return res
  
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
    weaps.append({"WeapNm":weap["INGAME_ITEM:"+x]['name'],"WeapCd":x,"Tier":weapmastery['data']['attributes']['weaponSummaries'][x]['TierCurrent'],"Level":weapmastery['data']['attributes']['weaponSummaries'][x]['LevelCurrent']})
  res = {"code":200,"data":{"accountId":accountId, "Survival":{"Tier":survivalmastery['data']['attributes']['tier'],"Level":survivalmastery['data']['attributes']['level']}, "Weapon":weaps}}
 
  return res

def pubgserver():
  res = dict()
  link = os.environ['PUBG-LIVE-URL']
  test = requests.get(f"https://pctest-{link}.playbattlegrounds.com/")
  live = requests.get(f"https://prod-{link}.playbattlegrounds.com/")
  try:
    test = test.json()['health']
    if test == True:
      res['TestServer'] = True
  except:
    res['TestServer'] = False

  try:
    live = live.json()['health']
    if live == True:
      res['LiveServer'] = True
  except:
    res['LiveServer'] = False
  
  return res
  
def pubgmatches(shard, matchId):
  return requests.get(f"https://api.pubg.com/shards/{shard}/matches/{matchId}",headers={"Accept":"application/vnd.api+json"}).json()

def pubgtelemetry(shard, matchId):
  matches = pubgmatches(shard, matchId)
  for x in matches['included']:
    if x['type'] == "asset":
      return {"data":x['attributes']['URL']}
  return {"data":None}
