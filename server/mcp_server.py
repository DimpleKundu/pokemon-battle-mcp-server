from mcp.server.fastmcp import FastMCP
from server.data import fetch_pokemon
from server.battle import simulate_battle

# Create MCP server instance
mcp = FastMCP("Pokemon MCP Server")

# Pokémon Data Tool
@mcp.tool()
def pokemon_data(name: str):
    """Get Pokémon stats, types, abilities, moves, and evolution info."""
    return fetch_pokemon(name)

# Battle Simulation Tool
@mcp.tool()
def battle_simulator(pokemon1: str, pokemon2: str):
    """Simulate a battle between two Pokémon."""
    return simulate_battle(pokemon1, pokemon2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
