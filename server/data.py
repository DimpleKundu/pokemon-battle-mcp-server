import requests

POKEAPI_BASE = "https://pokeapi.co/api/v2/"

def fetch_pokemon(name):
    r = requests.get(f"{POKEAPI_BASE}pokemon/{name.lower()}")
    if r.status_code != 200:
        return {"error": "Pokémon not found"}
    
    d = r.json()
    stats = {s['stat']['name']: s['base_stat'] for s in d['stats']}
    types = [t['type']['name'] for t in d['types']]
    abilities = [a['ability']['name'] for a in d['abilities']]
    moves = [m['move']['name'] for m in d['moves'][:4]]

    species_data = requests.get(d['species']['url']).json()
    evolution_chain_url = species_data['evolution_chain']['url']

    return {
        "name": d['name'],
        "stats": stats,
        "types": types,
        "abilities": abilities,
        "moves": moves,
        "evolution_chain_url": evolution_chain_url
    }
