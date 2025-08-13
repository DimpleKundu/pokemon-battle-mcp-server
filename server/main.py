from fastapi import FastAPI
from server.data import fetch_pokemon
from server.battle import simulate_battle

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MCP Pokemon Server"}

@app.get("/pokemon/{name}")
def get_pokemon(name:str):
    return fetch_pokemon(name)

@app.get("/battle/{p1}/{p2}")
def battle(p1: str, p2: str):
    return simulate_battle(p1, p2)



