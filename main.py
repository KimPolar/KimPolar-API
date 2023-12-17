from fastapi import FastAPI
import krmetro as km
import json, random

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
