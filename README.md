# Pokémon Battle Simulation — MCP Server

This project implements a **Model Context Protocol (MCP) server** that gives AI models access to:

1. **Pokémon Data Resource** – Fetches comprehensive Pokémon information (stats, types, abilities, moves, evolution).
2. **Battle Simulation Tool** – Simulates a battle between any two Pokémon, including type effectiveness and basic status effects.

A **FastAPI** app is included for local API testing.

---

## Requirements

* Python **3.10+** (tested on 3.13)
* Internet connection (uses [PokéAPI](https://pokeapi.co))

---

##  Installation

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

You can run the server directly:

```bash
python -m server.mcp_server
```

Or via the FastAPI app (optional):

```bash
uvicorn server.main:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

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

* Replace `/absolute/path/to/project` with your actual local project directory path.
* Keep forward slashes `/` in the path for compatibility across OSes.
* `PYTHONPATH` ensures imports work when the server is launched from Claude.

3. **Restart Claude Desktop** for changes to apply.

---

## Example Usage in Claude

Once connected, you can try:

```
list tools
```

Or simulate a battle:

```
simulate a battle between pikachu and bulbasaur
```

---

## Deliverables

This project satisfies the MCP technical assessment by providing:

* A Pokémon Data Resource (MCP Resource)
* A Battle Simulation Tool (MCP Tool)
* Documentation & setup instructions
* FastAPI optional testing endpoint

---

## Credits

Developed by **Dimple Kundu** — special thanks to **Scopely** for the opportunity.

---

Alright — here’s the updated README with a **Quick Start** section right at the top so reviewers can get your Pokémon MCP server running in just two commands.

---

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

