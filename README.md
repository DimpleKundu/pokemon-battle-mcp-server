# Pokémon Battle Simulation — MCP Server

This project is a **Model Context Protocol (MCP) server** that gives AI models access to two Pokémon-related capabilities:

1. **Pokémon Data Resource** — Fetches detailed Pokémon data from [PokéAPI](https://pokeapi.co), including:

   * Base stats (HP, Attack, Defense, Special Attack, Special Defense, Speed)
   * Types (Fire, Water, Grass, etc.)
   * Abilities
   * Moves and effects
   * Evolution data
2. **Battle Simulation Tool** — Simulates a Pokémon battle between any two Pokémon with:

   * Type effectiveness (e.g., Water > Fire)
   * Damage calculations based on stats and move power
   * Speed-based turn order
   * 3 status effects: **Paralysis**, **Burn**, **Poison**
   * Full battle logs and winner determination

---

## 📦 Requirements

* Python **3.10+** (tested on Python 3.13)
* Internet connection (data is fetched live from PokéAPI)
* A working Claude Desktop installation (optional, for AI testing)

---

## 🚀 Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the MCP server

You can run the server directly:

```bash
python -m server.mcp_server
```

Or via FastAPI (HTTP interface):

```bash
uvicorn server.main:app --reload
```

FastAPI will start at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Project Structure

```
pokeaiagent/
│
├── server/
│   ├── __init__.py
│   ├── battle.py        # Battle mechanics
│   ├── data.py          # Pokémon data fetching
│   ├── main.py          # FastAPI app for testing
│   └── mcp_server.py    # MCP server (main entrypoint)
│
├── requirements.txt
└── README.md
```

---

## 🧪 Testing in Browser (FastAPI)

1. Start FastAPI:

   ```bash
   uvicorn server.main:app --reload
   ```
2. Open in browser:

   ```
   http://127.0.0.1:8000/docs
   ```
3. You can try:

   * `GET /pokemon/{name}` — fetch Pokémon data
   * `POST /battle` — simulate a battle

Example request body for `/battle`:

```json
{
  "pokemon1": "pikachu",
  "pokemon2": "charmander"
}
```

---

## 🤖 Connecting to Claude Desktop (MCP)

1. **Locate Claude’s MCP config folder:**

   * macOS: `~/Library/Application Support/Claude/`
   * Windows: `%AppData%\Claude\`
   * Linux: `~/.config/Claude/`

2. **Edit (or create) `mcp.json`** and add:

```json
{
  "servers": {
    "pokemon-battle": {
      "command": "python",
      "args": ["-m", "server.mcp_server"],
      "cwd": "/absolute/path/to/pokeaiagent"
    }
  }
}
```

3. **Restart Claude Desktop**.

4. Inside Claude, type something like:

   ```
   list tools
   ```

   or

   ```
   simulate a battle between pikachu and bulbasaur
   ```

   Claude will call the MCP server.

---

## 📌 Notes

* The MCP server fetches live data from PokéAPI — no local DB required.
* Battle results are **deterministic** (no RNG for this implementation).
* MCP and FastAPI are independent — you can run either or both.

---
