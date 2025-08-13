# Pokémon Battle Simulation — MCP Server

This project provides an **MCP server** with two main tools:

1. **Pokémon Data Tool** – Fetches detailed Pokémon information (stats, types, abilities, moves, evolution).
2. **Battle Simulation Tool** – Simulates a battle between any two Pokémon, including type effectiveness and basic status effects.

A **FastAPI** app is also included for quick local testing, along with a small Python client script.

---

##  Quick Start

### 0) Requirements

* Python 3.10+ (tested on 3.13)
* Internet connection (data fetched from [PokéAPI](https://pokeapi.co))

### 1) Setup

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install requirements.txt
```

### 2) Run MCP Server

```bash
python server/mcp_server.py
```

### 3) Run FastAPI Server (optional)

```bash
uvicorn server.main:app --reload
```

Open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 4) Test with Client Script

```bash
python client/test_client.py
```

---

## 📂 Project Structure

```
pokeaiagent/
│
├── server/
│   ├── __init__.py
│   ├── battle.py          # Battle mechanics
│   ├── data.py            # Pokémon data fetcher
│   ├── main.py            # FastAPI app
│   └── mcp_server.py      # MCP server tools
│
├── client/
│   └── test_client.py     # Simple HTTP test script
│
├── requirements.txt
└── README.md
```

---

