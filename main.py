from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"KimPolar's API"}

@app.get("/pubg/leaderboards/")
async def leader(season:str, server:str):
    with open('leaderboards.json') as f:
        a = json.load(f)
    return a[season][server]
