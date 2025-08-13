# Pokémon Battle Simulation — MCP Server

## Quick Start

```bash
git clone https://github.com/your-username/pokeaiagent.git
cd pokeaiagent
pip install -r requirements.txt
python -m server.mcp_server
```

> Server will start and wait for MCP-compatible clients (like Claude Desktop) to connect.

---

## Requirements

* Python **3.10+** (tested on 3.13)
* Internet connection (uses [PokéAPI](https://pokeapi.co))

---

## Installation

```bash
git clone https://github.com/your-username/pokeaiagent.git
cd pokeaiagent

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## Running the MCP Server

**Direct run:**

```bash
python -m server.mcp_server
```

**Or via FastAPI for API testing:**

```bash
uvicorn server.main:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## FastAPI Endpoints

| Endpoint            | Method | Description                                                    |
| ------------------- | ------ | -------------------------------------------------------------- |
| `/`                 | GET    | Returns a welcome message: `{"message": "MCP Pokemon Server"}` |
| `/pokemon/{name}`   | GET    | Fetch Pokémon data by name (uses PokéAPI)                      |
| `/battle/{p1}/{p2}` | GET    | Simulate a battle between two Pokémon by name                  |

**Example usage:**

```python
GET /pokemon/pikachu
# Returns Pikachu's data

GET /battle/pikachu/bulbasaur
# Returns simulated battle results
```

**Code snippet (`server/main.py`):**

```python
from fastapi import FastAPI
from server.data import fetch_pokemon
from server.battle import simulate_battle

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MCP Pokemon Server"}

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    return fetch_pokemon(name)

@app.get("/battle/{p1}/{p2}")
def battle(p1: str, p2: str):
    return simulate_battle(p1, p2)
```

---

## Project Structure

```
pokeaiagent/
│
├── server/
│   ├── __init__.py
│   ├── battle.py         # Battle mechanics
│   ├── data.py           # Pokémon data fetcher
│   ├── main.py           # FastAPI app with endpoints
│   └── mcp_server.py     # MCP server entrypoint
│
├── requirements.txt
└── README.md
```

---

## Connecting to Claude Desktop (MCP)

1. **Find Claude MCP config folder:**

   * **macOS:** `~/Library/Application Support/Claude/`
   * **Windows:** `%AppData%\Claude\`
   * **Linux:** `~/.config/Claude/`

2. **Edit (or create) `claude_desktop_config.json`** and add:

```json
{
  "mcpServers": {
    "pokemon": {
      "command": "python",
      "args": [
        "/absolute/path/to/project/server/mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "/absolute/path/to/project"
      }
    }
  }
}
```

**Notes:**

* Replace `/absolute/path/to/project` with your actual local project path.
* Keep forward slashes `/` for compatibility.
* `PYTHONPATH` ensures imports work when launched from Claude.

3. **Restart Claude Desktop** to load the MCP server.

---

## Example Usage in Claude

```
1. list tools
2. simulate a battle between pikachu and bulbasaur
```

**Prompt:** `simulate a battle between pikachu and bulbasaur`

**Response:**

```
battle_simulator

What a quick and decisive battle!

Pikachu vs Bulbasaur Battle Summary:

This battle featured two of the most iconic starter Pokémon, but it was surprisingly one-sided. Both Pokémon started with nasty status conditions - Pikachu was burned while Bulbasaur was poisoned.

Turn 1:
- Pikachu struck first but only managed 5 damage against Bulbasaur
- Bulbasaur retaliated with a devastating 23 damage attack, nearly KO'ing Pikachu in one hit!
- Both Pokémon then took damage from their status conditions

Turn 2:
- Pikachu tried again with another weak 5-damage attack
- Bulbasaur finished the job with another 23-damage blow, knocking out Pikachu completely

Result: Bulbasaur wins!

Despite being poisoned and losing HP each turn, Bulbasaur completely dominated with attacks over 4× stronger than Pikachu's moves. Bulbasaur finished with 27 HP remaining, having taken minimal damage. This matchup heavily favored Bulbasaur.
```

---

## Deliverables

This project satisfies the MCP technical assessment by providing:

* Pokémon Data Resource (MCP Resource)
* Battle Simulation Tool (MCP Tool)
* Full setup instructions
* Optional FastAPI testing

---

## Credits

Developed by **Dimple Kundu** — thanks to **Scopely** for the opportunity.

---

