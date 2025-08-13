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

Direct run:

```bash
python -m server.mcp_server
```

Or via FastAPI for API testing:

```bash
uvicorn server.main:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Project Structure

```
pokeaiagent/
│
├── server/
│   ├── __init__.py
│   ├── battle.py         # Battle mechanics
│   ├── data.py           # Pokémon data fetcher
│   ├── main.py           # FastAPI app
│   └── mcp_server.py     # MCP server entrypoint
│
├── requirements.txt
└── README.md
```

---

## onnecting to Claude Desktop (MCP)

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
list tools
simulate a battle between pikachu and bulbasaur
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

