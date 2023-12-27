from fastapi import FastAPI
import krmetro as km, hangang as hg, json, random, color, pubg, os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
async def root():
    return "KimPolar's API"

@app.get("/pubg/leaderboards/")
async def leader(season:str, server:str):
    with open('leaderboards.json') as f:
        a = json.load(f)
    return a[season][server]

@app.get("/metro/korea/")
async def krmetro(lineNum:str):
    return km.getData(lineNum)

@app.get("/quote/")
async def quote():
    with open('quote.json') as f:
        a = json.load(f)
    return random.choice(a)

@app.get("/hangang/")
async def hangang():
    return hg.hangang()

@app.get("/color/complement/")
async def compc(RGB:str):
    RGB = str(RGB)
    return color.compcolor(RGB)

@app.get("/pubg/weapon/")
async def weapon():
    with open("weapon.json") as f:
        a = json.load(f)
    return a
    
@app.get("/pubg/mastery/")
async def masteryfind(accountId):
    return pubg.finder(accountId)

@app.get("/pubg/status/")
async def pubgstatus():
    return pubg.pubgserver()

app.mount("/pubg/weapon/raw/", StaticFiles(directory="pubg/weapon/"), name="weaponraw")
