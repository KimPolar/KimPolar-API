from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/leaderboards/")
async def leader(season:str, server:str):
    with open('leaderboards.json') as f:
        a = json.load(f)
    return a[season][server]
